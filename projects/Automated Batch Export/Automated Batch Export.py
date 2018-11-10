import arcpy

mxd = arcpy.mapping.MapDocument("C:/Users/ashaiban/Desktop/Lesson 6/Untitled.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd, "Buffer", df)[0]
arcpy.RefreshActiveView()
arcpy.mapping.overwriteExport = True
arcpy.mapping.ExportToPNG(mxd, r"C:/Users/ashaiban/Desktop/Lesson 6/test/test321.png", df)

del mxd
