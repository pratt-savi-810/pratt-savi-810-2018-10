import arcpy
import pandas as pd
file = r'E:\Python for ArcGIS\ClassProject\Data\ACS_16_5YR_B25070.csv'
grentper_df = pd.read_csv(file)
grentper_df
grentper_df.rename(index = str, columns = {'GEO.id':'GEOid', 'GEO.id2':'GEOid2', 'GEO.display-label': 'Geography'})
grentper_df.drop([0])
grentper_df.to_csv(r'E:\Python for ArcGIS\ClassProject\Data\GRentPercent.csv')
# nycgeoclient to geocode address to the building footprint

import arcpy
import pandas as pd

file = r'E:\Python for ArcGIS\ClassProject\Data\brooklynbldgsRS16.csv'
bkbuildings_df = pd.read_csv(file)
bkbuildings_df
bkbuildings_df['BlocLot'] = ""
bkbuildings_df
bkbuildings_df['BlocLot'] = bkbuildings_df['BLOCK'] + bkbuildings_df['LOT']
bkbuildings_df
bkbuildings_df.dtypes

arcpy.env.workspace E:\Python for ArcGIS\ClassProject\Data\BKMapPLUTO.shp

import arcpy
import pandas as pd
import geocoder

address_df = pd.read_csv(r'E:\Python for ArcGIS\ClassProject\Data\brooklynbldgsRSAddress.csv')
address_df
address_df['lat'] = ""
address_df['long'] = ""
address_df
for index, row in address_df.iterrows():
    print(index, row)
for index, row in address_df.iterrows():
    g = geocoder.arcgis(row['ADDRESS'])
    row['lat'] = g.lat
    row['long'] = g.lng
address_df
address_df.to_csv(r'E:\Python for ArcGIS\ClassProject\Data\brooklynbldgsRSlatlng.csv')

