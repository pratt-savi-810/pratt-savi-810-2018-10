import arcpy

footprints_file = r'C:\Users\djasmin\Downloads\LPC_IL_HD_Bld_DB_10_19_18\LPC_IL_HD_Bld_DB_10_19_18.shp'


def select_bin_ids(
        input_bin,
        input_footprints,
        distance
):
    sql_bin = '''"BIN" = {}'''.format(input_bin)

    if arcpy.Exists('build_lyr'):
        arcpy.Delete_management('build_lyr')
    if arcpy.Exists('select_bin_lyr'):
        arcpy.Delete_management('select_bin_lyr')
    if arcpy.Exists('in_memory/buffer'):
        arcpy.Delete_management('in memory/buffer')

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        "build_lyr",
        sql_bin
    )

    arcpy.Buffer_analysis(
        "build_lyr",
        "in_memory/buffer1",
        distance,
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        'select_bin_lyr'
    )

    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr',
        'INTERSECT',
        'in_memory/buffer1'
    )

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
            for row in cursor:
                    bin_list.append(row[0])

    arcpy.Delete_management('input_bin_lyr')
    arcpy.Delete_management('select_bin_lyr')
    arcpy.Delete_management('in_memory/buffer1')

    return bin_list


s_bins = select_bin_ids('1011258', footprints_file, '400 feet')

print(s_bins)