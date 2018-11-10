mxd = arcpy.mapping.MapDocument('CURRENT')
df = arcpy.mapping.ListDataFrames(mxd, "Layers") [0]
lyr = arcpy.mapping.ListLayers(mxd, "Siteslyr", df)[0]
arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", ' "gid" = 2739 ')
df.zoomToSelectedFeatures()

arcpy.RefreshActiveView()
