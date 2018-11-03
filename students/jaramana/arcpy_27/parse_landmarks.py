import pandas as pd

in_csv = 'C:/Users/ashaiban/Documents/data/individual_landmarks.csv'

df = pd.read_csv(in_csv)

df=df[(df['BoroughID'] == 'MN')]

print('Count of Historic Landmarks by District in Manhattan')

dfg=df.groupby(['LM_NAME']).count()

print(dfg.head)



#
# out_csv = in_csv.replace('.csv','_clean.csv')
#
# df.to_csv(out_csv, index=False)




#
# arcpy.MakeXYEventLayer_management (
#     out_csv,
#     'longitude',
#     'latitude',
#     'in_memory_xy_layer',
# )
#
# arcpy.FeatureClassToFeatureClass_conversion(
#     'in_memory_xy_layer',
#     'C:/Users/ashaiban/Documents/data/',
#     'landmarks.shp',
# )
#
# print(df.head())