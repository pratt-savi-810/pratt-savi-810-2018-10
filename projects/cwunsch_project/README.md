# Project Description 

I created a geodatabase that stores the data for all our groundwater sampling events for a specific client. The geodatabase was originally created using ArcCatalog, published as a Web Servvice to ArcGIS Online, and accessed in the field via Collector for ArcGIS. 

The data collected from these groundwater sampling events has to be later downloaded and sent to a new geodatabase as each sampling event will get its own. The two data tables associated with the "well" point feature class have to be joined together and later joined to the well points to create one unified shapefile and csv with no spared information.

# Project Outline

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
 
  
  
  
  

