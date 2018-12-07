# Street Tree Corridor Analysis
A trend in street tree planning is to make
a corridor plan, which sets out species and design recommendations for the major roads
in a city. This tool can be used to generate an analysis of the street trees on any particular street in New York City using the Forestry Treepoints dataset from NYC Open Data. One challenge posed by the Forestry Treepoints dataset used by NYC Parks is that it cannot be filtered based on the street name or any other location data. This tool isolates the street trees on the selected corridor within a specified range. Tree corridors are usually analyzed by segment (eg. 59th St to 110th St). Using this tool, users can choose to split the corridor up using either NYC Community Districts or Neighborhood Tabulation Areas. A unique shapefile is then created for the street trees in each segment of the corridor. This data could be further analyzed using matplotlib and pandas to recommend which species are best to plant on each section of the corridor.


This project was driven by a request made by the Broadway Malls Association during
my internship in the Forestry Division at the NYC Department of Parks and Recreation.
This Broadway Malls Association is a community group that manages the plantings in the
medians on Broadway in Manhattan. They wanted some assistance from the Parks Department in analyzing
their existing plantings and getting some recommendations about which tree species to plant in the future.

Though developed for Broadway, this tool can be used for any corridor in New York City.

Here is a (video)[https://www.dropbox.com/s/ptwv3nzppuegr52/SAVI810_FinalProject_StreetTree_Corridor_Analysis.fbr?dl=0
] of the tool executing on my computer.
## Dependencies
	import urllib
	import pandas as pd
	import arcpy
	import arcpy.mapping
	from arcpy import env
	import zipfile

## Data Inputs
#### Parameters
* corridor: the name of the corridor
	- a string with the name of any road in NYC
	- should match the street name listed in the FULL_STREE column of the DOT centerline dataset
* borocode: the borough in which the corridor is located
	- this helps identify the correct corridor since some roads in NYC share the same name
	- should match the value of LBoro in the DOT centerline dataset
* buffer_distance
	- The size of the buffer around the corridor that is used to capture the trees along the corridor
	- 40 feet is a good standard, but some corridors may require a larger or smaller buffer to capture all of its street trees
* district_type:
	- the geographic extent that will be
	  used to split the corridor into segments for analysis
	- choose community districts ('CD') or neighborhood tabulation areas ('NTA'), depending on the size of the segment that you prefer
* district_numbers: a list of which districts you want to analyze
	- from the CD or NTA file, make a list of the districts you are interested in analyzing as segments on the corridor
	- each value matches the column BoroCD or BoroNTA

#### Inputs for this project
	* corridor: 'BROADWAY'
	* borocode: '01' (i.e. Manhattan)
	* buffer_distance: '40 feet'
	* district_type: 'CD'
	* district_numbers: (112, 109, 107)


## Project Outline
- downloading files:
	- all files are downloaded directly from NYC Open Data
	- this ensures that all data is the most current version, particularly useful for the treepoints dataset which is updated weekly
	- first download centerline, unzip, add to map
- function: export_the_corridor
	- selects and exports the relevant corridor from the centerline shapefile
- add the corridor to the map
- function: buffer_the_corridor
	- creates a buffer of the specified distance around the entire corridor
- add the entire corridor buffer to the map
- download and unzip the relevant district file (CD or NTA)
- add it to the map
- function: extract_districts
	- selects and exports each of the relevant CDs or NTAs that are used to split the corridor into segments for analysis
- function: clip_the_buffer
	- clips the buffer of the entire corridor to the extent of each of the relevant districts
	- this creates, for example, a polygon shapefile of a 40 foot buffer surrounding Broadway in Community District 7 in Manhattan
	- returns a list of the clipped buffer segments
- download the treepoints file
- separate the Lat and Long into their own columns
- display xy event data for the entire treepoints dataset
- copy those features into a layer and add it to the map
- function: intersect_trees_and_segments
	- intersects the treepoints file with each of the segments of the corridor
	- returns a list of treepoint files showing only the trees in each segment
