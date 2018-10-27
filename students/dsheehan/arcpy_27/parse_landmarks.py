
import pandas as pd
import arcpy

in_csv = 'C:/Users/dsheehan/Downloads/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')

out_csv = in_csv.replace('.csv', '_clean.csv')

df.to_csv(out_csv, index=False)

arcpy.MakeXYEventLayer_management(
    out_csv,
    'longitude',
    'latitude',
    'in_memory_xy_layer',
)

arcpy.FeatureClassToFeatureClass_conversion(
    'in_memory_xy_layer',
    'C:/Users/dsheehan/Downloads/',
    'landmarks.shp',
)