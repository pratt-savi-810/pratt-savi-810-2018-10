import pandas as pd
import arcpy

in_csv = 'C:/Users/ksutton/Documents/Data/landmarks/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)

#print(df.head())

#print(df.dtypes)

print(df.BBL.describe())
# useful for number data types print(df.BBL.quantile)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')


out_csv = in_csv.replace('.csv', '_clean.csv')

df = df[(df['BoroughID'] == 'MN')]

print (len(df.index))
print('Count of Historic Landmarks by District in Manhattan')

dfg = df.groupby(['LM_NAME']).count()
df['count_landmarks_in_district'] = dfg['BBL']

print(dfg.head)

dfg.to_csv(out_csv.replace('.csv', 'mn_landmarks_count_dis.csv'), index=False)
print(df.head())

df.to_csv(out_csv, index=False)

arcpy.MakeXYEventLayer_management(
    out_csv,
    'longitude',
    'latitude',
    'in_memory_xy_layer',
)

arcpy.FeatureClassToFeatureClass_conversion(
    'in_memory_xy_layer',
    'C:/Users/ksutton/Documents/Data/landmarks',
    'landmarks.shp',
)

# arcpy.FeatureClassToFeatureClass_conversion(
#     'in_memory_xy_layer',
#     'C:/Users/ksutton/Documents/Data/landmarks',
#     'landmarks.shp',
# )

