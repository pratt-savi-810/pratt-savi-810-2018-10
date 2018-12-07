import arcpy
import urllib
import zipfile
import os

# not using the local mxd function unless I can't get the download multiple files to work
# mxd = arcpy.mapping.MapDocument(r'C:\Users\Adam\Desktop\lpc_test.mxd')


def download_file_from_web(url, filename):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.urlretrieve(url, filename)


def main():
    link_dict = {
        "boro_boundary": "http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip",
        "landmark_footprints": "https://data.cityofnewyork.us/api/geospatial/7mgd-s57w?method=export&format=Original",
        "ind_landmarks": "https://data.cityofnewyork.us/api/geospatial/ch5p-r223?method=export&format=Original",
    }

    download_location = r'C:\Users\Adam\Desktop\data'  # a 'data' folder must first be created on the desktop

    for key, url in link_dict.items():

        print('downloading {0} data, from url: {1}'.format(key, url))

        download_file_from_web(
            url,
            '{0}/{1}.zip'.format(download_location, key)
        )


if __name__ == '__main__':
    main()

dest_dir = r'C:\Users\Adam\Desktop\data'
data = os.listdir(r'C:\Users\Adam\Desktop\data')  # from os import listdir to compile list of file names

for i in data:  # iterate through link dictionary and extract each into same folder
    zip = zipfile.ZipFile(r'C:\Users\Adam\Desktop\data\{}'.format(i), 'r')
    zip.extractall(dest_dir)

# set up map document in ArcMap
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]  # set up data frame from the mxd object

# create layers and set filenames as vars
points = arcpy.mapping.Layer(r"C:\Users\Adam\Desktop\data\IND_Landmark_Points_10_26_18_revised.shp")
arcpy.mapping.AddLayer(df, points, "BOTTOM")  # add the layer to the map at the bottom of the TOC in data frame 0

bldgs = arcpy.mapping.Layer(r'C:\Users\Adam\Desktop\data\LPC_IL_HD_Bld_DB_10_19_18.shp')
arcpy.mapping.AddLayer(df, bldgs, "BOTTOM")

nybb = arcpy.mapping.Layer(r'C:\Users\Adam\Desktop\data\nybb_17c\nybb.shp')
arcpy.mapping.AddLayer(df, nybb, "BOTTOM")

# convert date field types from string to date
# for reference http://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-field.htm
arcpy.AddField_management(points, "cal", "DATE")
arcpy.CalculateField_management(points, "cal", "[CALDATE]", "VB")
arcpy.AddField_management(points, "des", "DATE")
arcpy.CalculateField_management(points, "des", "[DESDATE]", "VB")

# create and populate rate field
arcpy.AddField_management(points, "rate", "LONG")
arcpy.CalculateField_management(points, "rate", "[des] - [cal]", "VB")

# spatial join the new point-based data to the building polygons        
arcpy.SpatialJoin_analysis(bldgs, points, "in_memory/lpc_rate")
