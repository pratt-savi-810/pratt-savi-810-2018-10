import arcpy


def select_bin_ids(
        input_bin,  # this is the input bin id
        input_footprints,  # this is the historic footprints file
        distance,  # this is the buffer dist.
):
    sql_bin = '''"BIN" = {}'''.format(input_bin)

    arcpy.MakeFeatureLayer_management(
        input_footprints,  # input feature class
        "build_lyr",  # output layer
        sql_bin,  # sql statement
    )

    arcpy.Buffer_analysis(
        "build_lyr",
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

    arcpy.Delete_management('build_lyr')
    arcpy.Delete_management('select_bin_lyr')
    arcpy.Delete_management('in_memory/buffer')

    arcpy.RefreshActiveView()

    return bin_list