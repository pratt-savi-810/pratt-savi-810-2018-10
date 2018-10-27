import arcpy

shape_folder = 'C:/Users/dcook13/Documents/data/unzipped_folder'
shape_points = 'C:/Users/dcook13/Documents/data/unzipped_folder/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp'

## copy as python snippet
# arcpy.Buffer_analysis(in_features="C:/Users/dcook13/Documents/data/unzipped_folder/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp"
# , out_feature_class="C:/Users/dcook13/Documents/output/wifi_buffer.shp", buffer_distance_or_field="100 Feet", line_side="FULL"
# , line_end_type="ROUND", dissolve_option="NONE", dissolve_field="", method="PLANAR")

# http://desktop.arcgis.com/en/arcmap/latest/tools/analysis-toolbox/buffer.htm

## remove the optional parameters, and change the output filename because arcgis doesn't like to overwrite
# arcpy.Buffer_analysis(
#     in_features="C:/Users/dcook13/Documents/data/unzipped_folder/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp"
#     , out_feature_class="C:/Users/dcook13/Documents/output/wifi_buffer_2.shp"
#     , buffer_distance_or_field="100 Feet"
# )

arcpy.Buffer_analysis(
    in_features="C:/Users/dcook13/Documents/data/unzipped_folder/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp"
    , out_feature_class="C:/Users/dcook13/Documents/output/wifi_buffer_2diss.shp"
    , buffer_distance_or_field="1000 Feet"
    , dissolve_option='ALL'
)
































