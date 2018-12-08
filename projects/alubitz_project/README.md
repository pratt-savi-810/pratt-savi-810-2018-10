# Rate of Landmark Designation

## Project Description

This project uses NYC Landmarks Preservation Commission (LPC) data to calculate a new field that measures the time between landmark and historic district calendaring and their designation. This field is created in order to compare across neighborhoods as well as types of landmarks to identify potential trends in faster or slower designation. 
While this rate is likely contingent on several external factors, such as time of the year and the number of other actively calendared buildings, the rationale behind this project is to be able to search for a hypothesized correlation between faster designation times and higher land values.

This project also hopes to create a generic method of creating and calculating a new field for spatial analysis that can be transferable to similar projects.
Although this analysis can only consider designated landmarks, further study could include buildings calendared but not designated.

## Data Sources
LPC Designated Individual Landmarks (Point shapefile IND_Landmark_Points_10_26_18_revised), NYC Open Data Portal
<br>https://data.cityofnewyork.us/api/geospatial/ch5p-r223?method=export&format=Original

Individual Landmark and Historic District Building Footprints (Polygon shapefile LPC_IL_HD_Bld_DB_10_19_18), NYC Open Data Portal
<br>https://data.cityofnewyork.us/api/geospatial/7mgd-s57w?method=export&format=Original

Borough Boundaries Clipped to Shoreline (Polygon shapefile nybb), NYC Department of City Planning
<br>http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip

## Output
The output is a new polygon shapefile which contains rate of designation as a new field which can be symbolized for relative rates across NYC. For instance, this can be used for running statistics or symbolizing average rates by borough.

A recording of the code running can be viewed here: http://recordit.co/9xCiJrpXJQ

## Outline of Steps
####    1. Import dependencies


	import arcpy
	import urllib
	import zipfile
	import os
	
#### 	2. Define functions to download the three sources of data and store locally


	def download_file_from_web(url, file_name):
	
This will download the file from `url` and save it locally under `file_name`.


    def main():
        link_dict = {
            "boro_boundary": "http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip",
            "landmark_footprints": "https://data.cityofnewyork.us/api/geospatial/7mgd-s57w?method=export&format=Original",
            "ind_landmarks": "https://data.cityofnewyork.us/api/geospatial/ch5p-r223?method=export&format=Original",
        }

    download_location = r'C:\Users\...'

Then create and run `main` function which compiles a list of all file names.

    for key, url in link_dict.items():

        print('downloading {0} data, from url: {1}'.format(key, url))

        download_file_from_web(
            url,
            '{0}/{1}.zip'.format(download_location, key)
        )

    if __name__ == '__main__':
        main()
   
#### 3. Iterate through the list of all downloaded files in order to unzip

    dest_dir = r'C:\Users\Adam\Desktop\data'
    data = os.listdir(r'C:\Users\Adam\Desktop\data')

    for i in data:
        zip = zipfile.ZipFile(r'C:\Users\Adam\Desktop\data\{}'.format(i), 'r')
        zip.extractall(dest_dir)

#### 4. Set up ArcMap document

    mxd = arcpy.mapping.MapDocument("CURRENT")  
    df = arcpy.mapping.ListDataFrames(mxd, "*")[0]  # set up data frame from the mxd object
    
    # Create the three layers and set filenames as variables in Arcmap
    points = arcpy.mapping.Layer(r"C:\Users\Adam\Desktop\data\IND_Landmark_Points_10_26_18_revised.shp")  
    arcpy.mapping.AddLayer(df, points, "BOTTOM")

    bldgs = arcpy.mapping.Layer(r'C:\Users\Adam\Desktop\data\LPC_IL_HD_Bld_DB_10_19_18.shp')  # sets filenames as vars
    arcpy.mapping.AddLayer(df, bldgs, "BOTTOM")

    nybb = arcpy.mapping.Layer(r'C:\Users\Adam\Desktop\data\nybb_17c\nybb.shp')
    arcpy.mapping.AddLayer(df, nybb, "BOTTOM")

#### 5. Convert calendared and designated date field types from string to date

    arcpy.AddField_management(points, "cal", "DATE")
    arcpy.CalculateField_management(points, "cal", "[CALDATE]", "VB")
    arcpy.AddField_management(points, "des", "DATE")
    arcpy.CalculateField_management(points, "des", "[DESDATE]", "VB")

#### 6. Create and populate the new `rate` field with a value which represents, in days, the difference between designation date minus calendared date.

    arcpy.AddField_management(points, "rate", "LONG")
    arcpy.CalculateField_management(points, "rate", "[des] - [cal]", "VB")

#### 7. Conduct a spatial join between the `points` shapefile with the polygon-based `bldgs` shapefile as the destination.

	arcpy.SpatialJoin_analysis("bldgs", "points", "in_memory/lpc_rate")

This final shapefile is now ready to use for spatial analysis, including symbolizing where higher and lower rates of designation exist across the city.
