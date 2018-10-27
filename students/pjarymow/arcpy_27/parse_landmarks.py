import pandas as pd
import arcpy

# create dataframe variable
in_csv = 'C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/LPC_LL_OpenData_2015Nov.csv'
df = pd.read_csv(in_csv)

# print(df.head(10))

df_MN = df[(df['BoroughID'] == 'MN')]  # query to only select borough ID manhattan

# print(df.dtypes)

# print(df.BBL.describe())

# print(df.BLOCK.describe())

# create longitude column and fill it with data
# df['longitude'] = df['the_geom']
# print(df.longitude.head())

# split function divides a string at a character and creates a list of strings from each split
# split the_geom at first open parenthesis and return string to the right
# df['longitude'] = df['the_geom'].str.split('(').str[1]
# print(df.longitude.head())

# split the_geom at first open parenthesis and return string to the right
# then split result at the space and return string to the left
df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
print(df.longitude.head())

# split the_geom at second space and return string to the right
# then replace closing parenthesis with no character
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')', '')
print(df.latitude.head())

out_csv = in_csv.replace('.csv', '_clean.csv')

df.to_csv(out_csv, index=False)

arcpy.MakeXYEventLayer_management(
    out_csv,
    'longitude',
    'latitude',
    'in_memory_xy_layer',
)

print('made event layer')

arcpy.FeatureClassToFeatureClass_conversion(
    'in_memory_xy_layer',
    'C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/students/pjarymow/arcpy_27/data-10_27_2018/',
    'landmarks.shp',
)

print('complete')
