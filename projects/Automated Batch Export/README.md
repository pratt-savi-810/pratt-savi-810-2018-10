# Automated Batch Export

**Project Description**

Many times when I am tasked with mapping projects, a lot of time and effort is spent toggling layers and bookmarks to export individually, only to then wait for the export to finish to repeat the process, over and over again. The goal of this project is to automate this process as much as possible.

**How to Use**

1. FIll in all the desired bookmarks, layers, and export
2. Run
3. Voila
	
Python Dependencies:
- arcpy

Current Limitations:
I am having difficulty clearing the layers I enabled previously for the next export. I tried using the <i>else</i> function, but I kept recieving errors. I tried all the indentations I thought possible, and ordered them in different ways to no avail.

My workaround is to use the <i>del mxd</i> function and just re-input the mxd after each export. I imagine this will slow things down, but it works.
	

**Psuedocode**
```
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
```


