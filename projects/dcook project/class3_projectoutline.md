# Project Description
I have been volunteering with some advocacy groups that focus on issues such as housing, social vulnerability, and resilience. At the same time, I have wanted to work on 311 data. Awhile ago I also looked into some things that were tied to a study known as the "Heat Vulnerability Index." With winter coming up, I thought it would be cool to look at 311 heating complaints from last winter.  I hope to combine this data with demographic data (population, poverty, etc.) and other contextual considerations as a way to identify what locations might have high numbers of people (tenants) who are particularly vulnerable to inadequate heating during this upcoming winter. This sort of analysis might be of interest to advocates who are doing policy campaigns or mutual aid efforts.

# Project Outline

## obtain 311 data, querying as desired (see below)
* type: heating; timeframe: winter of 2017; can use urllib or nyc open data can be queried like below:
`https://data.cityofnewyork.us/resource/fhrw-4uyv.geojson?$where=complaint_type like '%25HEAT%25' and created_date between '2017-11-01' and '2018-3-21'`

## aggregate in a meaningful way to compare with other data
* obtain census tract data
`https://data.cityofnewyork.us/City-Government/2010-Census-Tracts/fxpq-c8ku`
* count 311 complaint points within census tracts
`https://pro.arcgis.com/en/pro-app/tool-reference/big-data-analytics/summarize-within.htm`
`arcpy.geoanalytics.SummarizeWithin(311points,census_tracts)`

## normalize complaint data in a meaningful way 
* using census tract-level data
* such as population, 
* or population of residents who rent their household,
* or housing units that are rented
`df['normalized_field'] = df['311points_count'] / df['tract_population']`

## check against other data such as poverty metrics available at census tract-level
* could be other census data such as percentage living below poverty
* or could be other metrics or indices such as the social vulnerability index
* matt also suggests looking at nys dec environmental justice standards/identifications

## rank, identify most severe areas
* could come up with an new score/index/rank such as ((complaints/renters)*sovi)
`df['severity_score'] = df['normalized_field'] * df['sovi_score']`

## produce maps of most severe areas
* top 5, top 10, etc.
* have area of interest for each map correspond to
  * tracts, or higher aggregations such as NTAs
* if time, make primary features displayed on maps
  * lots/foot prints which approximate complaint location
  * (also acquire mappluto or bldg footprints)
  * symbolized according to number of complaints
  * (aggregate/count complaints within lot or footprint extents)
```
for i in top_5:
   arcpy.SelectLayerByAttribute_management(...)
   map_df.zoomToSelectedFeatures()
   arcpy.SelectLayerByAttribute_management(fc,"CLEAR_SELECTION")
   arcpy.mapping.ExportToPNG(mxd, '{}_{}.png'.format(output_png_dir,i))
```

## expected dependencies
```
arcpy
pandas
```




