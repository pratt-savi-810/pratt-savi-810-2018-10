
import arcpy
import urllib.request
import os

arcpy.env.workspace = "c:/data"

## download geojson data, convert to shapefiles, join
def count_points_in_poly(url_points, url_poly):
    urllib.request.urlretrieve(
        url_points,
        'points.geojson'
    )
    arcpy.JSONToFeatures_conversion('points.geojson', os.path.join('points.shp'), 'POINT')

    urllib.request.urlretrieve(url_poly,'poly.geojson')
    arcpy.JSONToFeatures_conversion('poly.geojson', os.path.join('poly.shp'))

    arcpy.SpatialJoin_analysis("poly", "points", "in_memory/points_SpatialJoin")
    arcpy.Delete_management('poly')
    arcpy.Delete_management('points')


## 311 complaints from NYC Open Data
url_points = "https://data.cityofnewyork.us/resource/fhrw-4uyv.geojson?$limit=5000&$where=complaint_type%20like%20%27%25HEAT%25%27"
## census tracts from NYC Open Data
url_poly = 'https://data.cityofnewyork.us/resource/i69b-3rdj.geojson?$limit=4000'

count_points_in_poly(url_points, url_poly)





















