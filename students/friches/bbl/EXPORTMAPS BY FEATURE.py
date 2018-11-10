def export_maps_for_feature_in_fc(fc,mxd_file,unique_fieldname)

mxd = arcpy.mapping.Mapdocument(mxd_file)

map_df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

list_of_field_values = []
with arcpy.da.searchCursor(fc,unique_fieldname) as cursor:
	for row in cursor:
		list_of_field_values.append(row[0])

for field_value in list_of_field_values

	arcpy.SelectLayerByAttribute_managment(
		fc."NEW_SELECTION",
		""" "{}" = '{}'""".FORMAT (unique_fieldname, field_value),
		)

		map_df.zoomToSelectedFeatures()

		arcpy.SelectLayerByAttribute_managment(fc, "CLEAR_SELECTION")

		arcpy.mapping.ExportToPNG(mxd,'()_().png'.format(output_png_dir,field_value))