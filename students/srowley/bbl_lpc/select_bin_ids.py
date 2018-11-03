import arcpy

footprints_file = r'C:\Users\srowley4\Documents\DATA\LPC_IL_HD_Bld_DB_10_19_18.shp'


def select_bin_ids(
        input_bin, #this is the input bin id
        input_footprints, #this is the historic footprints file
        distance, # this is the buffer distance
):
    sql_bin = '''"BIN" = 1011258'''.format(input_bin)

    arcpy.Delete_management('build_lyr')
    if arcpy.Exists('input_bin_lyr'):
        arcpy.Delete_management('input_bin_lyr')
    if arcpy.Exists('select_bin_lyr'):
        arcpy.Delete_management('select_bin_lyr')
    if arcpy.Exists('in_memory/buffer2'):
        arcpy.Delete_management('in_memory/buffer3')

    arcpy.MakeFeatureLayer_management(
        input_footprints, #"LPC_IL_HD_Bld_DB_10_19_18",#input feature class
        "build_lyr",#output layer
        sql_bin, # '"BIN" = 10111258'(variable created to hold this), sql statement
    )

    arcpy.Buffer_analysis(
       "build_lyr",
       "in_memory/buffer6",
       distance,
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints, 'select_bin_lyr'
    )

    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr', 'INTERSECT', 'in_memory/buffer6'
    )

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    return bin_list


s_bins = select_bin_ids('1011258', footprints_file, '400 Feet')

print(s_bins)