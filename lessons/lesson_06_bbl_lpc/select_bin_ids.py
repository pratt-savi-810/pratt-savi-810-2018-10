import arcpy


def select_bin_ids(
        input_bin,
        input_footprints,
        distance,
):
    sql_bin = '''"BIN" = {}'''.format(input_bin)
    arcpy.Delete_management('input_bin_lyr')
    arcpy.MakeFeatureLayer_management(input_footprints, 'input_bin_lyr', where_clause=sql_bin)
    arcpy.Buffer_analysis('input_bin_lyr', 'in_memory/buffer', distance)
    arcpy.MakeFeatureLayer_management(input_footprints, 'select_bin_lyr')
    arcpy.SelectLayerByLocation_management('select_bin_lyr', 'INTERSECT', 'in_memory/buffer')

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    arcpy.Delete_management('input_bin_lyr')
    arcpy.Delete_management('select_bin_lyr')
    arcpy.Delete_management('in_memory/buffer')
    return bin_list

