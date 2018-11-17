import urllib
import pandas as pd
import arcpy
import zipfile

# downloading the necessary files from OpenData
def download_file_from_web(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.urlretrieve(url, file_name)

# uncomment this when done
# download_file_from_web("https://data.cityofnewyork.us/api/views/k5ta-2trh/rows.csv?accessType=DOWNLOAD",
#                        r'C:\Users\ksutton\Documents\Data\treepoints.csv')
# download_file_from_web("https://data.cityofnewyork.us/api/views/2v4z-66xt/files/64d8bbe5-3a34-4811-912d-7259c8679d57?filename=nyclion_18c.zip",
#                        r'C:\Users\ksutton\Documents\Data\LION.zip'

# extract the parks properties and LION zipfiles
# uncomment this when done
# zf = zipfile.ZipFile(r'C:\Users\ksutton\Documents\Data\LION.zip')
# zf.extractall(r'C:\Users\ksutton\Documents\Data')
#
# zf_parks_props = zipfile.ZipFile(r'C:\Users\ksutton\Documents\Data\ParksProperties.zip')
# zf_parks_props.extractall(r'C:\Users\ksutton\Documents\Data')

# separate long and lat in treepoints to their own columns
trees = r'C:\Users\ksutton\Documents\Data\treepoints.csv'
df = pd.read_csv(trees)
df['longitude'] = df['Location'].str.split('(').str[1].str.split(' ').str[0].str.replace(',', '')
df['latitude'] = df['Location'].str.split(' ').str[1].str.replace(')', '')
# export the dataframe to a fresh csv to use in arc
out_trees = trees.replace('.csv', '_clean.csv')
df.to_csv(out_trees, index=False)

# # make new arcmap
# need this to work!
# mxd_path = r'C:\Users\ksutton\Documents\GitHub\pratt-savi-810-2018-10\projects\KSutton_project\MXD\Tree_Corridor_Analysis'
# mxd = arcpy.mapping.MapDocument(mxd_path)

# show treepoint data
State_Plane = arcpy.SpatialReference(4456)
arcpy.MakeXYEventLayer_management(
    out_trees,
    'longitude',
    'latitude',
    'in_memory_xy_layer',
    State_Plane,
)

print('made in memory layer')

