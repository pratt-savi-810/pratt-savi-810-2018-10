

def export_map_for_feature_in_fc(fc, mxd_file, unique_fieldname, output_png_dir):
	# declare mxd as current (instead of filepath)
	mxd = arcpy.mapping.MapDocument(mxd_file)

	# get map dataframe from mxd object
	map_df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

	# make empty list
	list_of_field_values = []

	with arcpy.da.SearchCursor(fc, unique_fieldname) as cursor:
		for row in cursor:
			list_of_field_values.append(row[0])

	for field_value in list_of_field_values:

		# select feature by attribute from table - attribute being boro_name
		arcpy.SelectLayerByAttribute_management(
			fc,
			"NEW_SELECTION",
			""" "{}" = '{}' """.format(unique_fieldname, field_value),
		)

		map_df.zoomToSelectedFeatures()

		arcpy.SelectLayerByAttribute_management(fc, "CLEAR_SELECTION")

		arcpy.mapping.ExportToPNG(mxd, '{}_{}.png'.format(output_png_dir, field_value))

