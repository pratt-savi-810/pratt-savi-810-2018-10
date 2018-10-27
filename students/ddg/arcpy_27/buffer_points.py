import arcpy

shape_folder = 'C:/Users/dgoodma7/Documents/Data/wifi_2018-10-27_final'
input_points = 'geo_export_36e702aa-22ef-4786-834c-197f523f6895.shp'


arcpy.Buffer_analysis(
    "C:/Users/dgoodma7/Documents/Data/wifi_2018-10-27_final/geo_export_36e702aa-22ef-4786-834c-197f523f6895.shp",
    "C:/Users/dgoodma7/Documents/Data/wifi_2018-10-27_final/buffer_100_new_dis.shp",
    "1000 Feet",
    dissolve_option="ALL"
)
