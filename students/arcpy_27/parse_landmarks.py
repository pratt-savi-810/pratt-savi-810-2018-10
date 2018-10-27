import pandas as pd
import arcpy

in_csv = 'C:\Users\cwunsch\Documents\data\landmarks.csv'

df = pd.read_csv(in_csv)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')

out_csv = in_csv.replace('.csv', '_clean.csv')

print(len(df.index))

df = df[(df['BoroughID'] == 'MN')] #query to only select borough ID Manhattan
print(len(df.index))
print("Count of Historic Landmarks by District in Manhattan"

dfg = df.groupby(['LM_NAME'], as_index=False).count()
dfg= dfg ['count_landmarks_in_district'] =dfg['BBL']

# arcpy.MakeXYEventLayer_management(
#     out_csv, #this is the new file we just referenced above "landmarks_clean.csv"
#     'longitude', #the X
#     'latitude', #the Y
#     'in_memory_xy_layer' #the output
# )
#
# arcpy.FeatureClassToFeatureClass_conversion(
#     'in_memory_xy_layer',
#     'C:\Users\cwunsch\Documents\data',
#     'landmarks.shp'
# )
#


