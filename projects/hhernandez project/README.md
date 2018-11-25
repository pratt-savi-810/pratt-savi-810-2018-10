Mapping New York City Major Bridges & Crossings
================================================
Dependencies
--------------
Import arcpy
Import json

Project Description
---------------------
NYCDOT creates annual NYC Bridge Traffic Volumes and Manhattan Crossings Reports. Both are publicly available. Within these reports there are maps that display 24 hour bi-directional (In & Out) traffic volumes for sets of NYC major bridges/crossings. I would like to recreate these maps and automate the process to create them using Python. Before writing Python code, the first step was to prepare a csv file of these sets of bridges/crossings. Once the csv file was created with the crossings, each crossing record was geocoded with the longitude and latitude coordinates. For this project, I am only using ten crossing records and these can be grouped in three sets. These three crossing sets are the East River Bridges, the Manhattan - New Jersey Crossings, and the Staten Island - New Jersey Crossings. The final product from the Python code will be one exported map for each crossings’ set, 3 exported maps total.
Code includes the files *run_bridge_export.py*, *bridge_export.py*, and *config.json* can be found at: (https://github.com/pratt-savi-810/pratt-savi-810-2018-10/tree/hhernandez_project/projects/hhernandez%20project)
Video of running code can be found at: (https://s3.amazonaws.com/img0.recordit.co/WiUlzKR1Ga.mp4?AWSAccessKeyId=AKIAINSRFOQXTN4DT46A&Expires=1543090794&Signature=5vqZ7XAA0z9%2Bf4NnepVZ4AyJVjo%3D)
mp4 of the video also in the github link above


Project Outline/Pseudocode
----------------------------
'''Create function to read JSON file
	Return path of csv file with coordinates

Store csv file path in variable

Project xy coordinates from csv file and save in memory

Create a shapefile from projected xy coordinates
	Save shapefile in location that is read from JSON 

Read JSON for location of basemap
	Get mxd document with basemap
Load shapefile in Arcmap document with basemap
Save shapefile as layer in Arcmap

Turn labels on for defined layer and show labels on map

Create a for loop that runs through a list of different map feature sets and performs the following
	Select first set of features
	Zoom to those selected features
	Export a png file
	Declare variable of location to save export and a save

Repeat loop for additional two map features sets'''


Sources of code
-----------------
Labeling layer code: (https://community.esri.com/thread/197931-how-to-label-features-using-arcpy)

Loading shapefile code: (https://community.esri.com/thread/47916)

All other code: 810 Intro to Python In class exercises
