#  be sure to disable background geoprocessing for in_memory issues
import arcpy

footprints_file = r'C:/Users/jbagtas/Documents/LPC_IL_HD_Bld_DB_10_19_18.shp'

def select_bin_ids(
        input_bin, # this is the input bin ID
        input_footprints,  # this is the historic footprints file
        distance,  # parameter; this is the buff dist
):

    sql_bin = '''"BIN" = {}'''.format(input_bin)


    if arcpy.Exists('build_lyr'):
        arcpy.Delete_management('build_lyr')
    if arcpy.Exists('build_lyr'):
        arcpy.Delete_management('select_bin_lyr')
    if arcpy.Exists('in_memory/buffer5'):
        arcpy.Delete_management('in_memory/buffer5')

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        "build_lyr",  #output in memory
        sql_bin,  # sql statement
    )

    arcpy.Buffer_analysis(
        'build_lyr',
        'in_memory/buffer5',
        distance,
    )

    arcpy.MakeFeatureLayer_management(
        input_footprints,
        'select_bin_lyr'
    )

    arcpy.SelectLayerByLocation_management(
        'select_bin_lyr',
        'INTERSECT',
        'in_memory/buffer5'
    )

    bin_list = []

    with arcpy.da.SearchCursor('select_bin_lyr', 'BIN') as cursor:
        for row in cursor:
            bin_list.append(row[0])

    arcpy.Delete_management('build_lyr')
    arcpy.Delete_management('select_bin_lyr')
    arcpy.Delete_management('in_memory/buffer5')

    return bin_list


print(select_bin_ids('1011250',footprints_file,'400 feet'))

