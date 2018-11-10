import arcpy
import pandas as pd

def feature_class_to_csv(in_fc, in_csv):
    field_list = get_fc_fields(in_fc)
    df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
    df.columns = field_list
    df.to_csv(in_csv, encoding='utf-8', index=false)
    # check out https://joelmccune.com/arcgis-to-pandas-data-frame-v2-0/

def feature_class_to_dataframe(in_fc):
    field_list = get_fc_fields(in_fc)
    df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])
    df.columns = field_list
    return df
    # check out https://joelmccune.com/arcgis-to-pandas-data-frame-v2-0/


def get_fc_fields(fc):
    field_names = []
    fields = arcpy.ListFields(fc)
    for field in fields:
        field_names.append(field.name)
    return field_names

def export_map_for_feature_in_fc(fc, mxd_file, unique_fieldname, output_png_dir):
    # declared mxd as current (instead of mxd filepath)
    mxd = arcpy.mapping.MapDocument(mxd_file)

    # got my map
    map_df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

    # make empty list that we will fill with field values using SearchCursor
    df = feature_class_to_dataframe(fc)
    list_of_field_values = df.unique_fieldname.unique()

    with arcpy.da.SearchCursor(fc, unique_fieldname) as cursor:
        for row in cursor:
            list_of_field_values.append(row[0])

    for field_value in list_of_field_values:
        arcpy.SelectLayerByAttribute_management(
            fc,
            "NEW_SELECTION",
            """ "{}" = {} """.format(unique_fieldname, field_value),
        )

        map_df.zoomToSelectedFeatures()

        arcpy.SelectLayerByAttribute_management(fc, "CLEAR SELECTION")

        arcpy.RefreshActiveView()

        arcpy.mapping.ExportToPNG(
            mxd,
            '{}_{}.png'.format(output_png_dir, field_value),
        )
 sdf
