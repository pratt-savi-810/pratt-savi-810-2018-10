import arcpy
import pandas as pd


def get_lps_from_bbls(lpc_points, input_bbls):
    df_list = []

    for in_bbl in input_bbls:
        print(in_bbl)

        df = lp_points_to_df(lpc_points)
        df = select_single_query_from_dataframe(df, 'bin_number', in_bbl)
        # df = df['lp_number'].unique().tolist()

        df_list.append(df)

    master_df = pd.concat(df_list, sort=True)
    master_df = master_df[['bin_number', 'lp_number']]
    print(master_df)
    return master_df


def lp_points_to_df(in_fc):
    df = feature_class_to_dataframe(in_fc)
    return df


def select_single_query_from_dataframe(df, column, value):
    # print(df.dtypes)
    df = df[(df[column] == value)]
    return df


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
