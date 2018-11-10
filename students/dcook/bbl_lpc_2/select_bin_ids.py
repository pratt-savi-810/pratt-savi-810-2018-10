import arcpy

footprints_file = r"C:\\Users\\dcook13\\Downloads\\LPC_IL_HD_Bld_DB_10_19_18\\LPC_IL_HD_Bld_DB_10_19_18.shp"

def select_bin_ids(
        input_bin,  # the input bin id
        input_footprints,  # the historic footprints file
        distance,  # the buffer distance
):

    ## sql_bin = '"BIN" = 1011258'
    sql_bin = '''"BIN" = {}'''.format(input_bin)

    if arcpy.Exists('build_lyr'):
        arcpy.Delete_management('build_lyr')
    if arcpy.Exists('select_bin_lyr'):
        arcpy.Delete_management('select_bin_lyr')
    if arcpy.Exists('in_memory/buffer2'):
        arcpy.Delete_management('in_memory/buffer2')

    arcpy.MakeFeatureLayer_management(  # was arcpy.management.MakeFeatureLayer
        input_footprints,  # input... was "LPC_IL_HD_Bld_DB_10_19_18"
        'build_lyr',  # output... was "build_lyr"
        sql_bin,  # sql statement
    )

    arcpy.Buffer_analysis(  # was arcpy.analysis.Buffer
        'build_lyr',
        'in_memory/buffer2',  # was r"C:\Users\dcook13\Downloads\bl_buffer400.shp"
        distance,  # was "400 feet"
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        'select_bin_lyr',
    )

    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr',
        'INTERSECT',
        'in_memory/buffer2',
    )

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    arcpy.Delete_management('build_lyr')
    arcpy.Delete_management('select_bin_lyr')
    arcpy.Delete_management('in_memory/buffer2')
    return bin_list

select_bin_ids('1011258', footprints_file, '400 Feet')
