
import arcpy
import urllib.request
import os


os.getcwd()

arcpy.env.workspace = "c:/data"

## census tracts
## download data using SODA API format (geojson)
urllib.request.urlretrieve('https://data.cityofnewyork.us/resource/i69b-3rdj.geojson?$limit=4000','test.geojson')
## convert downloaded file to shapefile
arcpy.JSONToFeatures_conversion('test.geojson', os.path.join('test.shp'))

## 311 complaints
## download data using SODA API format (geojson)
urllib.request.urlretrieve(
    "https://data.cityofnewyork.us/resource/fhrw-4uyv.geojson?$limit=5000&$where=complaint_type%20like%20%27%25HEAT%25%27",
    'test2.geojson'
    )
arcpy.JSONToFeatures_conversion('test2.geojson', os.path.join('test2.shp'), 'POINT')

arcpy.SpatialJoin_analysis("test", "test2","in_memory/points_SpatialJoin")

## arcpy.SpatialJoin_analysis("test2", "test","in_memory/points_SpatialJoin2", "JOIN_ONE_TO_MANY", "KEEP_ALL", "", "INTERSECT")


url_points = "https://data.cityofnewyork.us/resource/fhrw-4uyv.geojson?$limit=5000&$where=complaint_type%20like%20%27%25HEAT%25%27"
url_poly = 'https://data.cityofnewyork.us/resource/i69b-3rdj.geojson?$limit=4000'

def count_points_in_poly(url_points, url_poly):
    urllib.request.urlretrieve(
        url_points,
        'points.geojson'
    )
    arcpy.JSONToFeatures_conversion('points.geojson', os.path.join('points.shp'), 'POINT')

    urllib.request.urlretrieve(url_poly,'poly.geojson')
    ## convert downloaded file to shapefile
    arcpy.JSONToFeatures_conversion('poly.geojson', os.path.join('poly.shp'))

    arcpy.SpatialJoin_analysis("poly", "points", "in_memory/points_SpatialJoin")
    arcpy.Delete_management('poly')
    arcpy.Delete_management('points')



count_points_in_poly(url_points, url_poly)

aprx = arcpy.mp.ArcGISProject("CURRENT")





















