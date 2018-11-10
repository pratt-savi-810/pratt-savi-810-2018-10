import arcpy

projFolder = r"C:/Users/ashaiban/Desktop/Lesson 6"

mxd = arcpy.mapping.MapDocument(r"C:/Users/ashaiban/Desktop/Lesson 6/Untitled.mxd".format(projFolder))
df = arcpy.mapping.ListDataFrames(mxd, '')[0]

PNGPath = r"C:/Users/ashaiban/Desktop/Lesson 6/test"

layers = ['nybb','buffer_400','LPC_IL_HD_Bld_DB_10_19_18'] # List of your output layers

lyrlist = arcpy.mapping.ListLayers(mxd, '', df)

for layer in layers:
    layerOn = "*" # When required layer is turned on this will be the layer name to output
    for lyr in lyrlist:
        lyr.visible = False
        #if lyr.name in layers and lyr.name <> layer:
        #   lyr.visible = False
        if lyr.name == "nybb":
            lyr.visible = True
        if lyr.name == "buffer_400":
            lyr.visible = True
        if lyr.name == layer:
            lyr.visible = True
            layerOn = lyr.name
    if layerOn:
        arcpy.mapping.ExportToPNG(mxd,r"C:/Users/ashaiban/Desktop/Lesson 6/test/%s.png" % lyr.name)