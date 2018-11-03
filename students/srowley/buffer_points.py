

import arcpy

shape_folder = "C:/Users/srowley4/Documents/pratt-savi-810-2018-10/Students/SheriRowley/data/this_new"
input_points = "geo_export_be5a515e-3c1e-4f30-ba2d-31bd137fa6db.shp"


# buffer:desktop.arcgis.com/en/arcmap/latest/tools/analysis-toolbox/buffer.htm
#copy as python snippet
#remove the optional parameters, and change the output filename because arcgis doesn't like to overwrite
# layers in arc catalog
arcpy.Buffer_analysis(
    "C:/Users/srowley4/Documents/pratt-savi-810-2018-10/Students/SheriRowley/data/this_new/geo_export_be5a515e-3c1e-4f30-ba2d-31bd137fa6db.shp",
    "C:/Users/srowley4/Documents/ArcGIS/Default.gdb/wifi_new",
    "100 feet",
)

