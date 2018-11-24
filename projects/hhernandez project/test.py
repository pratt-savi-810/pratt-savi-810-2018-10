import pandas as pd
import arcpy

# Declare Variable for Location of csv File with Data
in_csv = 'C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\projects\hhernandez project/brg.csv'

# Project xy Coordinates
arcpy.MakeXYEventLayer_management(
     in_csv,
     'Brg_Lng',
     'Brg_Lat',
     'in_memory_xy_layer',
 )


# Declare Variable for Output Location of Shapefile & Location of Workspace for Loading Shapefile
out_shp_worksp = 'C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\projects\hhernandez project'
# Create a Shapefile
arcpy.FeatureClassToFeatureClass_conversion(
     'in_memory_xy_layer',
     out_shp_worksp,
     'brg.shp'
)


# Loading Shapefile in Map Document
# Declare Variable of Location of mxd File with Basemap for Shapefile Load
load_base = 'C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\projects\hhernandez project\ld2.mxd'
# get the map document
mxd = arcpy.mapping.MapDocument(load_base)
# Set the workspace
arcpy.env.workspace = out_shp_worksp
# get the data frame
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]
# Declare Variable of Location to Save Shapefile
save_ly = 'C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\projects\hhernandez project/brg.shp'
# create a new layer
newlayer = arcpy.mapping.Layer(save_ly)
# add the layer to the map at the bottom of the TOC in data frame 0
arcpy.mapping.AddLayer(df, newlayer,"AUTO_ARRANGE")
# save the mxd file
mxd.save()


# Adding Labeling
layer = arcpy.mapping.ListLayers(mxd, "brg")[0] #Indexing list for 1st layer
if layer.supports("LABELCLASSES"):
    for lblclass in layer.labelClasses:
        lblclass.showClassLabels = True
layer.showLabels = True
arcpy.RefreshActiveView()
mxd.save()


mp1 = " 'brg' = 'Brooklyn Bridge' OR 'brg' = 'Manhattan Bridge' OR 'brg' = 'Williamsburg Bridge' OR " \
      "\n'brg' = 'Ed Koch Queensboro Bridge' "
mp2 = " 'brg' = 'George Washington Bridge' OR 'brg' = 'Lincoln Tunnel' OR 'brg' = 'Holland Tunnel' "
mp3 = " 'brg' = 'Bayonne Bridge' OR 'brg' = 'Goethals Bridge' OR 'brg' = 'Outerbridge Crossing Bridge' "

MP_List = [mp1, mp2, mp3]
number = 1

for i in MP_List:
    output = 'example{}'.format(number)
    # Select Features & Zoom
    df = arcpy.mapping.ListLayers(mxd)[0]
    arcpy.SelectLayerByAttribute_management(df, "NEW_SELECTION", i)
    df.zoomToSelectedFeatures()
    # arcpy.SelectLayerByAttribute_management(nyc_brg, "CLEAR_SELECTION", i)
    mxd.save()

    # Export Map
    arcpy.mapping.ExportToPNG(
    mxd,
    '{}/{}.png'.format('C:\Users\Hector Hernandez\Documents\GitHub\pratt-savi-810-2018-10\projects\hhernandez project',
    output,
    df
    )
    )

    number += 1
    print (number)
