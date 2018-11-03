import arcpy

footprints_file = r'C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\students\hhernandez2783\Data110318\LPC_IL_HD_Bld_DB_10_19_18\LPC_IL_HD_Bld_DB_10_19_18.shp'

def select_bin_ids(
        input_bin, # this is the input bin id
        input_footprints,  # this is the historic footprints file
        distance,  # this is the buffer distance
):


    sql_bin = '''"Bin" = {}'''.format (input_bin)

    if arcpy.Exists('build_1yr'):
        arcpy.Delete_management('build_1yr')
    if arcpy.Exists('select_bin_1yr'):
        arcpy.Delete_management('select_bin_lyr')
    if arcpy.Exists('in_memory/buffer'):
        arcpy.Delete_management('in_memory/buffer')


    arcpy.MakeFeatureLayer_management(
        input_footprints,  # input feature class
        "build_1yr",  # output layer
        sql_bin,  # sql statement
    )

    arcpy.Buffer_analysis(
        "build_1yr",
        "in_memory/buffer",
        distance,
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        'select_bin_lyr')

    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr',
        'INTERSECT',
        'in_memory/buffer')

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    return bin_list


s_bins = select_bin_ids('1011258', footprints_file, '400 Feet')

print(s_bins)

#jkkj