# Automated Batch Export

**Project Description**

Many times when I am tasked with mapping projects, a lot of time and effort is spent toggling layers and bookmarks to export individually, only to then wait for the export to finish to repeat the process, over and over again. The goal of this project is to automate this process as much as possible.

**How to Use**

1. FIll in all the desired bookmarks, layers, and export
2. Run
3. Voila
	
**Python Dependencies**
-arcpy

**Current Limitations**
I am having difficulty clearing the layers I enabled previously for the next export. I tried using the <i>else:</i> function, but I kept recieving errors. I tried all the indentations I thought possible, and ordered them in different ways to no avail.

My workaround is to use the <i>del mxd</i> function and just re-input the mxd after each export. I imagine this will slow things down, but it works.

**Specific Project Examples**
At the moment, I am working on a project that studies Public Spending and it's relationship to equity within Community Districts, one in each borough.

We've identified a series of variables and topics that could potentially be interesting in this study, and I am tasked with mapping and visualizing them.

Some of them include:
    Community Facilities
        Parks and Open Spaces
        Schools
        Public Library
        LinkNYC and Public WiFi
    Transportation
        Bicycle
        Subway
        Bus
        Ferry Routes
    Housing
        Building by Year Built
        Inclusionary Housing Area
        421-a Tax Lots
        NYCHA Properties

The challenge is the continuous toggling of layers and changing extents to the different community districts. This process would usually be painstakingly long and cumberson. The automation would allow me to set up the scene, and just run.
	

**Psuedocode for copy**
```
# import modules
import arcpy

# EXPORT 1
# set the  mxd
mxd = arcpy.mapping.MapDocument(r"DESTINATION TO MXD")
# import layers
layers = arcpy.mapping.ListLayers(mxd, "*")
# import bookmarks and define desired bookmark
for bkmk in arcpy.mapping.ListBookmarks(mxd, "BOOKMARK 1"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        # input the desired layers to be toggled on
        if item.name == 'LAYER 1':
            item.visible = True
        if item.name == 'LAYER 2':
            item.visible = True
    # overwrite exports
    arcpy.mapping.overwriteOutput = True
    # output and export destination and characteristics
    arcpy.mapping.ExportToPNG(mxd, r"EXPORT DESTINATION".format(bkmk.name))
del mxd


# EXPORT 2
mxd = arcpy.mapping.MapDocument(r"DESTINATION TO MXD")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "BOOKMARK 1"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'LAYER 3':
            item.visible = True
        if item.name == 'LAYER 4':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"EXPORT DESTINATION".format(bkmk.name))
del mxd


# EXPORT 3
mxd = arcpy.mapping.MapDocument(r"DESTINATION TO MXD")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "BOOKMARK 2"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'LAYER 1':
            item.visible = True
        if item.name == 'LAYER 2':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"EXPORT DESTINATION".format(bkmk.name))
del mxd
```



**Psuedocode for example**
```
import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\AIA\GIS\AIA.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD103"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Transportation':
            item.visible = True
        if item.name == 'Bus':
            item.visible = True
        if item.name == 'Bus Routes SBS':
            item.visible = True
        if item.name == 'Bus Routes':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Documents\Desktop\AIA\Exports\11 24 18\Bus CD103".format(bkmk.name),resolution=300)
del mxd


mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\AIA\GIS\AIA.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD201"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Transportation':
            item.visible = True
        if item.name == 'Bus':
            item.visible = True
        if item.name == 'Bus Routes SBS':
            item.visible = True
        if item.name == 'Bus Routes':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Documents\Desktop\AIA\Exports\11 24 18\Bus CD201".format(bkmk.name),resolution=300)
del mxd

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\AIA\GIS\AIA.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD304"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Transportation':
            item.visible = True
        if item.name == 'Bus':
            item.visible = True
        if item.name == 'Bus Routes SBS':
            item.visible = True
        if item.name == 'Bus Routes':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Documents\Desktop\AIA\Exports\11 24 18\Bus CD304".format(bkmk.name),resolution=300)
del mxd

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\AIA\GIS\AIA.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD404"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Transportation':
            item.visible = True
        if item.name == 'Bus':
            item.visible = True
        if item.name == 'Bus Routes SBS':
            item.visible = True
        if item.name == 'Bus Routes':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Documents\Desktop\AIA\Exports\11 24 18\Bus CD404".format(bkmk.name),resolution=300)
del mxd

mxd = arcpy.mapping.MapDocument(r"C:\Users\blazer\Documents\Desktop\AIA\GIS\AIA.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD501"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Transportation':
            item.visible = True
        if item.name == 'Bus':
            item.visible = True
        if item.name == 'Bus Routes SBS':
            item.visible = True
        if item.name == 'Bus Routes':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\blazer\Documents\Desktop\AIA\Exports\11 24 18\Bus CD501".format(bkmk.name),resolution=300)
del mxd
```
