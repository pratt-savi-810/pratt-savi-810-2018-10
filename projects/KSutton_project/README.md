# Street Tree Corridor Analysis
This tool can be used to generate an analysis of the street trees on any particular street. A trend in street tree planning is to generate
a corridor plan, which sets out species and design recommendations for the major roads
in a city. This tool can and provide charts and graphs that would be useful to foresters and
community groups in deciding what species is best to plant on a particular street.

This project was driven by a request made by the Broadway Malls Association during
my internship in the Forestry Division at the NYC Department of Parks and Recreation.
This Broadway Malls Association is a community group that manages the plantings in the
medians on Broadway in Manhattan. They wanted some assistance from the Parks Department in analyzing
their existing plantings and getting some recommendations about what to plant in the future.

Though developed for Broadway, this tool can be used for any corridor in New York City.

## Data Inputs
#### Parameters
	* tree_data: tree point data from any city
		- ideally this data should have fields for Diameter at
		  Breast Height (DBH), and tree health
	* corridor: the street in question
	* corridor_extent
		- The distance around the corridor that determines which
			tree points to grab. Can be a boundary shapefile, as
			I use here, or a number of feet to make a buffer
			around the corridor.
	* segment_cross_streets: The cross streets used to break the
		corridor into segments


#### Inputs for this project
	* display_data: Forestry treepoints (available in NYC Open Data)
	* corridor: Broadway (in Manhattan)
	* corridor_extent: Broadway malls shapefile
	* segment_cross_streets:
		60th-110th, 110th-122nd, 125th to 155th, 155th-168th


## Steps

#### Data Cleaning
    - Grab Forestry Treepoints from NYC Open Data
    - Decode the Lat Long

#### Existing Plantings
function: **display_existing_plantings**
    - intersect point_data with corridor_extent
    - make visualizations of the whole corridor using matplotlib
    	- bar graphs of most common species
    	- histogram of DBH
    	- histogram of tree health
    - export csv of entire corridor
    - split the broadway malls shapefile into separate shapefiles based on the cross streets
    - select only the trees within one segment
    - make same visualizations for that segment
    - export a csv for that segment
    - export an image for that segment
    - add the extent of that export to the overview map
    - iterate for the rest of the segments
    - export the overview map


#### Species Recommendations
