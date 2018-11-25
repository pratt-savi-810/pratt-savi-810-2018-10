# Project Documentation

Objective: Use DEM files from visualize NJ with 3D Elevation. Find a driving route between 2 locations. Create a flythrough to preview your route in 3D

## Inputs

10m resolution DEMs for each Watershed: https://www.nj.gov/dep/gis/wmalattice.html

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma01lat.zip 

NJ Street Network: https://www.state.nj.us/transportation/gis/zip/NJ_Roads_shp.zip

http://njogis-newjersey.opendata.arcgis.com/

Note: There is a DEM for all of NJ, but will proceed with data broken out by watershed for the sake of practice. (Practice: DL multiple datasets using a loops, loading serveral datasets into Pro). 



## Output

A fly through of a given route



## Steps - (Utilize Python 3.x)

### Downloading the Data
1. To download the DEM for each watershed management area (WMA), first start by creating a list of URLs to download, one for each WMA (there are 20).  
    * The URL is the same for each watershed except for its WMA ID# (eg. wma01, wma02,...wma20). 
    * Use an if statement so those less than 10 have a leading zero.
    * Also download the NJ road networks shp file 
    * Utilize [download input data.py](https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/jbagtas_project/projects/download%20input%20data.py) to accomplish this

    Excerpt from [download input data.py](https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/jbagtas_project/projects/download%20input%20data.py)
    ```
    import urllib
    
    #create a list of URLs to download each WMA DEM (WMAs 1 through 20)
    url_list = []
    
    for i in range(1, 21):
        if i < 10:
            url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma0" + str(i) + "lat.zip")
        else:
            url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma" + str(i) + "lat.zip")
    
    ```
    [...]
    ```
    #  download all WMA DEMs to the specified file path (a list called filename_list contains the specified file path for each DEM)
    for url_item, filename_item in zip(url_list, filename_list):
        urllib.urlretrieve(url_item, filename_item)
    ```  
2. Extract to a specified location using [unzip all.py](https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/jbagtas_project/projects/unzip%20all.py)
    
    Exerpt:
    ```
    def unzip_file(zip_file_name, extract_location):
    zip_object = zipfile.ZipFile(zip_file_name, 'r')
    zip_object.extractall(extract_location)


    #  designate the folder where you want to extract the data
    your_project_folder = "C:/Users/jbagtas/Documents/"
    
    #  extract the data
    #  in previous steps the file paths for all .zip files were stored in a list called filename_list
    
    for i in range(len(filename_list)):
        unzip_file(
            filename_list[int(i) - 1],
            your_project_folder
        )
    ```
### Visualizing NJ in 3D in ArcGIS Pro
1. Add a local scene in ArcGIS Pro: 
    * Insert > New Map > New Scene. 
    
    * ![Text](https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/jbagtas_project/projects/Screenshot%20References/InsertScene.png)
    * Once the scene has loaded, make it a local scene: View > Local
    * ![Text](https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/jbagtas_project/projects/Screenshot%20References/LocalSceneView.png)

2. Open the Python Window and use [Load Data in Pro.py](https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/jbagtas_project/projects/Load%20Data%20in%20Pro.py) to easily load all 20 layers into the Scene
    * This utilizes the library ```arcpy.mp``` and ```addDataFromPath()```
3. Use [Mosaic to Raster.py](https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/jbagtas_project/projects/Mosaic%20to%20Raster.py) to combine all 20 DEM layers into 1 raster layer (```njdem```).
    * Having a single raster makes it easier to use as a 3D Elevation Surface
    * Uses ```arcpy.management.MosaicToNewRaster()```
    * Help Documentation: https://pro.arcgis.com/en/pro-app/tool-reference/data-management/mosaic-to-new-raster.htm
4. Remove the 20 DEM layers from the Scene. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Choose a Base Map (parameter. set a Topographic as the default basemap)

Find a biking route between 2 locations using the ArcGIS Network Analyst extension

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; http://pro.arcgis.com/en/pro-app/arcpy/network-analyst/what-is-network-analyst-module.htm
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MakeRouteLayer_na http://pro.arcgis.com/en/pro-app/tool-reference/network-analyst/make-route-layer.htm

Create a fly-through visualization to preview the route with elevation in mind 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; info: https://pro.arcgis.com/en/pro-app/help/mapping/animation/animate-the-camera.htm
	
	
