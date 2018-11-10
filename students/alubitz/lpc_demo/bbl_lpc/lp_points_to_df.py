import arcpy
import pandas as pd


def get_lps_from_bbls(lpc_points, input_bins):
    df_list = []
    df_all_lp = lp_points_to_df(lpc_points)
    for in_bin in input_bins:
        df = select_single_query_from_dataframe(df_all_lp, 'bin_number', in_bin)
        df_list.append(df)

    master_df = pd.concat(df_list)  # , sort=True)
    return master_df[['bin_number', 'lp_number']]


#  def lp_points_to_df(in_fc):
#  df = feature_class_to_dataframe(in_fc)
#  return df


def select_single_query_from_dataframe(df, column, value):
    # print(df.dtypes)
    df = df[(df[column] == value)]
    return df

def
# declared mxd as current (instead of mxd filepath since this was in ArcMap desktop)
mxd = arcpy.mapping.MapDocument(mxd_file)

# extracted map_datafram from the mxd object
map_df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

# make empty


list_of_field_values = unique_fieldname.unique

with arcpy.da.SearchCursor(fc, unique_fieldname) as cursor:
	for row in cursor:
		list_of_field_values.append(row[0])

for field_value in list_of_field_values:
	#select feature by atribute from layer - attribute being boro name
	arcpy.SelectLayerByAttribute_management(
		fc,
		"NEW_SELECTION",
		""" "{}" = '{}'' """.format(unique_fieldname, field_value),
		)

	map_df.zoomToSelectedFeatures()

#   arcpy.clearselectedfeature

#	arcpy.mapping.ExportToPNG




def feature_class_to_dataframe(in_fc):
    field_list = get_fc_fields(in_fc)
    df = pd.DataFrame([row for row in arcpy.da.SearchCursor(in_fc, field_list)])  # converting feature class to df
    df.columns = field_list
    return df
    # check out https://joelmccune.com/arcgis-to-pandas-data-frame-v2-0/


def get_fc_fields(fc):
    field_names = []
    fields = arcpy.ListFields(fc)
    for field in fields:
        field_names.append(field.name)
    return field_names
