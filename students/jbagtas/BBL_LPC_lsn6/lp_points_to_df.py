import arcpy
import pandas as pd

# use this in arcmap

def get_fc_fields(fc):  # get all field names
    field_names = []
    fields = arcpy.ListFields(fc)
    for field in fields:
        field_names.append(field.name)
    return field_names



in_fc = 'IND_Landmark_Points_10_26_18_revised'  #  in_fc = the layer you're using, drag from layer panel

field_list = get_fc_fields(in_fc)

for row in arcpy.da.SearchCursor(in_fc, field_list):
...     print(row)

def feature_class_to_dataframe(in_fc):
     field_list = get_fc_fields(in_fc)
     df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
     df.columns = field_list
     return df

feature_class_to_dataframe(in_fc)


def feature_class_to_csv(in_fc, in_csv):
    field_list = get_fc_fields(in_fc)
    df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
    df.columns = field_list
    df.to_csv(in_csv, encoding = 'utf-8', index = False)


feature_class_to_csv('IND_Landmark_Points_10_26_18_revised', r'C:\Users\jbagtas\Documents\IND_Landmark_Points_10_26_18_revised.csv')

##

arcpy.SelectLayerByAttribute_management('ny boros',"NEW_SELECTION",""" "BoroName" = 'Manhattan' """)
                                        #  """ allows you to use a mix quotation marks correctly " "Boro


##

def export_map_for_feature_in_fc(fc, mxd_file, unique_fieldname, output_png_dir):
    mxd = arcpy.mapping.MapDocument(mxd_file)
    map_df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
    df = feature_class_to_dataframe(fc)
    list_of_field_values = df[unique_fieldname].unique()]
    with arcpy.da.SearchCursor(fc, unique_fieldname) as cursor:
        for row in cursor:
            list_of_field_values.append(row[0])
    for field_value in list_of_field_values:
        print(field_value)
        arcpy.SelectLayerByAttribute_management(
            fc,
            "NEW_SELECTION",
            """ "{}" = '{}' """).format(unique_fieldname, field_value)
    map_df.zoomToSelectedFeatures()
    arcpy.refreshActiveView()
    arcpy.SelectLayerByAttribute_management('CLEAR SELECTION')
    arcpy.mapping.ExportToPNG(
        mxd,
        '{}_{}.png'.format(
            output_png_dir,
            field_value.replace('/','').replace("'",'')
        )


)

df = feature_class_to_dataframe
export_map_for_feature_in_fc( )