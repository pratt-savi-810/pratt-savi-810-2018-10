import arcpy

footprint_files = r'C:\Users\cwunsch\Desktop\Class 2\LPC_IL_HD_Bld_DB_10_19_18.shp'


def select_bin_ids(  # this is the funct. use to compute all of the blw including the 'make feature layer' scripts, etc.
        input_bin,  # this is the input BIN ID
        input_footprint,  # this is the historic footprints file
        distance,   # this is the buffer distance
):
    sql_bin = '''"BIN" = {}'''.format(input_bin)

    if arcpy.Exists('Build_lyr'):
        arcpy.Delete_management('Build_lyr')
    if arcpy.Exists('select_bin_lyr'):
        arcpy.Delete_management('select_bin_lyr')
    if arcpy.Exists('in_memory/buffer'):
        arcpy.Delete_management('in_memory/buffer')

    arcpy.MakeFeatureLayer_management(
        input_footprint,  # input feature class
        "Build_lyr",  # output feature class
        sql_bin,
    )

    arcpy.Buffer_analysis(
        "Build_lyr",
        "in_memory/buffer7",
        distance,
    )

    arcpy.MakeFeatureLayer_management(
        input_footprint,
        'select_bin_lyr',
    )

    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr',
        'INTERSECT',
        'in_memory/buffer7',
    )

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    # arcpy.Delete_management('input_bin_lyr')
    # arcpy.Delete_management('select_bin_lyr')
    # arcpy.Delete_management('in_memory/buffer')

    return bin_list
