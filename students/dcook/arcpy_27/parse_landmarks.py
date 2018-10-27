import pandas as pd

in_csv = 'C:/Users/dcook13/Documents/data/LPC_LL_OpenData_2015Nov.csv'

df = pd.read_csv(in_csv)

print(df.head())

## print the datatypes of the columns
print(df.dtypes)

print(df.BBL.describe())

# x = 'apple&banana&cherry'
# x.split('&')[0] => apple
# x.split('&')[1] => banana

# the_geom: POINT (-74.00377535992043 40.74645125048846)
df['longitude'] = df['the_geom'].str.split('(').str[1].str.split(' ').str[0]
df['latitude'] = df['the_geom'].str.split(' ').str[2].str.replace(')','')

out_csv = in_csv.replace('.csv','_clean.csv')
df.to_csv(out_csv, index=False)

import arcpy

# http://desktop.arcgis.com/en/arcmap/latest/tools/data-management-toolbox/make-xy-event-layer.htm

arcpy.MakeXYEventLayer_management(
    out_csv
    , 'longitude'
    , 'latitude'
    , out_layer='in_memory_xy_layer'
)

# http://pro.arcgis.com/en/pro-app/tool-reference/conversion/feature-class-to-feature-class.htm

arcpy.FeatureClassToFeatureClass_conversion(
    'in_memory_xy_layer'
    , 'C:/Users/dcook13/Documents/output/'
    , 'landmarks.shp'
)

df = df[(df['BoroughID']=='MN')]
# ... 'landmarks_fips_36061.shp'

print(len(df.index))

print('Count of Historic Landmarks by District in Manhattan')

## probably a better way to do this
dfcounts = df.groupby(['LM_NAME'], as_index=False).count()
dfcounts = dfcounts['LM_NAME','BBL']






















