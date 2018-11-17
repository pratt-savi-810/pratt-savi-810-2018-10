import arcpy
mxd = arcpy.mapping.MapDocument(r'C:\Users\alubitz\Desktop\lpc_test.mxd')

for fc in arcpy.ListFeatureClasses():
arcpy.AddField_management(fc, "Time", "DOUBLE")

map_df = arcpy.mapping.ListDataFrames(mxd, " * ")[0]  # extract map_dataframe from the mxd object

with arcpy.da.SearchCursor(fc, "Time") as cursor:
		for row in cursor:
			Time.subtract("DESDATE", "CALDATE", row[0])

# df.merge()

for field_value in list_of_field_values:
arcpy.SelectLayerByAttribute_management(
        fc,
        "NEW_SELECTION",
        """ "{}" = '{}'' """.format(unique_fieldname, field_value),
    )

arcpy.ExportToPNG

