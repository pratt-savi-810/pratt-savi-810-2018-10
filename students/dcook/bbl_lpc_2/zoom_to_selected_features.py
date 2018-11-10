import arcpy

## arcpy.SelectLayerByAttribute_management('...',"New_selection",...)
## map_df.zoomToSelectedFeatures()
## arcpy.mapping.ExportToPNG(mxd, r'...png')

arcpy.SelectLayerByAttribute_management("nybb","NEW_SELECTION",""" "BoroName" = 'Manhattan' """)

mxd = arcpy.mapping.MapDocument('CURRENT')
map_df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
map_df.zoomToSelectedFeatures()
arcpy.mapping.ExportToPNG(mxd, r'C:\\Users\\dcook13\\Desktop\\test.png')

z = 'boror'
arcpy.mapping.ExportToPNG(mxd, r'C:\\Users\\dcook13\\Desktop\\test_{}.png'.format(z))
## test_boror.png

## example of what the project outline would be resulting in the above
## declared mxd as current (instead of mxd filepath)
## got my mapdataframe form the mxd object
## selected features by attribut from layer - attribute being boroname
## zoom to selected feature
## exported the png

## declared mxd as current (instead of mxd filepath)
## got my mapdataframe form the mxd object
## for boro_name in list_of_boronames:
    ## selected features by attribut from layer - attribute being boroname
    ## zoom to selected feature
    ## exported the png

def export_maps_each_feature(fc, mxd_file, unique_fieldname, output_png_dir):
    arcpy.RefreshActiveView()
    ## declared mxd as current (instead of mxd filepath)
    mxd = arcpy.mapping.MapDocument('CURRENT') ## or 'C://...map.mxd'
    ## got my mapdataframe form the mxd object
    map_df = arcpy.mapping.ListDataFrames(mxd,'*')[0]
    ## for boro_name in list_of_boronames:
    field_values_list = []
    with arcpy.da.SearchCursor(fc, unique_fieldname) as cursor:
        for row in cursor:
            field_values_list.append(row[0])

    for field_value in field_values_list:
        ## selected features by attribute from layer - attribute being boroname
        arcpy.SelectLayerByAttribute_management(
            fc,
            "NEW_SELECTION",
            """ "{}" = '{}' """.format(unique_fieldname, field_value),
        )
        ## zoom to selected feature
        map_df.zoomToSelectedFeatures()
        ## exported the png
        arcpy.SelectLayerByAttribute_management(fc,"CLEAR_SELECTION") ## just to get rid of outline
        arcpy.mapping.ExportToPNG(mxd, '{}_{}.png'.format(output_png_dir,field_value))


arcpy.RefreshActiveView()
export_maps_each_feature('nybb','CURRENT','BoroName',r'C:\\Users\\dcook13\\Desktop\\')



### building on dataframe code

def export_maps_each_feature(fc, mxd_file, unique_fieldname, output_png_dir):
    arcpy.RefreshActiveView()
    ## declared mxd as current (instead of mxd filepath)
    mxd = arcpy.mapping.MapDocument('CURRENT') ## or 'C://...map.mxd'
    ## got my mapdataframe form the mxd object
    map_df = arcpy.mapping.ListDataFrames(mxd,'*')[0]
    ## for boro_name in list_of_boronames:
    df = feature_class_to_dataframe(fc)
    field_values_list = df[unique_fieldname].unique()

    for field_value in field_values_list:
        ## selected features by attribute from layer - attribute being boroname
        arcpy.SelectLayerByAttribute_management(
            fc,
            "NEW_SELECTION",
            """ "{}" = '{}' """.format(unique_fieldname, field_value),
        )
        ## zoom to selected feature
        map_df.zoomToSelectedFeatures()
        ## exported the png
        arcpy.SelectLayerByAttribute_management(fc,"CLEAR_SELECTION") ## just to get rid of outline
        arcpy.mapping.ExportToPNG(mxd, '{}_{}.png'.format(output_png_dir,field_value))










