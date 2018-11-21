### Python Dependencies
	pip install pandas
	pip install glob
	pip install csv
	pip install numpy 
	pip install arcpy
	arcpy.CheckOutExtension("Spatial")
	
### Project Description 

I created a geodatabase that stores the data for all our groundwater sampling events for a specific client. The geodatabase was originally created using ArcCatalog, published as a Web Servvice to ArcGIS Online, and accessed in the field via Collector for ArcGIS. 

The data collected from these groundwater sampling events has to be later downloaded and sent to a new geodatabase as each sampling event will get its own. The two data tables associated with the "well" point feature class have to be joined together (the purge chemistry and the sampling information tables) and later joined to the well csv file (Step 1 - 3 CSVs merged to 1 - this is used as a reference and not included in the continuing steps).

Next, I have to download the lab data that was provided to us as three CSVs (Step 2 - Merege Lab Data CSVs). Then, I link the original "well" CSV with the combined lab data (Step 3). Note: I do not need to use the combined CSVs aquired from Step 1. Once the well CSV is merged with the Lab Data based on the common identifier, I need to pick out the parameters that exhibit exceedances as according to the state regulations (Step 4). 
I would like to pick out all exceeding well locations and associated data that specifically exceeds the "Benzene" regulations, convert the  features to a shapefile, and save to the geodatabase (Step 5). Finially, I would like to interpolate as IDW and show on ArcMap (Step 6).

### Project Outline

Join Purge Chemistry and Sampling Information

  call locations
  allow pandas to read
  join pc to si as a df
  convert to csv
  
  call on new output csv
  allow pandas to read
  join output to wells as a df
  convert to csv
  
 Join Lab Data CSVs together
 
  read all csv files in a folder
  for every csv file in the folder:
    open file and set the delimiter
   
   save the header from one of the csv files
    for filename in csv:
      open file
        keep header
 
 Join Lab Results CSV and Wells (joined) CSV....(HALP)
 
 
 
 Convert CSV to Shapefile Using Lat/Long
 
  Arcpy
  
  MakeXYMakeFeatureEvent
  CopyFeature
 
  
  
  
  

