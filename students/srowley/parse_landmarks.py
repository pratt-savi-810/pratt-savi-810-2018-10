


import pandas as pd
import arcpy

in_csv = 'C:/Users/srowley4/Documents/pratt-savi-810-2018-10/Students/SheriRowley/data/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')

out_csv = in_csv.replace('.csv', '_clean.csv')

df.to_csv(out_csv, index=False)

# arcpy.MakeXYEventLayer_management(
#     out_csv,
#     'longitude',
#     'latitude',
#     'in_memory_xy_layer',
# )
#
# arcpy.FeatureClassToFeatureClass_conversion(
#     'in_memory_xy_layer',
#     'C:/Users/srowley4/Documents/pratt-savi-810-2018-10/Students/SheriRowley/data',
#     'landmarks.shp',
# )
df = df(['boroughid'] =='MN')]#query to only selct boroughs in manhattan
print (count of historic district in manhattan
dfg=df.groupby(['lm_name']).count()
print(dfg)