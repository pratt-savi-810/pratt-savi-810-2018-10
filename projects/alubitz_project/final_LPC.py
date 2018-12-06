import arcpy
# mxd = arcpy.mapping.MapDocument(r'C:\Users\alubitz\Desktop\lpc_test.mxd')
from arcpy import env
import urllib
import zipfile
import os


def download_file_from_web(url, filename):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.urlretrieve(url, filename)


link_dict = {
        "boro_boundary": "http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip",
        "landmark_footprints": "https://data.cityofnewyork.us/api/geospatial/7mgd-s57w?method=export&format=Original",
        "ind_landmarks": "https://data.cityofnewyork.us/api/geospatial/ch5p-r223?method=export&format=Original",
    }

dest_dir = r'C:\Users\alubitz\Desktop\data'
data = os.listdir(r'C:\Users\alubitz\Desktop\data')  # from os import listdir to compile list of file names

for i in data:  # iterate through link dictionary
    zip = zipfile.ZipFile(r'C:\Users\alubitz\Desktop\data\{}'.format(i), 'r')
    zip.extractall(dest_dir)


mxd = arcpy.mapping.MapDocument("CURRENT")  # set up map document in ArcMap
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]  # set up data frame
nybb = arcpy.mapping.Layer(r'C:\Users\alubitz\Desktop\data\nybb')  # create new layer
arcpy.mapping.AddLayer(df, nybb, "BOTTOM")  # add the layer to the map at the bottom of the TOC in data frame 0

for fc in arcpy.ListFeatureClasses():
    arcpy.AddField_management(fc, "Time", "DOUBLE")

map_df = arcpy.mapping.ListDataFrames(mxd, " * ")[0]  # extract map_dataframe from the mxd object

with arcpy.da.SearchCursor(fc, "Time") as cursor:
    for row in cursor:
Time.subtract("DESDATE", "CALDATE", row[0])

# df.merge()

for field_value in list_of_field_values:
    arcpy.SelectLayerByAttribute_management(
        fc,
        "NEW_SELECTION",
        """ "{}" = '{}'' """.format(unique_fieldname, field_value),
    )


# arcpy.ExportToPNG
