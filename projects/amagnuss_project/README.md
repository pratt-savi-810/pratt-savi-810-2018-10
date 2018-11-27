# CIAT Global Coffee Projects

**Background**

The production of Arabica coffee is under threat from changes in the climate. With radical shifts in weather predicted in coffee growing regions around the world, the timing is apt to ascertain which coffee lands and producers are the most at risk for losing viable land for Arabica production, to implement climate change adaptation/mitigation interventions. 

The International Center for Tropical Agriculture (CIAT), a CGIAR research center, has been modeling the effects of climate change in the coffee producing regions of the world. In September 2018, they published a paper regarding the impact of climate change on coffee production in Latin America. All published data produced through the research of CGIAR consortia is made publicly available on the Harvard Dataverse website. 

**Project Description**

The purpose of this project is to create tools to handle dynamic dataframes to plot various coffee locations and practice projecting muliple vector and raster files at once. 

This project takes two datasets made available from CIAT via the Harvard Dataverse and uses them in Python script. The first, is a csv of 2,194 coffee projects/farm locations (including lat/long), and the second is a zip file of raster layers for six countries in Central America (CAM). The first step in the project was to establish a general function that would also for the easy manipulation of csv, setting a dataframe that would export to a csv based on the column (field name) and the desired list of coffee places under those columns. 

Then I wanted to automate the plotting of the xy data for the six countries in Central America which are included in the raster dataset through arcpy. After this step, there are six layers created. These are then projected into North American Alber Equal Area. This projection was chosen because ultimately, I would like to examine the change in coffee suitability by doing analyses on the area potenially 'lost' to changes in climate. 

**How to Use**

Coffee Projects Data: Located in GitHub project (https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/coffee_project/projects/amagnuss_project/CoffeePoints_2.csv). Download this data and save it locally. Copy the path name for this file - this will be your "input_table".

json_config file: https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/coffee_project/projects/amagnuss_project/coffee_cfg.json. Save in same directory as data above. You will use this path to define "coffee_cfg" later in the script. 

	
Python Dependencies:
IMPORT
- arcpy
- pandas as pd
- json
	
VENV
C:\Python27\ArcGIS10.6\python.exe
	
	


**Psuedocode**
```
download data from CIAT through Harvard dataverse
	raster data: https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/9QUGUR/GATGQJ&version=1.0
	coffee locations (csv): https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/29634#

unzip project files 

set local variables in python project
	in_put table
	list_of_coffee_places
	field_names

create function to set the dataframe for the csv based on values in one of three columns (field_name)
	'Country', 'ADM1_NAME', 'ADM2_NAME'

export dataframe to csv
	read csv
	loop through unique attributes (list_of_coffee_places) in those columns to filter for desired dataframe
	name each csv based on those unique attributes

create event layer from xy from csvs just saved
	loop through all the csvs just created to ploy xy points
	save new shapefiles
	save new layers as well

project data in NA Albers Equal Area
	project all news vector layers into AEA
```


