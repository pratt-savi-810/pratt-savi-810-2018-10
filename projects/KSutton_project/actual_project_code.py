import urllib
import pandas as pd
import arcpy
import arcpy.mapping
from arcpy import env
import zipfile

arcpy.env.overwriteOutput = 'True'

# downloading the necessary files from OpenData
def download_file_from_web(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.urlretrieve(url, file_name)

download_file_from_web('https://data.cityofnewyork.us/api/geospatial/exjm-f27b?method=export&format=Original',
                       r'E:\SAVI810\Final_Project\Data_Test\shape\centerlineshp.zip')



zf_centerline = zipfile.ZipFile(r'E:\SAVI810\Final_Project\Data_Test\shape\centerlineshp.zip')
zf_centerline.extractall(r'E:\SAVI810\Final_Project\Data_Test\shape')

# establish the arcmap workspace
mxd = arcpy.mapping.MapDocument('E:\SAVI810\Final_Project\MXD\Workspace.mxd')
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
arcpy.env.workspace = r'E:\SAVI810\Final_Project\Data_Test\shape'


#add centerline data
centerline_location = arcpy.mapping.Layer(r'E:\SAVI810\Final_Project\Data_Test\shape\centerline.shp')
arcpy.mapping.AddLayer(df, centerline_location, "BOTTOM")
print('added centerline')
centerline = arcpy.mapping.ListLayers(mxd)[0]

# I couldn't get this to work. It's supposed to take the borough of the corridor and output the borough code
# as listed in the centerline dataset
# def borough_identifier(borough):
#     if borough='Manhattan':
#         borough_code = '1'
#     else:
#         if borough = 'Bronx':
#             borough_code = '2'
#         else:
#             if borough = 'Brooklyn:
#                 borough_code = '3'
#             else:
#                 if borough = 'Queens'
#                 borough_code = '4'
#             else borough_code = '5'
#     return borough_code

# select and export the corridor from centerline
mn_borocode = '1'
corridor = 'BROADWAY'
def export_the_corridor(corridor, borocode):
    sql_statement = ''' "FULL_STREE"= {0}{1}{0} AND "BOROCODE" = {0}{2}{0} '''.format('~', corridor, borocode).replace("~", "'")
    arcpy.FeatureClassToFeatureClass_conversion(
        centerline,
        r'E:\SAVI810\Final_Project\Data_Test\shape\corridor',
        "{}_test".format(corridor.replace(" ", "_")),
        sql_statement,
    )


export_the_corridor(corridor, mn_borocode)

# add the corridor to the map and name the file
corridor_location = arcpy.mapping.Layer(r"E:\SAVI810\Final_Project\Data_Test\shape\corridor\{}_test.shp"
                                        .format(corridor.replace(" ", "_")))
arcpy.mapping.AddLayer(df, corridor_location, "BOTTOM")
full_corridor = arcpy.mapping.ListLayers(mxd)[1]

arcpy.SelectLayerByAttribute_management(centerline, "CLEAR_SELECTION")



# create a 40 foot buffer around the corridor
buffer_path = r'E:\SAVI810\Final_Project\Data_Test\shape\corridor\{}_buffer_test'.format(corridor.replace(" ", "_"))
buffer_distance = '40 feet'

def buffer_the_corridor(in_file, out_file, buffer_distance):
    arcpy.Buffer_analysis(in_file, out_file, buffer_distance)


buffer_the_corridor(full_corridor, buffer_path,'40 feet')

# add the buffered corridor to the map
full_corridor_buffered_location = arcpy.mapping.Layer(
    r'E:\SAVI810\Final_Project\Data_Test\shape\corridor\{}_buffer_test.shp'.format(corridor.replace(" ", "_")))
arcpy.mapping.AddLayer(df, full_corridor_buffered_location, "BOTTOM")
full_corridor_buffered = arcpy.mapping.ListLayers(mxd)[2]

# clip the buffer by CDs or NTAs

# first, download and extract the relevant district file
# QUESTION: can i pull out the zipfile extraction parts below the if statements so that it would apply to both?
def download_the_districts(district_type):
    if district_type == 'CD':
        download_file_from_web(
            'https://data.cityofnewyork.us/api/geospatial/yfnk-k7r4?method=export&format=Original',
            r'E:\SAVI810\Final_Project\Data_Test\shape\district\{}shp.zip'.format(district_type)
        )
        zf_cd = zipfile.ZipFile(r'E:\SAVI810\Final_Project\Data_Test\shape\district\{}shp.zip'.format(district_type))
        zf_cd.extractall(r'E:\SAVI810\Final_Project\Data_Test\shape\district')
    else:
        download_file_from_web(
            'https://data.cityofnewyork.us/api/geospatial/cpf4-rkhq?method=export&format=Original',
            r'E:\SAVI810\Final_Project\Data_Test\shape\district\{}shp.zip'.format(district_type)
        )
        zf_nta = zipfile.ZipFile(r'E:\SAVI810\Final_Project\Data_Test\shape\district\{}shp.zip'.format(district_type))
        zf_nta.extractall(r'E:\SAVI810\Final_Project\Data_Test\shape\district')


chosen_district = 'CD'

download_the_districts(chosen_district)


# add the master district file to the map
# QUESTION: can I add a wild card in the nycd_18c statement so that this function
# would work even if you download a later version of the nycd file
def set_chosen_district_location(in_district):
    if in_district == 'CD':
        global chosen_district_location
        chosen_district_location = arcpy.mapping.Layer(
            r'E:\SAVI810\Final_Project\Data_Test\shape\district\nycd_18c\nycd.shp'.format(chosen_district))
    else:
        chosen_district_location = arcpy.mapping.Layer(
            r'E:\SAVI810\Final_Project\Data_Test\shape\district\nynta_18c\nynta.shp'.format(chosen_district))


set_chosen_district_location(chosen_district)
arcpy.mapping.AddLayer(df, chosen_district_location, "BOTTOM")
master_district = arcpy.mapping.ListLayers(mxd)[3]


# extract each community district of interest
district_numbers = (112, 109, 107)

def extract_districts(in_districts):
    for i in in_districts:
        sql_statement = ''' "BoroCD"= {0} '''.format(i)
        arcpy.FeatureClassToFeatureClass_conversion(
            master_district,
            r'E:\SAVI810\Final_Project\Data_Test\shape\district',
            '{0}_{1}'.format('chosen_district', i),
            sql_statement
        )


extract_districts(district_numbers)


# clip the corridor buffer to the relevant CDs or NTAs
arcpy.env.workspace = r'E:\SAVI810\Final_Project\Data_Test\shape\district'

def clip_the_buffer(in_list, in_buffer):
    segment_list = []
    for i in in_list:
        arcpy.Clip_analysis(
            in_buffer,
            r'E:\SAVI810\Final_Project\Data_Test\shape\district\chosen_district_{}.shp'.format(i),
            r'E:\SAVI810\Final_Project\Data_Test\shape\corridor\segment_{0}_{1}.shp'.format(chosen_district, i),
        )
        segment_list.append(
            r'E:\SAVI810\Final_Project\Data_Test\shape\corridor\segment_{0}_{1}.shp'.format(chosen_district, i))
    return segment_list


segment_list = clip_the_buffer(district_numbers, full_corridor_buffered)

# tree stuff starts
download_file_from_web("https://data.cityofnewyork.us/api/views/k5ta-2trh/rows.csv?accessType=DOWNLOAD",
                       r'E:\SAVI810\Final_Project\Data_Test\table\treepoints.csv')



# separate long and lat in treepoints to their own columns
trees = r'E:\SAVI810\Final_Project\Data_Test\table\treepoints.csv'
df_trees = pd.read_csv(trees)
df_trees['longitude'] = df_trees['Location'].str.split('(').str[1].str.split(' ').str[0].str.replace(',', '')
df_trees['latitude'] = df_trees['Location'].str.split(' ').str[1].str.replace(')', '')

# export the dataframe to a fresh csv to use in arc
out_trees = trees.replace('.csv', '_clean.csv')
df_trees.to_csv(out_trees, index=False)

# show treepoint data
# the projection isn't working correctly. I specified the spatial reference parameter in hopes that it would work
# but it does not
State_Plane = arcpy.SpatialReference(4456)
arcpy.MakeXYEventLayer_management(
    out_trees,
    'longitude',
    'latitude',
    "trees_layer",
    State_Plane
)

# copy the features to a layer
arcpy.CopyFeatures_management("trees_layer", r'E:\SAVI810\Final_Project\Data_Test\shape\treepoints.shp')

treepoints_location = arcpy.mapping.Layer(r'E:\SAVI810\Final_Project\Data_Test\shape\treepoints.shp')
arcpy.mapping.AddLayer(df, treepoints_location, "BOTTOM")
treepoints = arcpy.mapping.ListLayers(mxd)[4]

# select treepoints by location for each segment
def intersect_trees_and_segments(in_trees, selection_type, selection_list, district_numbers):
    list_of_treepoints_by_segment = []
    for i in (range(len(selection_list))):
        input_extent = selection_list[i]
        district_number = district_numbers[i]
        arcpy.SelectLayerByLocation_management(
            in_trees,
            selection_type,
            input_extent,
        )
        arcpy.CopyFeatures_management(
            in_trees,
            r'E:\SAVI810\Final_Project\Data_Test\shape\{0}_{1}_treepoints.shp'.format(chosen_district, district_number)
        )
        list_of_treepoints_by_segment.append(r'E:\SAVI810\Final_Project\Data_Test\shape\{0}_{1}_treepoints.shp'.format(chosen_district, district_number))
    return list_of_treepoints_by_segment


list_of_treepoints_by_segment = intersect_trees_and_segments(
    treepoints,
    'intersect',
    segment_list,
    district_numbers
)


