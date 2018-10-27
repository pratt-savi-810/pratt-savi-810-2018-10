import arcpy

shape_folder = 'C:/Users/dsheehan/Documents/data/THISISMYFOLDER'
input_points = 'geo_export_f909e93e-0e35-41f5-bf27-52f178cceae9.shp'


arcpy.Buffer_analysis(
    "C:/Users/dsheehan/Documents/data/THISISMYFOLDER2018-10-27/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp",
    "C:/Users/dsheehan/Documents/data/THISISMYFOLDER2018-10-27/wifi_buffer_v2_undis.shp",
    "500 Feet",
)


tables_list = [
    'a',
    'b',
    'c',
    'd'
]




