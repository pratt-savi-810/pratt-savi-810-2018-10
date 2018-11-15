import arcpy

featureclass = arcpy.ListFields("C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project\_data\BKMapPLUTO.shp")
field_names = [f.name for f in arcpy.ListFields(featureclass)]

print(field_names)
