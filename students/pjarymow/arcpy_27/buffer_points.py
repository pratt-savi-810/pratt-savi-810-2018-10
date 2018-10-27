import arcpy

shape_folder = 'C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/Unzipped_2018-10-27'
input_points = 'Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp'

arcpy.Buffer_analysis(
    "C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/Unzipped_2018-10-27/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp",
    "C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/Unzipped_2018-10-27/Production_Open_Data_HOTSPOT_buffer_from_script_dis.shp",
    "500 Feet",
    dissolve_option="ALL",
)

# arcpy.Buffer_analysis(
#     in_features="C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/Unzipped_2018-10-27/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp",
#     out_feature_class="C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/Unzipped_2018-10-27/Production_Open_Data_HOTSPOT_buffer.shp",
#     buffer_distance_or_field="100 Feet",
#     line_side="FULL",
#     line_end_type="ROUND",
#     dissolve_option="NONE",
#     dissolve_field="",
#     method="PLANAR"
# )

