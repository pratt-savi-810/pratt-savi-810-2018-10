# Toronto Bikeshare Route Analysis

## Pratt SAVI-810 Final Project
*by: Paul Jarymowycz*
<br/><br/>

### Overview
Bikeshare systems are becoming increasingly popular in many major cities worldwide. It provides a convenient and inexpensive mode of short-distance travel in an urban environment.

The bikeshare model is often structured as a point-to-point system. A rider picks-up a bicycle at a bikestand and has a limited amount of time to return it to another bikestand within the network. The bikestand locations are not fixed - they generally do not vary widely on a daily basis, but may be added or removed unexpectedly due to traffic issues, seasonal weather changes, etc.

This project was created to generate a route for an individual desiring to use the [Bike Share Toronto](https://bikesharetoronto.com/) network. It takes user-defined coordinates of stops in the city, finds the nearest bikestands, and outputs text directions and a map of a suggested route.

### How to Use
**CAUTION - To be safe, copy all necessary files into a new directory.<br/> The script performs some directory deletion within the assigned parent directory, so data loss may occur if not run from a fresh folder.**

*This program was written in Python 2.7 and relies on ArcGIS Desktop 10.6 with the Network Analyst extension. It uses some Network Analyst functions (specifically	`CreateNetworkDatasetFromTemplate_na()`	) that were introduced in this version of ArcGIS Desktop.*

#### Procedure

- Create new directory for program files
- Copy required files to new directory
	- `Bikeshare_Functions.py`
	- `Bikeshare_Run.py`
	- `Bikeshare_ND_template.xml`
	- `Bikeshare_Route.mxd`
	- `OpenStreetMap.lyr`
	- `config1.json`, `config2.json`, `config3.json`, `config4.json`
		- template config files
- Edit config.json files
	- in `directories -> project_dir`
		- type directory path of downloaded files
	- in `directories -> save_dir`
		- type directory path of where to save maps and directions
	- in `locations -> pt_#`
		- add longitude and latitude values for points along trip
	- save config.json files
- Open `Bikeshare_Run.py` in Python editor (or text editor)
	- type desired config file name into functions
		- ie. `Bf.run_bikeshare_route('config4.json')`
- Run `Bikeshare_Run.py`
	- Ensure Python 2.x environment interpreter includes ArcGIS Desktop 10.6 with Network Analyst functionality
		- Dependencies:<br/>
		```Python
		import arcpy
		import json
		import urllib
		import urllib2
		import pandas as pd
		import shutil
		import os
		import zipfile
		```
	- When code finishes running, there will be a map and text directions in your indicated save directory

### Code Outline

- Read `config.json`
	- set parameter variables from config data
- Clear old data and recreate directory structure
	- as currently written, this function deletes any directory named "Data" within the code parent directory, ie. `C:/Bikeshare/Data`<br/>
	- to be safe, ensure no directory named "Data" exists within the parent code directory, otherwise unintentional data loss may occur

```Python
gdb_dir = project_dir + r'/Data'

def clear_data_dir(gdb_dir, shapefile_dir, save_dir):
    # delete data directory
    shutil.rmtree(gdb_dir, ignore_errors=True)

    # create empty directories for geodatabase and shapefiles
    os.mkdir(gdb_dir)
    os.mkdir(shapefile_dir)

    # check if save directory exists, and create, if not
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print('Directory Clear and Refresh Complete!')

```

- Set-up ArcGIS environment
	- create geodatabase and set spatial reference
- Import data
	- using `pandas` library, create csv of bikeshare station locations
		- [Toronto Bike Share Data](https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#84045f23-7465-0892-8889-7b6f91049b29)
	- create points layer of bikeshare locations
	- download and unzip Toronto bikeways shapefile
		- [Toronto Bikeways](https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#62a5e0cf-690e-1a8a-e8c3-81696c6f7cc9)
	- select only valid bike routes from bikeways shapefile
	- export data to bikeshare featureset in geodatabase
- Prepare features for network dataset
	- snap bikeshare points to bike route network
	- clip route at station points
		- ensure points are at line segment endpoints (required for Network Analyst)
	- add length and travel time fields to each line segment in bike routes feature
		- time was calculated based on average travel speed assumptions from [here](https://en.wikipedia.org/wiki/Bicycle_performance)
			- street speed: 10 km/h = 2.8 m/s
			- bike path speed: 20 km/h = 5.6 m/s
- Find nearest stations to indicated travel points
	- perform near analysis from each travel point to the nearest bikeshare station
	- generate circular buffer around each travel point with the near distance
	- intersect buffer layer with bikeshare stations layer
	- export near stations layer for use in Network Analyst
- Build and solve network dataset
	- create network dataset based on parameters in template file (pre-generated)
	- build network dataset
	- create a route analysis layer for lowest travel time
	- add stop locations (near stations) to network dataset
	- solve route analysis
	- export solved route as a feature
- Export directions and map
	- export directions as text file
	- update data connections in template mxd file
		- zoom map to route features
		- update basemap
	- export map as image
