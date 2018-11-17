import pandas as pd
import arcpy

in_csv = 'C:/Users\Hector Hernandez/Documents/GitHub/pratt-savi-810-2018-10/students/hhernandez2783/Test/brg.csv'

df = pd.read_csv(in_csv)

out_csv = in_csv

# project xy coordinates
arcpy.MakeXYEventLayer_management(
     out_csv,
     'Brg_Lng',
     'Brg_Lat',
     'in_memory_xy_layer',
 )

# create a shapefile
arcpy.FeatureClassToFeatureClass_conversion(
     'in_memory_xy_layer',
     'C:/Users\Hector Hernandez/Documents/GitHub/pratt-savi-810-2018-10/students/hhernandez2783/Test',
     'brg.shp'
)

# loading shapefile in map document
# get the map document
mxd = arcpy.mapping.MapDocument(r"C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\Test\ld.mxd")
# Set the workspace
arcpy.env.workspace = r"C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\Test"
# get the data frame
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]
# create a new layer
newlayer = arcpy.mapping.Layer(r"C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\Test\brg.shp")
# add the layer to the map at the bottom of the TOC in data frame 0
arcpy.mapping.AddLayer(df, newlayer,"AUTO_ARRANGE")
# save the mxd file
mxd.save()


# adding labeling
layer = arcpy.mapping.ListLayers(mxd, "brg")[0] #Indexing list for 1st layer
if layer.supports("LABELCLASSES"):
    for lblclass in layer.labelClasses:
        lblclass.showClassLabels = True
layer.showLabels = True
arcpy.RefreshActiveView()
mxd.save()

# select features & zoom
nycbrg = arcpy.mapping.ListLayers(mxd)[0]
arcpy.SelectLayerByAttribute_management(nycbrg, "NEW_SELECTION", """ "brg" = 'Brooklyn Bridge' """)
df.zoomToSelectedFeatures()
mxd.save()

# export map
arcpy.mapping.ExportToPNG(mxd, r'C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\Test\expmap1.png')