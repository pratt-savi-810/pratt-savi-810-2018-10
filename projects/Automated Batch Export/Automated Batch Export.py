import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")

for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD103"): #Put in the Bookmark Name
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Year Built': #Put in the desired layers
            item.visible = True
    arcpy.mapping.ExportToPDF(mxd, r"C:\Users\blazer\Desktop\test3.pdf".format(bkmk.name)) #Export Destination