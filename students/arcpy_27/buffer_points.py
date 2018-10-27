import arcpy

#shape_folder = 'C:/Users/cwunsch/Documents/data/wifi_MYFOLDER2018-10-27'
#input_points = 'C:\Users\cwunsch\Documents\data\wifi_MYFOLDER2018-10-27\geo_export_f6165e20-9b92-4c43-996b-4f70f92bec0f.shp'

#def myfunction(param_1)

arcpy.Buffer_analysis(
    "C:/Users/cwunsch/Documents/data/wifi_MYFOLDER2018-10-27/geo_export_f6165e20-9b92-4c43-996b-4f70f92bec0f.shp",
    "C:/Users/cwunsch/Documents/data/wifi_MYFOLDER2018-10-27/buffer_dissolve.shp",
    "200 Feet",
    dissolve_option = 'ALL'

)

