import arcpy
import json
import urllib
import urllib2
import pandas as pd
import os
import zipfile


def run_bikeshare_route(config_json):
    # This function runs the full bikeshare route finder

    import_bikeshare_data(config_json)
    find_nearest_stations(config_json)
    solve_network(config_json)
    save_result(config_json)


def get_station_list(bike_json_addr):
    # bike_json_addr = Toronto Bikeshare json response url

    # receive json response
    response = urllib2.urlopen(bike_json_addr)

    # read raw response into python variable
    bike_json = response.read()

    # load raw response as python dictionary
    load_bike_json = json.loads(bike_json)

    # pull list of bikeshare json feed urls
    feeds_bike_json = load_bike_json['data']['en']['feeds']

    # initialize station info deed url variable
    station_info_url = ''

    # loop through feeds to find station info url
    for url_loop in feeds_bike_json:
        if url_loop['name'] == 'station_information':
            station_info_url = url_loop['url']

    # receive json response
    station_info_response = urllib2.urlopen(station_info_url)

    # read raw response into python variable
    station_info_json = station_info_response.read()

    # load raw response as python dictionary
    load_station_info_json = json.loads(station_info_json)

    # pull list of data about bikeshare stations
    station_list = load_station_info_json['data']['stations']

    print('Station List Import Complete!')
    return station_list


def station_list_to_csv(station_list, csv_path):
    station_list_df = pd.DataFrame(station_list)
    station_list_df.to_csv(csv_path, encoding='utf-8')

    print('List to CSV Conversion Complete!')


def travel_pt_list_to_csv(pt_list, csv_path):
    pt_list_df = pd.DataFrame(pt_list).transpose()
    pt_list_df.to_csv(csv_path, encoding='utf-8')

    print('Travel Point List to CSV Conversion Complete!')


def clear_data_dir(gdb_dir, shapefile_dir, save_dir):
    gdb_name = r'Bikeshare_GDB'
    gdb_path = gdb_dir + r'/' + gdb_name + r'.gdb'

    # set arcpy workspace
    arcpy.env.workspace = gdb_path
    arcpy.ResetEnvironments()
    arcpy.env.overwriteOutput = True

    # check if data directory exists, and delete it, if yes
    if os.path.exists(gdb_dir):
        arcpy.Delete_management(gdb_dir)

    # create empty directories for geodatabase and shapefiles
    os.mkdir(gdb_dir)
    os.mkdir(shapefile_dir)

    # check if save directory exists, and create, if not
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print('Directory Clear and Refresh Complete!')


def read_config_json(config_json):
    # this function reads configuration data from a config.json file
    with open(config_json) as f:
        data = json.load(f)

    print('Read config.json Complete!')
    return data


def bike_data_to_gdb(shapefile_path, csv_path, travel_pt_path, gdb_feature_path):
    # This function reads the bike lane and bikeshare station data,
    # reprojects it into a geodatabase with the proper spatial reference system,
    # and adds makes relevant modifications to the initial data

    # read bikeway shapefile and pull out only routes suitable for bike traffic
    arcpy.MakeFeatureLayer_management(
        shapefile_path,
        "CENTRELINE_BIKEWAY_OD_Layer",
        """ ( "CP_TYPE" <> ' ' ) OR 
        ( "FCODE_DESC" = 'Local' ) OR 
        ( "FCODE_DESC" = 'Collector' ) OR 
        ( "FCODE_DESC" = 'Collector Ramp' ) OR 
        ( "FCODE_DESC" = 'Minor Arterial' ) OR 
        ( "FCODE_DESC" = 'Minor Arterial Ramp' ) OR 
        ( "FCODE_DESC" = 'Laneway' ) OR 
        ( "FCODE_DESC" = 'Major Arterial' ) OR 
        ( "FCODE_DESC" = 'Major Arterial Ramp' ) """
    )

    # copy bike routes selection layer into geodatabase
    arcpy.FeatureClassToGeodatabase_conversion(
        "CENTRELINE_BIKEWAY_OD_Layer",
        gdb_feature_path
    )

    # create bikeshare station points layer
    arcpy.MakeXYEventLayer_management(csv_path, "lon", "lat", "bike_stations_layer")

    # reproject the bikeshare station points layer into the geodatabase with the correct projection
    arcpy.Project_management(
        "bike_stations_layer",
        (gdb_feature_path + r'/Bike_Stations'),
        """PROJCS['NAD27_MTM_zone_10',
        GEOGCS['GCS_North_American_1927',
        DATUM['D_North_American_1927',
        SPHEROID['Clarke_1866',6378206.4,294.9786982]],
        PRIMEM['Greenwich',0.0],
        UNIT['Degree',0.0174532925199433]],
        PROJECTION['Transverse_Mercator'],
        PARAMETER['False_Easting',304800.0],
        PARAMETER['False_Northing',0.0],
        PARAMETER['Central_Meridian',-79.5],
        PARAMETER['Scale_Factor',0.9999],
        PARAMETER['Latitude_Of_Origin',0.0],
        UNIT['Meter',1.0]
        ]""",
        "'WGS_1984_(ITRF00)_To_NAD_1983 + NAD_1927_To_NAD_1983_NADCON'",
    )

    # create travel points layer
    arcpy.MakeXYEventLayer_management(travel_pt_path, "lon", "lat", "travel_points_layer")

    # reproject the bikeshare station points layer into the geodatabase with the correct projection
    arcpy.Project_management(
        "travel_points_layer",
        (gdb_feature_path + r'/Travel_Points'),
        """PROJCS['NAD27_MTM_zone_10',
        GEOGCS['GCS_North_American_1927',
        DATUM['D_North_American_1927',
        SPHEROID['Clarke_1866',6378206.4,294.9786982]],
        PRIMEM['Greenwich',0.0],
        UNIT['Degree',0.0174532925199433]],
        PROJECTION['Transverse_Mercator'],
        PARAMETER['False_Easting',304800.0],
        PARAMETER['False_Northing',0.0],
        PARAMETER['Central_Meridian',-79.5],
        PARAMETER['Scale_Factor',0.9999],
        PARAMETER['Latitude_Of_Origin',0.0],
        UNIT['Meter',1.0]
        ]""",
        "'WGS_1984_(ITRF00)_To_NAD_1983 + NAD_1927_To_NAD_1983_NADCON'",
    )

    # prepare stations and routes for network dataset
    snap_and_split(gdb_feature_path)

    # add necessary data fields to bike route data
    add_data_fields(gdb_feature_path)

    print('Data to GDB Load Complete!')


