# Rate of Landmark Designation

# project description

This project uses NYC Landmarks Preservation Commission (LPC) data to calculate a new field that measures the time between landmark and historic district calendaring and their designation. This is done in order to compare across neighborhoods as well as types of landmarks and identify potential trends in faster or slower designation. This rate is likely contingent on several external factors as well, such as time of the year or number of other actively calendared buildings, which is why the rate is also compared to how recently each designation occurred. The aim of this project is to create a generic method of creating and calculating a new field for spatial analysis that can be transferable to similar projects.

# data inputs
IND_Landmark_Points_10_26_18_revised (LPC shapefiles from nyc open data portal)

LPC_IL_HD_Bld_DB_10_19_18 (landmark and historic district building footprints)

nybb  (borough boundaries clipped to shoreline)

# output
The output is a new polygon shapefile which contains rate of designation as a new field so it can be symbolized for relative rates across NYC. This can be symbolized by plotting statistics and showing average rates by borough.

# steps to accomplish this
1) Import arcpy and set up workspace

	import arcpy
	mxd = arcpy.mapping.MapDocument(mxd_filepath)
	def convertdatetimestring # define function

2) Start a loop and create a new double numeric field in IND_Landmark_Points_10_26_18_revised

	for fc in arcpy.ListFeatureClasses():
	arcpy.AddField_management(fc, "Time", "DOUBLE")

3) Use a cursor-based approach to populate the new field with a value which represents the difference between designation date minus calendared date.

	map_df = arcpy.mapping.ListDataFrames(mxd, " * ")[0] # extract map_dataframe from the mxd object

	with arcpy.da.SearchCursor(fc, "Time") as cursor:
		for row in cursor:
			Time.subtract("DESDATE", "CALDATE", row[0])

4) Merge data in points shapefile with the polygon shapefile 'LPC_IL_HD_Bld_DB_10_19_18'

	df.merge

5) ExportToPNG

	for field_value in list_of_field_values:
	#select feature by attribute from layer - attribute being boro name
	arcpy.SelectLayerByAttribute_management(
		fc,
		"NEW_SELECTION",
		""" "{}" = '{}'' """.format(unique_fieldname, field_value),
		)

##	map_df.zoomToSelectedFeatures()

##	arcpy.clearselectedfeature

	arcpy.ExportToPNG
