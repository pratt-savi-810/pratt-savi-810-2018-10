import arcpy



mxd = arcpy.mapping.MapDocument("C:/Users/ashaiban/Desktop/Lesson 6/Untitled.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "*")
bkmk = arcpy.mapping.ListBookmarks(mxd, "*")
layers = arcpy.mapping.ListLayers(mxd, "*")

#print lyr

for item in layers:
    print(item)
    # print(item.isGroupLayer)
    item.visible = False
    if item.name == "IND":   #first layer
        item.visible = True
    if item.name == "LPC":   #second layer
        item.visible = True
    if item.name == 'Group One':   # third layer
        item.visible = True
    if item.name == 'nybb':  # third layer
        item.visible = True

arcpy.RefreshActiveView()
arcpy.mapping.overwriteExport = True
arcpy.mapping.ExportToPNG(mxd, r"C:/Users/ashaiban/Desktop/Lesson 6/test/test1.png")



'''
layers = ["IND"]

for lyr in layers:
    if lyr.name in layers:
        lyr.visible = True


arcpy.RefreshActiveView()
arcpy.mapping.overwriteExport = True
arcpy.mapping.ExportToPNG(mxd, r"C:/Users/ashaiban/Desktop/Lesson 6/test/test1.png")

print lyr

del mxd
'''