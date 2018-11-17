I'll be creating a map showing the locations of buildings with stabilized rent
and also show the gross rent as a percent of household income of the population.

Steps:
Extract zip file
Edit field names of file "ACS_16_5YR_B25070"(rent file)
Add a new field to "BKMapPluto" called "BlocLot" the field values will be the the total of the "block" and "lot" fields.
Create the same 'BlocLot' field in "brooklynbldgsRS16"
Join "ACS_16_5YR_B25070" to "BKMapPluto" shapefile using fields "GEOid2" and "BBL"
Join "brooklynbldgsRS16" file to  "BKMapPluto" shapefile using their "BlocLot" fields
Export as new layer
Edit map symbology in ArcMap






