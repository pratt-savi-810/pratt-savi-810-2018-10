import arcpy
#Create geodatabase

arcpy.env.workspace = "C:/XSAVI/github/pratt-savi-810-2018-10/projects/rowleys_project/ClassProject"
out_folder_path = "C:/XSAVI/github/pratt-savi-810-2018-10/projects/rowleys_project/ClassProject"
out_name = "BKRS.gdb"
arcpy.CreateFileGDB_management(out_folder_path, out_name)


#Add table and shapefile to geodatabase

arcpy.env.workspace = "C:/XSAVI/github/pratt-savi-810-2018-10/projects/rowleys_project/ClassProject"

inFeatures = ['BKMapPLUTO.shp']
outLocation = "C:/XSAVI/github/pratt-savi-810-2018-10/projects/rowleys_project/ClassProject/BKRS.gdb"
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)

tables = arcpy.ListTables()
print("Importingtablestogdb:" + outLocation)
arcpy.TableToGeodatabase_conversion(tables, outLocation)

#Jointabletoshapefile

arcpy.env.workspace="C:/XSAVI/github/pratt-savi-810-2018-10/projects/rowleys_project/ClassProject/BKRS.gdb"

shpFeatures = "BKMapPLUTO"
joinField = "BBL"
joinTable = "T2016BKBldgsGeo"
fieldList = "bbl"
arcpy.JoinField_management(shpFeatures, joinField, joinTable, fieldList)
