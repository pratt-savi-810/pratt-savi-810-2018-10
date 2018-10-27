import arcpy

shape_folder = 'C:/Users/ksutton/Documents/Data/wifi/MYFOLDER'
input_points = 'Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp'

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Production_Open_Data_HOTSPOTS_UPDATE_09072018"
arcpy.Buffer_analysis(
    "C:/Users/ksutton/Documents/Data/wifi/MYFOLDER/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp",
    "C:/Users/ksutton/Documents/Data/wifi/MYFOLDER/wifi_buffer_100ft_2.shp",
    "100 Feet",
    dissolve_option="ALL",
)


