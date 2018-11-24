import urllib
import pandas as pd
import arcpy

arcpy.env.overwriteOutput = 'True'

# downloading the necessary files from OpenData
def download_file_from_web(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.urlretrieve(url, file_name)

# tree stuff starts
# download_file_from_web("https://data.cityofnewyork.us/api/views/k5ta-2trh/rows.csv?accessType=DOWNLOAD",
#                        r'E:\SAVI810\Final_Project\Data_Test\table\treepoints.csv')

# ods_download = r'E:\SAVI810\Final_Project\Data_Test\table\treepoints.ods'
# csv_download = ods_download.replace('ods', 'csv')


# separate long and lat in treepoints to their own columns
trees = r'E:\SAVI810\Final_Project\Data_Test\table\treepoints.csv'
df_trees = pd.read_csv(trees)


df_trees['longitude'] = df_trees['Location'].str.split('(').str[1].str.split(' ').str[0] .str.replace(',', '')

print(df_trees.longitude.head)
df_trees['latitude'] = df_trees['Location'].str.split(' ').str[1].str.replace(')', '')
print(df_trees.latitude.head)
#
# # export the dataframe to a fresh csv to use in arc
# out_trees = trees.replace('.csv', '_clean.csv')
# df_trees.to_csv(out_trees, index=False)
#
# # show treepoint data
# State_Plane = arcpy.SpatialReference(4456)
# arcpy.MakeXYEventLayer_management(
#     out_trees,
#     'longitude',
#     'latitude',
#     "trees_layer",
#     State_Plane,
# )
#
# # copy the features to a layer
# arcpy.CopyFeatures_management("trees_layer", r'E:\SAVI810\Final_Project\Data_Test\shape\treepoints.shp')

