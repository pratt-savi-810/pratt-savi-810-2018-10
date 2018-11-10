import arcpy


 # display_data: Forestry treepoints (available in NYC Open Data)
	# * corridor: Broadway (in Manhattan)
	# * corridor_extent: Broadway malls shapefile
	# * segment_cross_streets:
	# 	60th-110th, 110th-122nd, 125th to 155th, 155th-168th
	# * DBH_field: 'DBH'
	# * Health_field: 'Condition'
    #
trees =  'https://data.cityofnewyork.us/resource/k5ta-2trh.json'

def existing_plantings (
        corridor,
        corridor_extent,
        segment_cross_streets,
        mxd_name,
):




# ## Steps
#
# #### Data Cleaning
#     - Grab Forestry Treepoints from NYC Open Data
#     - Decode the Lat Long
#
# #### Existing Plantings
# function: **display_existing_plantings**
#     - intersect point_data with corridor_extent
#     - make visualizations of the whole corridor using matplotlib
#     	- bar graphs of most common species
#     	- histogram of DBH
#     	- histogram of tree health
#     - export csv of entire corridor
#     - split the broadway malls shapefile into separate shapefiles based on the cross streets
#     - select only the trees within one segment
#     - make same visualizations for that segment
#     - export a csv for that segment
#     - export an image for that segment
#     - add the extent of that export to the overview map
#     - iterate for the rest of the segments
#     - export the overview map