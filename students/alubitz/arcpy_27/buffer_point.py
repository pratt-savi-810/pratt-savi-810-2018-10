import arcpy

shape_folder = 'C:/Users/alubitz/Documents/data/Unzipped_Folder'
input_points = 'Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp'

arcpy.Buffer_analysis(
    "C:/Users/alubitz/Documents/data/Unzipped_Folder/Production_Open_Data_HOTSPOTS_UPDATE_09072018.shp",
    "C:/Users/alubitz/Documents/data/Unzipped_Folder/Production_Open_Data_HOTSPOTv2_dissolve.shp",
    "500 Feet",
    dissolve_option='ALL'
)
