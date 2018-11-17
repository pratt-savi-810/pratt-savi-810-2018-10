import arcpy
import json
import urllib
import urllib2
import pandas as pd
import shutil
import os
import zipfile


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

    return station_list


def station_list_to_csv(station_list, csv_path):
    station_list_df = pd.DataFrame(station_list)
    station_list_df.to_csv(csv_path, encoding='utf-8')


def clear_data_dir(gdb_dir, shapefile_dir):
    # delete data directory
    shutil.rmtree(gdb_dir, ignore_errors=False)

    # create empty directories for geodatabase and shapefiles
    os.mkdir(gdb_dir)
    os.mkdir(shapefile_dir)


def import_bikeshare_data(project_dir, bike_json_addr, bikelane_data_url):
    # set directory and path for bikeshare locations csv
    csv_dir = project_dir + r'/Data'
    csv_name = 'station_list'
    csv_path = csv_dir + r'/' + csv_name + r'.csv'

    # set directory and path for bike routes shapefile
    shapefile_dir = project_dir + r'/Data/Shapefiles'
    bikelane_data_zip_path = shapefile_dir + r'mtm3.zip'

    # set directory and path for network geodatabase
    gdb_dir = project_dir + r'/Data'
    gdb_name = r'Test_GDB'
    gdb_path = gdb_dir + r'/' + gdb_name + r'.gdb'
    feature_dataset_name = 'Bikeshare'

    # clear old data
    clear_data_dir(gdb_dir, shapefile_dir)

    # set arcpy workspace
    arcpy.env.workspace = csv_dir

    # geodatabase spatial reference
    to_sr = arcpy.SpatialReference(2019)

    # create list of stations
    station_list = get_station_list(bike_json_addr)

    # save station list to csv
    station_list_to_csv(station_list, csv_path)

    # create geodatabase
    arcpy.CreateFileGDB_management(gdb_dir, gdb_name, "CURRENT")

    # retrieve bike route dataset
    urllib.urlretrieve(bikelane_data_url, bikelane_data_zip_path)

    # unzip bike route shapefile
    zip_ref = zipfile.ZipFile(bikelane_data_zip_path, 'r')
    zip_ref.extractall(shapefile_dir)
    zip_ref.close()

    # create feature dataset in geodatabase
    arcpy.CreateFeatureDataset_management(gdb_path, feature_dataset_name, to_sr)

    # export bike routes to geodatabase feature dataset
    arcpy.FeatureClassToGeodatabase_conversion(
        (shapefile_dir + r'/CENTRELINE_BIKEWAY_OD.shp'),
        (gdb_path + r'/Bikeshare')
    )

    # create bikeshare station points layer
    arcpy.MakeXYEventLayer_management(csv_path, "lon", "lat", "bike_stations_layer")

    # Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
    # The following inputs are layers or table views: "bike_stations_layer"
    arcpy.Project_management(
        "bike_stations_layer",
        (gdb_path + r'/Bikeshare/Bike_Stations'),
        "PROJCS['NAD27_MTM_zone_10',GEOGCS['GCS_North_American_1927',DATUM['D_North_American_1927',SPHEROID['Clarke_1866',6378206.4,294.9786982]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',304800.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-79.5],PARAMETER['Scale_Factor',0.9999],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]",
        "'WGS_1984_(ITRF00)_To_NAD_1983 + NAD_1927_To_NAD_1983_NADCON'",
    )


