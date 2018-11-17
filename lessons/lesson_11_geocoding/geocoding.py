import geocoder
import pandas as pd
import arcpy

add_df = pd.read_csv(r'\Mac\Home\Desktop\Geocode\Addresses.csv')
add_df['Lat'] = ''
add_df['Long'] = ''

for index, row in add_df.iterrows():
    g = geocoder.arcgis(row['Address'])
    row['Lat'] = g.lat
    row['Long'] = g.lng

add_df.to_csv(r'\Mac\Home\Desktop\Geocode\LatLong_Plot.csv')

arcpy.MakeXYEventLayer_management(
    r'\Mac\Home\Desktop\Geocode\LatLong_Plot.csv',
    'Long',
    'Lat',
    'latlong_plot',
)

arcpy.CopyFeatures_management(
    'latlong_plot',
    r'\Mac\Home\Desktop\Geocode\address_plot.shp',
)