def snap_and_split(gdb_feature_path):
    # This function snaps bike station points to the closest bike route
    # and splits the route segments at the station points

    # snap bike station points to closest line segment
    arcpy.Snap_edit(
        (gdb_feature_path + r'/Bike_Stations'),
        (gdb_feature_path + r"/CENTRELINE_BIKEWAY_OD_Layer EDGE '100 Meters'")
    )

    # split bike route line segments at station points (necessary for proper network analyst calculations)
    arcpy.SplitLineAtPoint_management(
        (gdb_feature_path + r'/CENTRELINE_BIKEWAY_OD_Layer'),
        (gdb_feature_path + r'/Bike_Stations'),
        (gdb_feature_path + r'/Bikeways_Split'),
        "1 Meters"
    )

    print('Snap and Split Complete!')


def add_data_fields(gdb_feature_path):
    # This function adds fields necessary for calculating network paths

    # add length field to split bike routes
    arcpy.AddGeometryAttributes_management(
        (gdb_feature_path + r'/Bikeways_Split'),    # input field
        "LENGTH",                                   # new field name
        "METERS"                                    # new field units
    )

    # add speed field in bike route data
    arcpy.AddField_management(
        (gdb_feature_path + r'/Bikeways_Split'),    # input table
        "SPEED_MPS",                                # new field name
        "DOUBLE",                                   # field type
        "5",                                        # field precision
        "2",                                        # field scale
        "",                                         # field length
        "",                                         # field alias
        "NULLABLE",                                 # is field nullable
        "NON_REQUIRED",                             # is field required
        ""                                          # field domain
    )

    # calculate speed on each route segment in meters / second
    # bicycle speeds estimated from wikipedia article
    #    https://en.wikipedia.org/wiki/Bicycle_performance
    # street speed: 10 km/hr = 2.8 m/s
    # bike path speed: 20 km/hr = 5.6 m/s
    arcpy.CalculateField_management(
        (gdb_feature_path + r'/Bikeways_Split'),    # input table
        "SPEED_MPS",                                # field name
        "Bike_Speed(!CP_TYPE!)",                    # new field value
        "PYTHON_9.3",                               # script type
        """def Bike_Speed(cp_type):
        \n   if (cp_type == ' '):
        \n      return 2.8
        \n   else:
        \n      return 5.6"""                       # custom script
    )

    # add travel time field in bike route data
    arcpy.AddField_management(
        (gdb_feature_path + r'/Bikeways_Split'),    # input table
        "TIME_MIN",                                 # new field name
        "DOUBLE",                                   # field type
        "18",                                       # field precision
        "12",                                       # field scale
        "",                                         # field length
        "",                                         # field alias
        "NULLABLE",                                 # is field nullable
        "NON_REQUIRED",                             # is field required
        ""                                          # field domain
    )

    # calculate travel time on each route segment in minutes
    arcpy.CalculateField_management(
        (gdb_feature_path + r'/Bikeways_Split'),    # input table
        "TIME_MIN",                                 # field name
        "( !LENGTH! / !SPEED_MPS! ) / 60",          # new field value
        "PYTHON_9.3",                               # script type
        ""                                          # custom script
    )

    print('Data Field Calculations Complete!')


