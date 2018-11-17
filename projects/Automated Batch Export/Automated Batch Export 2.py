import arcpy



mxd = arcpy.mapping.MapDocument("C:/Users/ashaiban/Desktop/Lesson 6/Untitled.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "")
bkmk = arcpy.mapping.ListBookmarks(mxd, "")
layers = arcpy.mapping.ListLayers(mxd, "")

print layers