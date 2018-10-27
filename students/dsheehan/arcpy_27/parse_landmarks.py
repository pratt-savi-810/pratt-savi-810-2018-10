
import pandas as pd
import arcpy

in_csv = 'C:/Users/dsheehan/Downloads/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')

out_csv = in_csv.replace('.csv', '_clean.csv')

print(len(df.index))


df = df[(df['BoroughID'] == 'MN')]  # query to only select borough ID manhattan
print(len(df.index))
print('Count of Historic Landmarks by District in Manhattan')

dfg = df.groupby(['LM_NAME'], as_index=False).count()

dfg['count_landmarks_in_district'] = dfg['BBL']

dfg = dfg[['LM_NAME', 'count_landmarks_in_district']]

print(dfg.head)

dfg.to_csv(out_csv.replace('.csv', 'mn_landmarks_count_dist.csv'), index=False)

# df.to_csv(out_csv, index=False)

# arcpy.MakeXYEventLayer_management(
#     out_csv,
#     'longitude',
#     'latitude',
#     'in_memory_xy_layer',
# )
#
# arcpy.FeatureClassToFeatureClass_conversion(
#     'in_memory_xy_layer',
#     'C:/Users/dsheehan/Downloads/',
#     'landmarks_fips_36061.shp',
# )