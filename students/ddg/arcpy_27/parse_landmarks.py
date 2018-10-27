import pandas as pd
import arcpy

in_csv = 'C:/Users/dgoodma7/Documents/Data/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', "")

# print(df.head())

df = df[(df['LM_TYPE'] == 'Individual Landmark')]  # query to only select borough ID manhattan

out_csv = in_csv.replace('.csv','_clean2.csv')


df.to_csv(out_csv,index=False)

arcpy.MakeXYEventLayer_management(
    out_csv,
    'longitude',
    'latitude',
    'in_memory_xy_layer',
)

arcpy.FeatureClassToFeatureClass_conversion(
    'in_memory_xy_layer',
    'C:/Users/dgoodma7/Documents/Data/',
    'landmarks_mn_indiv.shp',
)
