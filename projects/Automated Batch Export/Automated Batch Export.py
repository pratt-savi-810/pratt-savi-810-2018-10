import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "*")
bkmk = arcpy.mapping.ListBookmarks(mxd, "*")
layers = arcpy.mapping.ListLayers(mxd, "*")


#list and apply bookmarks extents
for bkmks in bkmk:
    ext = bkmks.extent


#list and toggle layers
for item in layers:
    print(item)
    if item.name == 'Overview':
        item.visible = True
    if item.name == 'Housing':
        item.visible = True
    if item.name == 'Year Built':
        item.visible = True

#refresh
arcpy.RefreshActiveView()

#overwrite export
arcpy.mapping.overwriteExport = True

#define export
arcpy.mapping.ExportToPNG(mxd, r"C:/Users/blazer/Desktop/test2.png", resolution=300)

del mxd