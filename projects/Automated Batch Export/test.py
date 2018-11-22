import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")
for bkmk in arcpy.mapping.ListBookmarks(mxd):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext

print bkmk