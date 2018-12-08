import urllib
import pandas as pd
import arcpy
import arcpy.mapping
import zipfile


# declare variable inputs
borocode = '1'  # '1' for Manhattan, '2' for Bronx, '3' for Brooklyn, '4' for Queens, '5' for Staten Island
corridor = 'BROADWAY'  # eg corridor = 'BROADWAY'
buffer_distance = '40 feet'  # pick the best distance to capture all trees on both sides of the road
district_type = 'nycd'  # choose 'nynta' for neighborhood tabulation areas or 'nycd' for community ditsricts
district_numbers = (112, 109, 107)  # choose which district numbers from the above that you want as your segments
year_code = '18'  # the last two digits of the current year, as a string
quarter_code = 'c'  # which quarter of the year you are downloading it in

# establish the arcmap workspace
mxd = arcpy.mapping.MapDocument('E:\SAVI810\Final_Project\MXD\Workspace.mxd')
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
arcpy.env.workspace = r'E:\SAVI810\Final_Project\Data\shape'
arcpy.env.overwriteOutput = 'True'


# downloading the necessary files from OpenData
def download_file_from_web(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.urlretrieve(url, file_name)


download_file_from_web('https://data.cityofnewyork.us/api/geospatial/exjm-f27b?method=export&format=Original',
                       r'E:\SAVI810\Final_Project\Data\shape\inputs\centerlineshp.zip')
zf_centerline = zipfile.ZipFile(r'E:\SAVI810\Final_Project\Data\shape\inputs\centerlineshp.zip')
zf_centerline.extractall(r'E:\SAVI810\Final_Project\Data\shape\inputs')


# add centerline data
centerline_location = arcpy.mapping.Layer(r'E:\SAVI810\Final_Project\Data\shape\inputs\centerline.shp')
arcpy.mapping.AddLayer(df, centerline_location, "BOTTOM")
centerline = arcpy.mapping.ListLayers(mxd)[0]


# select and export the corridor from centerline
def export_the_corridor(in_corridor, in_borocode):
    sql_statement = ''' "FULL_STREE"= {0}{1}{0} AND "BOROCODE" = {0}{2}{0} '''.format('~',
                                                                                      in_corridor,
                                                                                      in_borocode).replace("~", "'")
    arcpy.FeatureClassToFeatureClass_conversion(
        centerline,
        r'E:\SAVI810\Final_Project\Data\shape\corridor',
        "{}".format(in_corridor.replace(" ", "_")),
        sql_statement,
    )


export_the_corridor(corridor, borocode)


# add the corridor to the map and name the file
corridor_location = arcpy.mapping.Layer(r"E:\SAVI810\Final_Project\Data\shape\corridor\{}.shp"
                                        .format(corridor.replace(" ", "_")))


arcpy.mapping.AddLayer(df, corridor_location, "BOTTOM")
full_corridor = arcpy.mapping.ListLayers(mxd)[1]
arcpy.SelectLayerByAttribute_management(centerline, "CLEAR_SELECTION")


# create a 40 foot buffer around the corridor
buffer_path = r'E:\SAVI810\Final_Project\Data\shape\corridor\{}_buffer'.format(corridor.replace(" ", "_"))


def buffer_the_corridor(in_file, out_file, buffering_distance):
    arcpy.Buffer_analysis(in_file, out_file, buffering_distance)


buffer_the_corridor(full_corridor, buffer_path, buffer_distance)


# add the buffered corridor to the map
full_corridor_buffered_location = arcpy.mapping.Layer(
    r'E:\SAVI810\Final_Project\Data\shape\corridor\{}_buffer.shp'.format(corridor.replace(" ", "_")))
arcpy.mapping.AddLayer(df, full_corridor_buffered_location, "BOTTOM")
full_corridor_buffered = arcpy.mapping.ListLayers(mxd)[2]


# clip the buffer by CDs or NTAs

# first, download and extract the relevant district file
# QUESTION: can i pull out the zipfile extraction parts below the if statements so that it would apply to both?
def download_the_districts(in_district):
    if in_district == 'nycd':
        download_file_from_web(
            'https://data.cityofnewyork.us/api/geospatial/yfnk-k7r4?method=export&format=Original',
            r'E:\SAVI810\Final_Project\Data\shape\district\{}shp.zip'.format(in_district)
        )
        zf_cd = zipfile.ZipFile(r'E:\SAVI810\Final_Project\Data\shape\district\{}shp.zip'.format(in_district))
        zf_cd.extractall(r'E:\SAVI810\Final_Project\Data\shape\district')
    else:
        download_file_from_web(
            'https://data.cityofnewyork.us/api/geospatial/cpf4-rkhq?method=export&format=Original',
            r'E:\SAVI810\Final_Project\Data\shape\district\{}shp.zip'.format(in_district)
        )
        zf_nta = zipfile.ZipFile(r'E:\SAVI810\Final_Project\Data\shape\district\{}shp.zip'.format(in_district))
        zf_nta.extractall(r'E:\SAVI810\Final_Project\Data\shape\district')


download_the_districts(district_type)


# add the master district file to the map
# QUESTION: can I add a wild card in the nycd_18c statement so that this function
# would work even if you download a later version of the nycd file
def set_district_type_location(in_district):
    global district_type_location
    if in_district == 'nycd':
        district_type_location = arcpy.mapping.Layer(
            r'E:\SAVI810\Final_Project\Data\shape\district\{}_{}{}\{}.shp'.format(district_type,
                                                                                  year_code,
                                                                                  quarter_code,
                                                                                  district_type))
    else:
        district_type_location = arcpy.mapping.Layer(
            r'E:\SAVI810\Final_Project\Data\shape\district\{}_{}{}\{}.shp'.format(district_type,
                                                                                  year_code,
                                                                                  quarter_code,
                                                                                  district_type))


set_district_type_location(district_type)
arcpy.mapping.AddLayer(df, district_type_location, "BOTTOM")
master_district = arcpy.mapping.ListLayers(mxd)[3]


# extract each community district of interest
def extract_districts(in_districts):
    for i in in_districts:
        sql_statement = ''' "BoroCD"= {0} '''.format(i)
        arcpy.FeatureClassToFeatureClass_conversion(
            master_district,
            r'E:\SAVI810\Final_Project\Data\shape\district',
            '{0}_{1}'.format(district_type, i),
            sql_statement
        )


extract_districts(district_numbers)


# clip the corridor buffer to the relevant CDs or NTAs
arcpy.env.workspace = r'E:\SAVI810\Final_Project\Data\shape\district'


def clip_the_buffer(in_list, in_buffer):
    list_of_segments = []
    for i in in_list:
        arcpy.Clip_analysis(
            in_buffer,
            r'E:\SAVI810\Final_Project\Data\shape\district\{}_{}.shp'.format(district_type, i),
            r'E:\SAVI810\Final_Project\Data\shape\segment\segment_{0}_{1}.shp'.format(district_type, i),
        )
        list_of_segments.append(
            r'E:\SAVI810\Final_Project\Data\shape\segment\segment_{0}_{1}.shp'.format(district_type, i))
    return list_of_segments


segment_list = clip_the_buffer(district_numbers, full_corridor_buffered)

# download treepoints
download_file_from_web("https://data.cityofnewyork.us/api/views/k5ta-2trh/rows.csv?accessType=DOWNLOAD",
                       r'E:\SAVI810\Final_Project\Data\table\treepoints.csv')


# separate long and lat in treepoints to their own columns
trees = r'E:\SAVI810\Final_Project\Data\table\treepoints.csv'
df_trees = pd.read_csv(trees)
df_trees['latitude'] = df_trees['Location'].str.split('(').str[1].str.split(' ').str[0].str.replace(',', '')
df_trees['longitude'] = df_trees['Location'].str.split(' ').str[1].str.replace(')', '')

# export the dataframe to a fresh csv to use in arc
out_trees = trees.replace('.csv', '_clean.csv')
df_trees.to_csv(out_trees, index=False)

# show treepoint data
# State_Plane = arcpy.SpatialReference(4456)
arcpy.MakeXYEventLayer_management(
    out_trees,
    'longitude',
    'latitude',
    "trees_layer",
)

# copy the features to a layer, add it to the map
arcpy.CopyFeatures_management("trees_layer", r'E:\SAVI810\Final_Project\Data\shape\inputs\treepoints.shp')

treepoints_location = arcpy.mapping.Layer(r'E:\SAVI810\Final_Project\Data\shape\inputs\treepoints.shp')
arcpy.mapping.AddLayer(df, treepoints_location, "BOTTOM")
treepoints = arcpy.mapping.ListLayers(mxd)[4]


# select treepoints by location for each segment
def intersect_trees_and_segments(in_trees, selection_type, selection_list, district_nums):
    list_of_treepoints_by_segment_inside = []
    for i in (range(len(selection_list))):
        input_extent = selection_list[i]
        district_number = district_nums[i]
        arcpy.SelectLayerByLocation_management(
            in_trees,
            selection_type,
            input_extent,
        )
        arcpy.CopyFeatures_management(
            in_trees,
            r'E:\SAVI810\Final_Project\Data\shape\segment\{0}_{1}_treepoints.shp'.format(district_type, district_number)
        )
        list_of_treepoints_by_segment_inside.append(r'E:\SAVI810\Final_Project\Data\shape\segment\{0}_{1}_treepoints.shp'
                                                    .format(district_type, district_number))
    return list_of_treepoints_by_segment_inside


list_of_treepoints_by_segment = intersect_trees_and_segments(
    treepoints,
    'intersect',
    segment_list,
    district_numbers
)
