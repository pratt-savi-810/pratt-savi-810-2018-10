import arcpy


def select_bin_ids(
        input_bin,
        input_footprints,
        distance,
):

    sql_bin = '"BIN" = {}'.format(input_bin)
    print(sql_bin)
    arcpy.Delete_management('input_bin_lyr1')
    arcpy.MakeFeatureLayer_management(input_footprints, 'input_bin_lyr1', where_clause=sql_bin)
    print(arcpy.GetCount_management('input_bin_lyr1'))
    arcpy.Buffer_analysis('input_bin_lyr1', 'Z:/Windows/Buffer17.shp', distance)
    arcpy.MakeFeatureLayer_management(input_footprints, 'select_bin_lyr2')
    arcpy.SelectLayerByLocation_management('select_bin_lyr2', 'INTERSECT', 'Z:/Windows/Buffer17.shp')

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr2', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    print(bin_list)
    # arcpy.Delete_management('input_bin_lyr')
    # arcpy.Delete_management('select_bin_lyr')
    return bin_list

