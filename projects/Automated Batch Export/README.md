# Automated Batch Export

**Project Description**

Many times when I am tasked with mapping projects, a lot of time and effort is spent toggling layers and bookmarks to export individually, only to then wait for the export to finish to repeat the process, over and over again. The goal of this project is to automate this process.

**How to Use**

1. Adjust in the desired layer
2. Make sure any related layer groups are also filled in
3. Adjust export file destination

	
Python Dependencies:
IMPORT
- arcpy
	

**Psuedocode**
```
import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\Python\Python.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "*")
bkmk = arcpy.mapping.ListBookmarks(mxd, "*")
layers = arcpy.mapping.ListLayers(mxd, "*")

for item in layers:
    print(item)
    # print(item.isGroupLayer)
    if item.name == 'Overview':   #first layer
        item.visible = True
    if item.name == 'Housing':   #first layer
        item.visible = True
    if item.name == 'Year Built':  #second layer
        item.visible = True

arcpy.RefreshActiveView()
arcpy.mapping.overwriteExport = True
arcpy.mapping.ExportToPNG(mxd, r"C:/Users/blazer/Desktop/test2.png", resolution=300)

del mxd
```


