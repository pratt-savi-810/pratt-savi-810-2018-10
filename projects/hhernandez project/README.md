#create a map of 10 bridges by joining my bridge data table with a NYC CSCL shapefile



#define function
#declared mxd as current (intestd of mxd filepath)
#got my map_dataframe from the mxd objects
#make empty

#select multiple bridge features

arcpy.SelectLayerByAttribute_management("bridge_Vol", "NEW_SELECTION", """ "bridge" = 'Brooklyn Bridge' """)

#zoom to selected features

mxd = arcpy.mapping.MapDocument('current')
map_df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
map_df.zoomToSelectedFeatures()

#export multiple maps based on a group of selected features

arcpy.mapping.ExportToPNG(mxd, r'C:\XXX')