def import_bikeshare_data(config_json):
    # read configuration data
    config_data = read_config_json(config_json)

    # write configuration data into variables
    project_dir = config_data['directories']['project_dir']
    save_dir = config_data['directories']['save_dir']
    bike_json_addr = config_data['links']['bike_json_addr']
    bikelane_data_url = config_data['links']['bikelane_data_url']
    travel_pt_list = config_data['locations']

    # set directory and path for bikeshare locations csv
    csv_dir = project_dir + r'/Data'
    csv_name = 'station_list'
    csv_path = csv_dir + r'/' + csv_name + r'.csv'

    # set directory and path for start and end points
    travel_pt_list_name = 'travel_points_list'
    travel_pt_path = csv_dir + r'/' + travel_pt_list_name + r'.csv'

    # set directory and path for bike routes shapefile
    shapefile_dir = project_dir + r'/Data/Shapefiles'
    shapefile_path = shapefile_dir + r'/CENTRELINE_BIKEWAY_OD.shp'
    bikelane_data_zip_path = shapefile_dir + r'mtm3.zip'

    # set directory and path for network geodatabase
    gdb_dir = project_dir + r'/Data'
    gdb_name = r'Bikeshare_GDB'
    gdb_path = gdb_dir + r'/' + gdb_name + r'.gdb'
    feature_dataset_name = 'Bikeshare'
    gdb_feature_path = gdb_path + r'/' + feature_dataset_name

    # clear old data
    clear_data_dir(gdb_dir, shapefile_dir, save_dir)

    # set arcpy workspace
    arcpy.env.workspace = csv_dir

    # geodatabase spatial reference
    to_sr = arcpy.SpatialReference(7991)

    # create geodatabase
    arcpy.CreateFileGDB_management(gdb_dir, gdb_name, "CURRENT")

    # create feature dataset in geodatabase
    arcpy.CreateFeatureDataset_management(gdb_path, feature_dataset_name, to_sr)

    # create list of stations
    station_list = get_station_list(bike_json_addr)

    # save station list to csv
    station_list_to_csv(station_list, csv_path)

    # save travel points list to csv
    travel_pt_list_to_csv(travel_pt_list, travel_pt_path)

    # retrieve bike route dataset
    urllib.urlretrieve(bikelane_data_url, bikelane_data_zip_path)

    # unzip bike route shapefile
    zip_ref = zipfile.ZipFile(bikelane_data_zip_path, 'r')
    zip_ref.extractall(shapefile_dir)
    zip_ref.close()

    # write original data to geodatabase
    bike_data_to_gdb(shapefile_path, csv_path, travel_pt_path, gdb_feature_path)

    del to_sr

    print('Data Import Complete!')


def find_nearest_stations(config_json):
    # This function finds the nearest bikeshare stations to the travel points,
    # creates buffers around the stations, intersects the buffers with the
    # near stations, and exports them to a new layer

    # set directory and path for network geodatabase
    config_data = read_config_json(config_json)
    project_dir = config_data['directories']['project_dir']
    gdb_dir = project_dir + r'/Data'
    gdb_name = r'Bikeshare_GDB'
    gdb_path = gdb_dir + r'/' + gdb_name + r'.gdb'
    feature_dataset_name = 'Bikeshare'
    gdb_feature_path = gdb_path + r'/' + feature_dataset_name

    # set arcpy workspace
    arcpy.env.workspace = gdb_path

    # find the nearest stations
    arcpy.Near_analysis(
        (gdb_feature_path + r'/Travel_Points'),     # input feature
        (gdb_feature_path + r'/Bike_Stations'),     # near feature
        "",                                         # search radius
        "NO_LOCATION",                              # write near location to near feature
        "NO_ANGLE",                                 # find angle to near feature
        "PLANAR"                                    # method
    )

    # buffer the travel points to the nearest stations
    arcpy.Buffer_analysis(
        (gdb_feature_path + r'/Travel_Points'),         # input feature
        (gdb_feature_path + r'/Travel_Points_Buffer'),  # output buffer feature
        "NEAR_DIST",                                    # buffer distance field
        "FULL",                                         # line side
        "ROUND",                                        # line end type
        "NONE",                                         # dissolve type
        "",                                             # dissolve field
        "PLANAR"                                        # method
    )

    # create new layer with nearest stations
    arcpy.Intersect_analysis(
        "Bike_Stations #;Travel_Points_Buffer #",           # input path
        (gdb_feature_path + r'/Bike_Stations_Intersect'),   # output path
    )

    print('Nearest Stations and Buffers Added!')


