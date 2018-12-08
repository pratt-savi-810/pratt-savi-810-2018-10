import arcpy

footprints_file = r'C:\Users\dgoodma7\Documents\lpc_data\LPC_IL_HD_Bld_DB_10_19_18.shp'


def select_bin_ids(
        input_bin,  # this is the input BIN ID
        input_footprints, # this is the historic footprints file
        distance,  # this is the buffer distance
):

    sql_bin = '''"BIN" = {}'''.format(input_bin)

    arcpy.Delete_management('build_lyr_new8')
    arcpy.Delete_management('input_bin_lyr')
    arcpy.Delete_management('select_bin_lyr')
    arcpy.Delete_management('in_memory/buffer')

    arcpy.MakeFeatureLayer_management(
        input_footprints,  # input feature class
        "build_lyr_new8",  # output layer
        sql_bin,  # sql statement
    )

    arcpy.Buffer_analysis(
        "build_lyr_new8",
        "in_memory/buffer",
        distance,
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        'select_bin_lyr',
    )
    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr',
        'INTERSECT',
        'in_memory/buffer',
    )

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])


    return bin_list

select_bin_ids('1011258',footprints_file,'400 Feet')