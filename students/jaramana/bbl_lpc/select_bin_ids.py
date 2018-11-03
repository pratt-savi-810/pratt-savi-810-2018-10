import arcpy

footprints_file = r'C:\Users\ashaiban\Desktop\Lesson 6\lpc_data\LPC_IL_HD_Bld_DB_10_19_18.shp'

def select_bin_ids (
        input_bin,  # this is the input bin id
        input_footprints,  # this is the historic footprints file
        distance,  #this is the buffer distance
):
    sql_bin = ' "BIN" = 1011258'

    arcpy.Delete_management('input_bin_lyr')

    arcpy.MakeFeatureLayer_management(
        input_footprints, #input feature class
        "input_bin_lyr", #output layer
        where_clause=sql_bin
    )

    arcpy.Buffer_analysis(
        "input_bin_lyr",
        "in_memory/buffer2",
        distance
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        'select_bin_lyr')

    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr',
        'INTERSECT',
        'in_memory/buffer2')

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    if arcpy.Exists('input_bin_lyr'):
        arcpy.Delete_management('input_bin_lyr')
    if arcpy.Exists('select_bin_lyr'):
        arcpy.Delete_management('select_bin_lyr')
    if arcpy.Exists('in_memory/buffer'):
        arcpy.Delete_management('in_memory/buffer')

    return bin_list

select_bin_ids('1011258', footprints_file, '400 Feet')