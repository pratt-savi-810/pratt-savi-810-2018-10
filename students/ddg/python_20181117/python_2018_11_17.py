import geocoder
import pandas as pd
import arcpy

add_df = pd.read_csv(r'C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project_20181117\brooklyn_addresses_for_project_test.csv')
add_df['Lat'] = ''
add_df['Long'] = ''

for index, row in add_df.iterrows():
    g = geocoder.osm(row['Full Address'])
    row['Lat'] = g.lat
    row['Long'] = g.lng

add_df.to_csv(r'C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project_20181117\brooklyn_addresses_for_project_test.csv')

arcpy.management.MakeXYEventLayer(
    'F:\Python Class\brooklyn_addresses_for_project_test.csv',
    'Long',
    'Lat',
    'latlong_plot',
)

arcpy.management.CopyFeatures(
    'latlong_plot',
    'address_pts.shp',
)