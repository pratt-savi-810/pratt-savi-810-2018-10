# Project updates

## dependencies
```
import arcpy
import pandas as pd
import urllib.request
import os
```

Using ArcGIS Pro

## obtain 311 data, querying as desired

http://pro.arcgis.com/en/pro-app/tool-reference/conversion/json-to-features.htm
https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/fxpq-c8ku

```
## census tracts
## download data using SODA API format (geojson)
urllib.request.urlretrieve('https://data.cityofnewyork.us/resource/i69b-3rdj.geojson?$limit=4000','test.geojson')
## convert downloaded file to shapefile
arcpy.JSONToFeatures_conversion('test.geojson', os.path.join('test.shp'))
```

```
## 311 complaints
## download data using SODA API format (geojson)
urllib.request.urlretrieve("https://data.cityofnewyork.us/resource/fhrw-4uyv.geojson?$where=complaint_type like '%25HEAT%25'&$limit=200000",'test2.geojson')
arcpy.JSONToFeatures_conversion('test2.geojson', os.path.join('test2.shp'), 'POINT')
```

## aggregate points

```
## doesn't work
arcpy.SummarizeWithin_sfa("test", "test2", 'test3')
```
https://pro.arcgis.com/en/pro-app/tool-reference/feature-analysis/summarize-within.htm

* writing things to disk vs. making things and working with them as event layers or in_memory objects
* encountering unwieldy file sizes… set smaller limit? restrict columns being fetched?
* count point in polygon difficulties
* bad nyc open data census tract ids
* wanting to make it as functional/pythonic as possible