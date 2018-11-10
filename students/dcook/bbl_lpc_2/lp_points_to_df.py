## grab feature class/layer and export as a dataframe

##

##

import arcpy
import pandas as pd

## footprints_file = r"C:\\Users\\dcook13\\Downloads\\LPC_IL_HD_Bld_DB_10_19_18\\LPC_IL_HD_Bld_DB_10_19_18.shp"
## landmark_points = r"C:\\Users\\dcook13\\Downloads\\IND_Landmark_Points_10_26_18_revised\\IND_Landmark_Points_10_26_18_revised.shp"

def get_fc_fields(fc):
    field_names = []
    fields = arcpy.ListFields(fc)
    for field in fields:
        field_names.append(field.name)
    return field_names
## displays values as u'...' because the field names are in a unicode format, the print function will print without

## footprints_fields = get_fc_layer(footprints_file)
## for row in arcpy.da.SearchCursor(footprints_file, footprints_fields):
##  print(row)


def feature_class_to_dataframe(in_fc):
    field_list = get_fc_fields(in_fc)
    df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
    df.columns = field_list
    return df


## lp_df = feature_class_to_dataframe(landmark_points)
## lp_df.head()

## .to_csv(r'...', encoding='utf-8')

def feature_class_to_csv(in_fc, in_csv):
    field_list = get_fc_fields(in_fc)
    df = pd.DataFrame(
        [row for row in arcpy.da.SearchCursor(in_fc, field_list)]
    )
    df.columns = field_list
    return df.to_csv(in_csv, encoding='utf-8', index=False)
## feature_class_to_csv(landmark_points, r'landmark_table.csv')


## for each layer in the arcgis map document dataframe, convert to csv

mxd = arcpy.mapping.MapDocument('CURRENT')
map_df = arcpy.mapping.ListDataFrames(mxd,'Layers')[0]
arcpy.mapping.ListLayers(map_df)
list_mxd_layers = arcpy.mapping.ListLayers(map_df)
for i in list_mxd_layers:
    print(i)

for i in list_mxd_layers:
    feature_class_to_csv(i, r'...{}.csv'.format(i))







