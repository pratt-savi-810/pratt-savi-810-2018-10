# Course Projects

Objective: Use DEM files from visualize NJ with 3D Elevation. Find a biking route between 2 locations. Create a flythrough to preview your route in 3D

Inputs

10m resolution DEMs for each Watershed: https://www.nj.gov/dep/gis/wmalattice.html

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma01lat.zip 

NJ Street Network: https://www.state.nj.us/transportation/gis/zip/NJ_Roads_shp.zip

http://njogis-newjersey.opendata.arcgis.com/

Note: There is a DEM for all of NJ, but will proceed with data broken out by watershed for the sake of practice. (Practice: DL multiple datasets using a loops, loading serveral datasets into Pro). 



Output

A web map of New Jersey uploaded to ArcOnline, Fly through of a given route



Steps

Download the DEM for each Watershed. Create a list of URLs to download, one for each WMA (there are 20). The URL is the same for each one except for its WMA ID number (eg. wma01, wma02,...wma20). Use an if statement so those less than 10 have a leading zero.
```
import urllib

url_list = []

for i in range(1,20):
   if i < 10:
       url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma0"+str(i)+"lat.zip")
   else:
       url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma"+str(i)+"lat.zip")
       
filename_list = []

your_local_drive = "C:/Users/bagta/Documents/810 Project Data/" #substitute with your project folder

for i in range(1,20):
     if i < 10:
         filename_list.append(
	 str(your_local_drive)+"wma0"+str(i)+".zip")
     else:  
         filename_list.append(
         str(your_local_drive)+"wma"+str(i)+".zip")

for url_item, filename_item in zip(url_list, filename_list): 
    urllib.urlretrieve(url_item, filename_item)


```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Extract to a specified location 

Download the NJ Street Network shapefile

```
urllib.urlretrieve(
"https://www.state.nj.us/transportation/gis/zip/NJ_Roads_shp.zip", 
str(your_local_drive) + "NJroads.zip
)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set each WMA raster to an object name in the following scheme: WMA{ID number}

Go through steps to extrude elevation values to create a 3D surface 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New Local Scene

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add Data to ArcGIS Pro (Add Elevation Surfaces)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Use a for loop to add all 20 watersheds? or add all files in a specified folder?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Choose a Base Map (parameter. set a Topographic as the default basemap)

Find a biking route between 2 locations using the ArcGIS Network Analyst extension

Create a fly-through visualization to preview the route with elevation in mind 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; info: https://pro.arcgis.com/en/pro-app/help/mapping/animation/animate-the-camera.htm
	
	
