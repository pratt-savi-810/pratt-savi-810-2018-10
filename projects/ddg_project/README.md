# Addresses to Points to MapPLUTO Lots, Oh My

![image placeholder](http://i.imgur.com/KCDPWhM.gif)

## Dependencies

	import arcpy

	config.json
		* stores the following:
			- coordinate system for plotting xy data in ArcGIS Pro
			- filepath for MapPLUTO data on local drive
			- api key (nyc geoclient api)

## Project Description

	[text_to_come]

## Project Outline

	*this entire process, ideally, would happen in ArcGIS Pro, with a map active*

	receive list of (nyc-based) addresses
		(e.g., list of no-build projects; list of historic landmarks, etc.)
		* make sure the address is properly formatted in a column
			- "full address" = street number + street, city, state
				- zip optional    

	geocode addresses (lng,lat)
		* NYC Geoclient(?)
		* Geocoder(?)

	plot geocoded addresses to map
		* arcpy.management.XYTableToPoint
			- create shapefile ('address_pts.shp')

	add MapPLUTO data to map

	select MapPLUTO lots that intersect with the address points ('address_pts.shp')
		* arcpy.management.SelectLayerByLocation

	export selected MapPLUTO lots to a shapefile ('selected_lots.shp')
		* arcpy.management.CopyFeatures

	export selected MapPLUTO lots to a csv ('selected_lots.csv')
		* arcpy.management.CopyRows

## Questions Remaining

	* geocoding addresses within python

	* can I export only selected fields/columns from the MapPLUTO lots csv ('selected_lots.csv')

