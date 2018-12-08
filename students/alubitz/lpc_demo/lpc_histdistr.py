def 
# declared mxd as current (instead of mxd filepath since this was in ArcMap desktop)
mxd = arcpy.mapping.MapDocument(mxd_file)

# extracted map_datafram from the mxd object
map_df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

# make empty


list_of_field_values = unique_fieldname.unique

with arcpy.da.SearchCursor(fc, unique_fieldname) as cursor:
	for row in cursor:
		list_of_field_values.append(row[0])

for field_value in list_of_field_values:
	#select feature by atribute from layer - attribute being boro name
	arcpy.SelectLayerByAttribute_management(
		fc,
		"NEW_SELECTION",
		""" "{}" = '{}'' """.format(unique_fieldname, field_value),
		)

	map_df.zoomToSelectedFeatures()

	arcpy.clearselectedfeature

	arcpy.ExportToPNG