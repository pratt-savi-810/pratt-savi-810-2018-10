import pandas as pd

def export_map_for_feature_in_fc(fc, mxd_file, unique_fieldname, output_png_dir):
    # declared mxd as current (instead of mxd filepath)
    mxd = arcpy.mapping.MapDocument(mxd_file)

    # got my map_dataframe from the mxd object
    map_df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

    # make empty
    df = feature_class_to_dataframe(fc)

    list_of_field_values = df[unique_fieldname].unique()

    for field_value in list_of_field_values:
        print(field_value)
        # select feature by attribute from layer - attribute being boro_name
        arcpy.SelectLayerByAttribute_management(
            fc,
            "NEW_SELECTION",
            """ "{}" = '{}' """.format(
                unique_fieldname,
                field_value.replace("'", '"'),
            ),

        )

        map_df.zoomToSelectedFeatures()

        arcpy.SelectLayerByAttribute_management(fc, "CLEAR_SELECTION")

        arcpy.mapping.ExportToPNG(
            mxd, '{}_{}.png'.format(
                output_png_dir,
                field_value.replace('/', '').replace("""n\""", '')
            )
        )


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