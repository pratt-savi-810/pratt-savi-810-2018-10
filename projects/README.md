# Course Projects

Objective: Use DEM files from NJGIN to Visualize NJ with 3D Elevation. Export to ArcOnline Account. 

Inputs
https://www.nj.gov/dep/gis/wmalattice.html
https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma01lat.zip 

Output
A web map of New Jersey uploaded to ArcOnline

Steps


Download the DEM for each Watershed from https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma[...]lat.zip

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace [...] with the Watershed number

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Use a for loop to download all DEMs, watersheds 1 through 20

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Download .zip file to a specified location - parameter 1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Extract to a specified location - parameter 2 (default = same as parameter 1)



Go through steps to extrude elevation values to create a 3D surface (further research may be needed)
nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; New Local Scene

nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add Data to ArcGIS Pro (Add Elevation Surfaces)

nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Use a for loop to add all 20 watersheds? or add all files in a specified folder?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Choose a Base Map (Get User input to Choose which base map?)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 

Share 3D scene to ArcOnline (to one's own ArcOnline account or another account specified by the user)

Share Map to ArcOnline

For further research: take the 3D data to create a web app with JavaScript API
	
	
