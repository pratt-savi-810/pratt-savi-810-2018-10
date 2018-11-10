import arcpy
import pandas as pd


def get_fc_fields(fc):
    field_names = []
    fields = arcpy.ListFields(fc)
    for field in fields:
        field_names.append(field.name)
    return field_names

field_list = get_fc_fields(in_fc)

for row in arcpy.da.SearchCursor(in_fc, field_list)


    def feature_class_to_dataframe(in_fc):
        field_list = get_fc_fields(in_fc)
        df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
        df.columns = field_list
        return df
        # check out https://joelmccune.com/arcgis-to-pandas-data-frame-v2-0/

def feature_class_to_crv(in_fc, in_csv):
    field_list = get_fc_fields(in_fc)
    df = pd.DataFrame(
        [row for row in arcpy.da.SearchCursor(in_fc, field_list)]
    )
    df.columns = field_list
    df.to_csv(in_csv, encoding='utf-8', index=False)