def solve_network(config_json):
    # This function creates a network dataset from a template,
    # builds the network, adds the nearest station points as stops,
    # and solves for the least-cost route

    # check network analyst license
    arcpy.CheckOutExtension("network")
    print('Network Analyst License Confirmed!')

    # set directory and path for network geodatabase
    config_data = read_config_json(config_json)
    project_dir = config_data['directories']['project_dir']
    save_dir = config_data['directories']['save_dir']
    direction_save_name = config_data['filenames']['direction_save_name']
    gdb_dir = project_dir + r'/Data'
    gdb_name = r'Bikeshare_GDB'
    gdb_path = gdb_dir + r'/' + gdb_name + r'.gdb'
    feature_dataset_name = 'Bikeshare'
    gdb_feature_path = gdb_path + r'/' + feature_dataset_name

    # set arcpy workspace
    arcpy.env.workspace = gdb_path

    # create network dataset from template
    arcpy.CreateNetworkDatasetFromTemplate_na(
        (project_dir + r'/Bikeshare_ND_template.xml'),      # network dataset template location
        gdb_feature_path                                    # feature dataset for network
    )

    # build network dataset
    arcpy.BuildNetwork_na(gdb_feature_path + r'/Bikeshare_ND')

    # create layer for least-cost route analysis
    arcpy.MakeRouteLayer_na(
        "Bikeshare_ND",             # input network dataset
        "Route",                    # output route analysis layer
        "Time",                     # impedance attribute
    )

    # add nearest station routing points
    arcpy.AddLocations_na(
        "Route",                    # input route analysis layer
        "Stops",                    # "Stops" analysis sub-layer
        "Bike_Stations_Intersect",  # input features table
        "Name Name #",              # field mapping
        "5000 Meters",              # search tolerance
        "ORIG_FID",                 # sort field
    )

    # solve the routing problem
    arcpy.Solve_na(
        "Route",                    # input route analysis layer
    )

    # export bike route as feature
    arcpy.FeatureClassToGeodatabase_conversion(
        r"Route\Routes",
        gdb_feature_path
    )

    print('Network Route Complete!')

    # export route directions
    arcpy.Directions_na(
        "Route",                                            # input route analysis layer
        "TEXT",                                             # export format
        (save_dir + r'/' + direction_save_name + r'.txt'),  # export path
        "Meters",                                           # distance units
        "REPORT_TIME",                                      # write travel time
        "Minutes"                                           # travel time units
    )
    print('Route Directions Exported!')


def save_result(config_json):
    # This function saves the network analyst results as a map document in PDF

    config_data = read_config_json(config_json)
    save_dir = config_data['directories']['save_dir']
    map_save_name = config_data['filenames']['map_save_name']
    project_dir = config_data['directories']['project_dir']
    basemap_path = config_data['layer_files']['basemap']
    save_path = save_dir + r'/' + map_save_name + r'.pdf'
    gdb_dir = project_dir + r'/Data'
    gdb_name = r'Bikeshare_GDB'
    gdb_path = gdb_dir + r'/' + gdb_name + r'.gdb'

    # set arcpy workspace
    arcpy.env.workspace = gdb_path

    # reference to map document
    mxd = arcpy.mapping.MapDocument(project_dir + r'/Bikeshare_Route.mxd')

    # reset mxd geodatabase connections
    mxd.findAndReplaceWorkspacePaths('', gdb_path)

    # add a basemap
    basemap_layer = arcpy.mapping.Layer(basemap_path)
    df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
    arcpy.mapping.AddLayer(df, basemap_layer, "BOTTOM")

    # create layer references
    route_layer = arcpy.mapping.ListLayers(mxd, "Routes")
    buffer_layer = arcpy.mapping.ListLayers(mxd, "Travel_Points_Buffer")

    # select features in view
    arcpy.SelectLayerByAttribute_management(buffer_layer[0], "NEW_SELECTION")
    arcpy.SelectLayerByAttribute_management(route_layer[0], "ADD_TO_SELECTION")

    # zoom to selected layers
    df.zoomToSelectedFeatures()

    # deselect features in view
    arcpy.SelectLayerByAttribute_management(buffer_layer[0], "CLEAR_SELECTION")
    arcpy.SelectLayerByAttribute_management(route_layer[0], "CLEAR_SELECTION")

    # refresh screen and export map
    arcpy.RefreshActiveView()
    arcpy.mapping.ExportToPDF(mxd, save_path)

    # clear database references
    del df
    del mxd
    del basemap_layer
    del route_layer
    del buffer_layer
    arcpy.Compact_management(gdb_path)

    print('Map Exported!')
