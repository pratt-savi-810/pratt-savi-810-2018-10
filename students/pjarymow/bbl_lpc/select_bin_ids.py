import arcpy

footprints_file = r'C:\Users\pjarymow\Documents\ArcMap_Data\data\LPC_IL_HD_Bld_DB_10_19_18.shp'

def select_bin_ids(
        input_bin,              # this is the input BIN id
        input_footprints,       # this is the historic footprints file
        distance,               # this is the buffer distance
):
    sql_bin = '"BIN" = 1011258'

    if arcpy.Exists('build_lyr'):
        arcpy.Delete_management('build_lyr')

    if arcpy.Exists('select_bin_layer'):
        arcpy.Delete_management('select_bin_layer')

    if arcpy.Exists('in_memory/buffer'):
        arcpy.Delete_management('in_memory/buffer')

    arcpy.MakeFeatureLayer_management(
        input_footprints,       # input feature class
        "build_lyr",            # output layer
        sql_bin,                # sql statement
    )

    arcpy.Buffer_analysis(
        "build_lyr",            # input layer for buffer
        "in_memory/buffer",     # output buffer shape to memory - do not save as file
        distance,               # buffer distance
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints,       # input feature class
        "select_bin_layer",     # output layer
    )

    arcpy.SelectLayerByLocation_management(
        "select_bin_layer",     # input features for selection
        "INTERSECT",            # selection type
        "in_memory/buffer",     # layer by which to select
    )

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_layer', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    arcpy.Delete_management('build_lyr')
    arcpy.Delete_management('select_bin_layer')
    arcpy.Delete_management('in_memory/buffer')

    # arcpy.RefreshActiveView()

    return bin_list


# print(select_bin_ids('1011258', footprints_file, '400 Feet'))
