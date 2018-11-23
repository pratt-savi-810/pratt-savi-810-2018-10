#import modules
import arcpy

# set the mxd
mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")

#import layers
layers = arcpy.mapping.ListLayers(mxd, "*")


#the following would be for one export, copy for as many exports as needed
#Export 1
# input the desired bookmark name
for bkmk in arcpy.mapping.ListBookmarks(mxd, "<BOOKMARK>"): #Bookmark
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        # input the desired layers to be on
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True

    #export
    arcpy.mapping.ExportToPDF(mxd, r"<DESTINATION>".format(bkmk.name)) #Export Destination


#Export 2
for bkmk in arcpy.mapping.ListBookmarks(mxd, "<BOOKMARK>"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True

    arcpy.mapping.ExportToPDF(mxd, r"<DESTINATION>".format(bkmk.name))


#Export 3
for bkmk in arcpy.mapping.ListBookmarks(mxd, "<BOOKMARK>"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True

    arcpy.mapping.ExportToPDF(mxd, r"<DESTINATION>".format(bkmk.name))


#Export 4
for bkmk in arcpy.mapping.ListBookmarks(mxd, "<BOOKMARK>"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True
        if item.name == '<LAYER>':
            item.visible = True

    arcpy.mapping.ExportToPDF(mxd, r"<DESTINATION>".format(bkmk.name))
