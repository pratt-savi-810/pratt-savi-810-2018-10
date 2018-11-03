import arcpy

shape_folder =  'C:/Users/friches/Documents/data/THISISMYFOLDER'
input_points ='geo_export_bcc83c0a-84dc-4704-9cde-be700ad0e862.shp'


arcpy.Buffer_analysis(
    "C:/Users/friches/Documents/data/THISISMYFOLDER/geo_export_bcc83c0a-84dc-4704-9cde-be700ad0e862.shp",
    "C:/Users/friches/Documents/data/THISISMYFOLDER/geo_export_bcc83c0a84dc47049.shp",
    "100 Feet",
    dissolve_option="ALL",
)

