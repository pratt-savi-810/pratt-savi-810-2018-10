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

	In working with planners at my job, we are often handed a list of addresses (e.g., a list of no-build projects) and asked to map them, thus creating both a shapefile and an accompanying table of data. It would be helpful to have both point and polygon data, as well as a "curated" table (one with only select fields, which the planners will need), in as few steps as possible.

	This work attempts to use a csv file with a list of geocoded addresses, bring them into ArcGIS Pro, plot them,then use those plots to "grab" the associated lots (from NYC's MapPLUTO data). In the end, the goal is to have an address points shapefile, a selected MapPLUTO lots shapefile, and a curated csv file with only selected fields from the selected MapPLUTO lots data.

	In further work on this project, I hope to be able to use python to geocode the addresses at the start.

## Project Outline

	*this entire process, ideally, would happen in ArcGIS Pro, with a map active*

	receive list of (nyc-based) addresses
		(e.g., list of no-build projects; list of historic landmarks, etc.)
		* make sure the address is properly formatted in a column
			- "full address" = street number + street, city, state
		* for initial purposes of this project, geocoding will already be present in csv

	<!-- geocode addresses (lng,lat)
		* NYC Geoclient(?)
		* Geocoder(?) -->

	plot geocoded addresses to map
		* arcpy.management.XYTableToPoint
			- create shapefile ('address_pts.shp')

	add MapPLUTO data to map

	select MapPLUTO lots that intersect with the address points ('address_pts.shp')
		* arcpy.management.SelectLayerByLocation

	export selected MapPLUTO lots to a shapefile ('selected_lots.shp')
		* arcpy.management.CopyFeatures

	make a curated table view of selected MapPLUTO lots with only select fields visible
		* arcpy.management.MakeTableView

	export curated table view selected MapPLUTO lots to a csv ('selected_lots.csv')
		* arcpy.management.CopyRows

## Questions Remaining

	* geocoding addresses within python (could not get geocoder to work as of yet)

