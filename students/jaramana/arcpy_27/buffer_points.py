import arcpy

arcpy.Buffer_analysis(
    in_features="C:/Users/ashaiban/Documents/data/hello/geo_export_f9edc9b4-626f-4a2f-9423-51324439a532.shp", out_feature_class="C:/Users/ashaiban/Documents/data/hello/wifihotspots_100ft.shp", buffer_distance_or_field="100 Feet", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field="", method="PLANAR")