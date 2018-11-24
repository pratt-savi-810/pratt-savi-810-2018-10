import arcpy
import urllib
import zipfile
import os


def download_file_from_web(url, filename):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.urlretrieve(url, filename)
# mxd = arcpy.mapping.MapDocument(r'C:\Users\alubitz\Desktop\lpc_test.mxd')


link_dict = {
        "boro_boundary": "http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip",
        "landmark_footprints": "https://data.cityofnewyork.us/api/geospatial/7mgd-s57w?method=export&format=Original",
        "ind_landmarks": "https://data.cityofnewyork.us/api/geospatial/ch5p-r223?method=export&format=Original",
    }

dest_dir = r'C:\Users\Adam\Desktop\data'
data = os.listdir(r'C:\Users\Adam\Desktop\data')  # from os import listdir to compile list of file names

for i in data:  # iterate through link dictionary and extract each into same folder
    zip = zipfile.ZipFile(r'C:\Users\Adam\Desktop\data\{}'.format(i), 'r')
    zip.extractall(dest_dir)

# from arcpy import env
mxd = arcpy.mapping.MapDocument("CURRENT")  # set up map document in ArcMap
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]  # set up data frame from the mxd object

points = arcpy.mapping.Layer(r"C:\Users\Adam\Desktop\data\IND_Landmark_Points_10_26_18_revised.shp")  # creates layer
arcpy.mapping.AddLayer(df, points, "BOTTOM")  # add the layer to the map at the bottom of the TOC in data frame 0

bldgs = arcpy.mapping.Layer(r'C:\Users\Adam\Desktop\data\LPC_IL_HD_Bld_DB_10_19_18.shp')  # sets filenames as vars
arcpy.mapping.AddLayer(df, bldgs, "BOTTOM")

nybb = arcpy.mapping.Layer(r'C:\Users\Adam\Desktop\data\nybb_17c\nybb.shp')
arcpy.mapping.AddLayer(df, nybb, "BOTTOM")

for points in arcpy.ListFeatureClasses():
    arcpy.AddField_management(points, "rate", "DOUBLE", 6, "", "", "rate", "NULLABLE", "NON_REQUIRED")
    # for reference http://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-field.htm

# from arcpy.time import ParseDateTimeString

with arcpy.da.SearchCursor(points, "rate") as cursor:
    for row in cursor:
        arcpy.CalculateField_management(points,
                                        "rate",
                                        expression="(arcpy.time.ParseDateTimeString(!DESDATE!) - arcpy.time.ParseDateTimeString(!CALDATE!)).days",
                                        expression_type="PYTHON_9.3", code_block="")
        # http://desktop.arcgis.com/en/arcmap/10.3/manage-data/tables/calculate-field-examples.htm#ESRI_SECTION1_AFC203DD316B4543A729B413C3322F3C
        # https://community.esri.com/thread/159217

# spatial join the new point-based data to the building polygons        
arcpy.SpatialJoin_analysis(bldgs, points, "in_memory/bldgs_SpatialJoin")
