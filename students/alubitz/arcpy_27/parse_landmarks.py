import pandas as pd
import arcpy

in_csv = 'C:/Users/alubitz/Downloads/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')

out_csv = in_csv.replace('.csv', '_clean.csv')

df = df[(df['BoroughID'] == 'MN')]
print(len(df.index))
print("Count of Historic Landmarks by District in Manhattan")

dfg = df.groupby(['LM_NAME'], asIndex=False).count()

dfg['count_landmarks_dist'] = dfg['BBL']

print(dfg.head)

df.to_csv(out_csv.replace('.csv', 'MN_landmarks_count_dist.csv'), index=False)

# arcpy.MakeXYEventLayer_management(
#     out_csv,
#     'longitude',
#     'latitude',
#     'ram_xy_layer'
# )
#
# arcpy.FeatureClassToFeatureClass_conversion(
#     'ram_xy_layer',
#     'C:/Users/alubitz/Downloads',
#     'landmarks.shp'
# )
