# Project Description 

I created a geodatabase that stores the data for all our groundwater sampling events for a specific client. The geodatabase was originally created using ArcCatalog, published as a Web Servvice to ArcGIS Online, and accessed in the field via Collector for ArcGIS. 

The data collected from these groundwater sampling events has to be later downloaded and sent to a new geodatabase as each sampling event will get its own. The two data tables associated with the "well" point feature class have to be joined together and later joined to the well points to create one unified shapefile and csv with no spared information.

# Project Outline

Create a new file geodatabase

Make feature layer/Add Attribute Indexes

Join table1 to table2

Export the new_joined_table

Join the new_joined_table to the "well" feature class

Export the new_wells_table_join as a new feature class

