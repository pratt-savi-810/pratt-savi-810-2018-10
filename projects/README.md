# Course Projects

Objective: Use DEM files, Export to ArcOnline Account. 

Inputs
https://www.nj.gov/dep/gis/wmalattice.html
https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma01lat.zip 

Output
A web map  uploaded to ArcOnline

Steps
Download the DEM for each Watershed from https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma[...]lat.zip
	Replace [...] with the Watershed number
	Use a for loop to download all DEMs, watersheds 1 through 20
	Download .zip file to a specified location - parameter 1
	Extract to a scecified location - parameter 2 (default = same as parameter 1)
Add Data to ArcGIS Pro
	Use a for loop to add all 20 watersheds? or add files in a specified folder?
New Local Scene
Go through Steps to extrude elevation values to create a 3D surface
Share WebScene (to your ArcOnline account)
	
	
