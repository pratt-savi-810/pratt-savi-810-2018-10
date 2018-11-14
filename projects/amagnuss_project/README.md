# CIAT Global Coffee Projects

**Background**

The production of Arabica coffee is under threat from changes in the climate. With radical shifts in weather predicted in coffee growing regions around the world, the timing is apt to ascertain which coffee lands and producers are the most at risk for losing viable land for Arabica production, to implement climate change adaptation/mitigation interventions. 

The International Center for Tropical Agriculture (CIAT), a CGIAR research center, has been modeling the effects of climate change in the coffee producing regions of the world. In September 2018, they published a paper regarding the impact of climate change on coffee production in Latin America. All published data produced through the research of CGIAR consortia is made publicly available on the Harvard Dataverse website. 

**Project Description**

The purpose of this project is to create tools to handle dynamic dataframes to plot various coffee locations and practice projecting muliple vector and raster files at once. 

This project takes two datasets made available from CIAT via the Harvard Dataverse and uses them in Python script. The first, is a csv of 2,194 coffee projects/farm locations (including lat/long), and the second is a zip file of raster layers for six countries in Central America (CAM). The first step in the project was to establish a general function that would also for the easy manipulation of csv, setting a dataframe that would export to a csv based on the column (field name) and the desired list of coffee places under those columns. 

Then I wanted to automate the plotting of the xy data for the six countries in Central America which are included in the raster dataset through arcpy. After this step, there are six layers created. These are then projected into North American Alber Equal Area. This projection was chosen because ultimately, I would like to examine the change in coffee suitability by doing analyses on the area potenially 'lost' to changes in climate. 
