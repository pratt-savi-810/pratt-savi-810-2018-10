

import pandas as pd
import arcpy

in_csv = 'C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\Students\Hector Hernandez\TEST\LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)
#created columns and split string
df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')','')

print(df.head())

out_csv = in_csv.replace('.csv', '_clean.csv')

print(len(df.index)

df = df[(df['BoroughID'] == 'MN')] # query to only select borough ID manhattan
print(len(df.index)
print("Count of Historic Landmarks by District in Manhattan")

dfg =df.groupby(['LM_Name']).count()

print(dfg.head)

dfg.to_csv(out_csv.replace, index=False)

#project xy coordinates
#
# arcpy.MakeXYEventLayer_management(
#     out_csv,
#     'longitude',
#     'latitude',
#     'in_memory_xy_layer',
# )
#
# #make a shapefile
#
# arcpy.FeatureClassToFeatureClass_conversion(
#     'in_memory_xy_layer',
#     'C:\Users\hhernan9\Documents\GitHub\pratt-savi-810-2018-10\Students\Hector Hernandez\TEST',
#     'landmarks.shp'
)