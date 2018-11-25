# Project Description
I have been volunteering with some advocacy groups that focus on issues such as housing, social vulnerability, and resilience. At the same time, I have wanted to work on 311 data. With winter coming up, I thought it would be cool to look at 311 heating complaints from last winter. While attempting to do some explorations and analyses for this, I found myself wanting to make some code that helps automates one or more of the major steps involved.

# Project Outline

## dependencies
```
import arcpy
import urllib.request
import os
```

## obtain point data using web API in geojson format, querying as desired (see below)
* type: 311 heating complaints from NYC Open Data portal; timeframe: winter of 2017
```
url_points = "https://data.cityofnewyork.us/resource/fhrw-4uyv.geojson?$limit=5000&$where=complaint_type%20like%20%27%25HEAT%25%27"
urllib.request.urlretrieve(
        url_points,
        'points.geojson'
    )
```

## obtain polygon data in geojson format
* type: census tract data in NYC
```
url_poly = 'https://data.cityofnewyork.us/resource/i69b-3rdj.geojson?$limit=4000'
urllib.request.urlretrieve(url_poly,'poly.geojson')
```

## convert geojson data into shapefiles
```
arcpy.JSONToFeatures_conversion('points.geojson', os.path.join('points.shp'), 'POINT')
arcpy.JSONToFeatures_conversion('poly.geojson', os.path.join('poly.shp'))
```

## count points within polygons
```
arcpy.SpatialJoin_analysis("poly", "points", "in_memory/points_SpatialJoin")
```
* this creates a new field "join_count" which contains the number of points contained within each polygon, but it also joins columns from the points

## put this code into a function which can be used for different data
```
def count_points_in_poly(url_points, url_poly):
    ...
...
count_points_in_poly(url_points, url_poly)
```

## possible next steps
* clean up the results of the spatial join (remove extraneous columns from points and keep only the "join_count" field)
* automate map producion in some way, such as the top 5 census tracts
* join demographic data by census tracts and use to normalize and perform other analyses




