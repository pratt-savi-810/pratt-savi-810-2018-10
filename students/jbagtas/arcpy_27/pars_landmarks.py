# Create feature layer from non-spatial data, like csv
# LAT LON in the following csv is in one field, use Pandas to sep

import pandas as pd
import arcpy
# suffix "as pd" lets you use pd.object rather than pandas.object

in_csv = 'C:/Users/jbagtas/Documents/Data/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv) #df standing for dataframe, like a spreadsheet. not the arcmap dataframee (viewer)

# print(df.head())  # head() is first 10 rows of file

#  print(df.dtypes)   shows data types

print(df.BBL.describe())  # BBL is a field in df our csv

#  dataframe.field.function

# yields:
#  count          46637
# unique         35419
# top       1000010010
# freq             101
# Name: BBL, dtype: int64


# df['longitude'] = 'potato' replaces all with potato

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0] #  split at certain delimiters, [] specifies which delimiter if there are several
#  [0] -> when index is zero it finds everything to the left of the delimter
#  str.split('(').str[1] denotes where to start the split
#  str.split(' ').str[0] denotes where to end the split
# finds the data after the 1st delimter (parenthesis) but before the next delimiter (space)

df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')','')

print(df.head())

out_csv = in_csv.replace('.csv', '_clean.csv')

df.to_csv(out_csv, index = False)

arcpy.MakeXYEventLayer_management(
    out_csv,
    'longitude',
    'latitude',
    'in_memory_xy_layer', #  create name of your layer to be put into memory
)

arcpy.FeatureClassToFeatureClass_conversion(
    'in_memory_xy_layer', #  calling the name you created in previous step
    'C:/Users/jbagtas/Documents/Data/',
    'landmarks.shp'
)

#query

print("Count of Historic Landmarks by district in manhattan")
dfg['count_landmarks_in_district'] = df[BBL]
#  creating new variable dfg and create a new column within it
df.groupby(['LM_NAME']).count()
dfg['count_landmarks_in_district']  #  creating new column
print(dfg.head())

arcpy.MakeXYEventLayer_management(
    out_csv,
    'longitude',
    'latitude',
    'in_memory_xy_layer', #  create name of your layer to be put into memory
)

arcpy.FeatureClassToFeatureClass_conversion(
    'in_memory_xy_layer', #  calling the name you created in previous step
    'C:/Users/jbagtas/Documents/Data/',
    'landmarks.shp'
)

