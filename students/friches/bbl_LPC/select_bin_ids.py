import arcpy


footprints_file = 'C:/Users/friches/Documents/GitHub/data/building/LPC_IL_HD_Bld_DB_10_19_18.shp'


def select_bin_ids(
        input_bin,  #input bin id
        input_footprints,  #this is the historic footprints file
        distance,  #this is the buffer dist.
):


        sql_bin ='''"BIN" = {}'''.format(input_bin)

        arcpy.Delete_management("build_lyr")
        if arcpy. Exists ('input_bin_lyr'):
                arcpy.Delete_management('input_bin_lyr')
        if arcpy. Exists ('select_bin_lyr'):
                arcpy.Delete_management('select_bin_lyr')
        if arcpy. Exists ('in_memory/buffer'):
                arcpy.Delete_management('in_memory/buffer')


        arcpy.MakeFeatureLayer_management(
                input_footprints,  # input features class
                "build_lyr", #output layer
                '"BIN" = 1011258',
        ) #squl statment

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
                'in_memory/buffer3'
        )

        bin_list = []

        arcpy.Delete_management("build_lyr")
        arcpy.Delete_management('input_bin_lyr')
        arcpy.Delete_management('select_bin_lyr')
        arcpy.Delete_management('in_memory/buffer')

select_bin_ids ('1011258', footprints_file, '400 Feet')