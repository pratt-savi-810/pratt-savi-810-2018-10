# import modules
import arcpy




# EXPORT 1

# set the  mxd
mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")
# import layers
layers = arcpy.mapping.ListLayers(mxd, "*")
# import bookmarks and define desired bookmark
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD103"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        # input the desired layers to be toggled on
        if item.name == 'Housing':
            item.visible = True
        if item.name == 'Year Built':
            item.visible = True
    # overwrite exports
    arcpy.mapping.overwriteOutput = True
    # output and export destination and characteristics
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Desktop\TEST1.png".format(bkmk.name), resolution=50)

del mxd


# EXPORT 2

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD103"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Housing':
            item.visible = True
        if item.name == 'Year Built':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Desktop\TEST1.png".format(bkmk.name), resolution=50)

del mxd


# EXPORT 3

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD103"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Housing':
            item.visible = True
        if item.name == 'Year Built':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Desktop\TEST1.png".format(bkmk.name), resolution=50)

del mxd