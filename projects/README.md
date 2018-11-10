# Course Projects

Objective: Use DEM files from NJGIN to Visualize NJ with 3D Elevation. Export to ArcOnline Account. 

Inputs

DEMs for each Watershed: https://www.nj.gov/dep/gis/wmalattice.html

https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma01lat.zip 

http://njogis-newjersey.opendata.arcgis.com/

Note: There is a DEM for all of NJ, but will proceed with data broken out by watershed for the sake of practice. (Practice: DL multimle datasets using a loops, loading serveral datasets into Pro). 



Output

A web map of New Jersey uploaded to ArcOnline



Steps

Download the DEM for each Watershed from https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma[...]lat.zip

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace [...] with the Watershed number: 01, 02, ..., 20

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Because of the leading zero, create a list

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Use a for loop to download all DEMs, watersheds 1 through 20

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Download .zip file to a specified location - parameter 1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Extract to a specified location - parameter 2 (default = same as parameter 1)


Go through steps to extrude elevation values to create a 3D surface (further research may be needed on how to do this with Python)

nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; New Local Scene

nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add Data to ArcGIS Pro (Add Elevation Surfaces)

nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Use a for loop to add all 20 watersheds? or add all files in a specified folder?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Choose a Base Map (parameter, set a default basemap)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 

Share 3D scene to ArcOnline to one's own ArcOnline account or another account specified by the user (parameter)

Share Map to ArcOnline

For further research: Find a biking route between 2 locations, create a fly-through visualization to preview the route with elevation in mind 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; info: https://pro.arcgis.com/en/pro-app/help/mapping/animation/animate-the-camera.htm
	
	
