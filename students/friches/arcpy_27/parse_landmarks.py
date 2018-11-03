

import pandas as pd

import arcpy

in_csv = 'C:/Users/friches/Documents/data/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)


# print(df.dtypes)
# print(df.head())
# df= df[(df['boroughID']== 'MN'   ONLY  GET DATA FOR MANHATTAN BOROUGH

dfg = df.groupby(['LM_name']).count()

print(dfg.head())

# print(df.BBL.describe())


# CNTRL FOWARD / TO COMMENT SELECTION OUT

# df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
# df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')
#
# # print(df.head())
#
# out_csv = in_csv.replace ('.csv', '_clean.csv')
#
# df.to_csv(out_csv, index = False)
#
# arcpy.MakeXYEventLayer_management(
#     out_csv,
#     'longitude',
#     'latitude',
#     'in memory_xy_layer',)
#
# arcpy.FeatureClassToFeatureClass_conversion(
#     'in_memory_xy_layer',
#     'C:/Users/friches/Documents/data',
#     'landmarks.shp')



