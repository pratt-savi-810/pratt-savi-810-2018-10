import arcpy

# snipet from arccatalog results after running buffer from tool box, cannot overwrite

arcpy.Buffer_analysis(
    "C:/Users/hhernan9/Documents/GitHub/pratt-savi-810-2018-10/Students/Hector Hernandez/TEST/ new folder2018-10-27/geo_export_650b9d12-421d-48d0-848b-d4617175ae45.shp",
    "C:/Users/hhernan9/Documents/GitHub/pratt-savi-810-2018-10/Students/Hector Hernandez/TEST/ new folder2018-10-27/geo_export_650b9d12421d48d08test.shp",
    "100 Feet",
)