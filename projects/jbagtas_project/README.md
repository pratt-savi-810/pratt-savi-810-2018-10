# Project Documentation

Objective: Use DEM files from visualize NJ with 3D Elevation. Create a flythrough 

## Inputs

10m resolution DEMs for each Watershed: https://www.nj.gov/dep/gis/wmalattice.html

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma01lat.zip 


http://njogis-newjersey.opendata.arcgis.com/

Note: There is a DEM for all of NJ, but will proceed with data broken out by watershed for the sake of practice. (Practice: DL multiple datasets using a loops, loading serveral datasets into Pro). 



## Output

A fly through of a NJ state elevation



## Steps - (Utilize Python 3.x)

### Downloading the Data
1. To download the DEM for each watershed management area (WMA), first start by creating a list of URLs to download, one for each WMA (there are 20).  
    * The URL is the same for each watershed except for its WMA ID# (eg. wma01, wma02,...wma20). 
    * Use an if statement so those less than 10 have a leading zero.
    * Also download the NJ road networks shp file 
    * Utilize [DownloadData.py](DownloadData.py) to accomplish this

    Excerpt from [DownloadData.py](DownloadData.py)
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
2. Extract to a specified location 
    
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
    
    * ![InsertScene](Screenshot%20References/InsertScene.png)
    * Once the scene has loaded, make it a local scene: View > Local
    * ![LocalSceneView](Screenshot%20References/LocalSceneView.png)

2. Open the Python Window and use [Load Data in Pro.py](Load%20Data%20in%20Pro.py) to easily load all 20 layers into the Scene
    * Uses ```arcpy.mp``` library, ```addDataFromPath()```, and a for loop
    * Each DEM layer should have been extracted to a path like the following:
        * "C:/Users/bagta/Documents/810 Project/wma01/wma01lat" 
        * Thus the for loop in the excerpt below:
        
    ```
    project_data_folder = r"C:\Users\bagta\Documents\810 Project"
    
    for i in range(1, 21):
        if i < 10:
            map1.addDataFromPath(project_data_folder + "\wma0" + str(i) + "\wma0" +str(i) + "lat")
        else:
            map1.addDataFromPath(project_data_folder + "\wma" + str(i) + "\wma" + str(i) + "lat")
    ```
3. Use [TransformRasters.py](TransformRasters.py) to combine all 20 DEM layers into 1 raster layer (```njdem```).
    * Easier to use a single raster rather than 20 as a 3D Elevation Surface
    * Uses ```arcpy.management.MosaicToNewRaster()```
    * The output should be added to the Scene
    * Help Documentation: https://pro.arcgis.com/en/pro-app/tool-reference/data-management/mosaic-to-new-raster.htm
4. Create hillshading with ```arcpy.ddd.HillShade()``` (code is in the same .py file as step 3)
    * The output should be added to the Scene
    * Help documentation for hillshading: https://pro.arcgis.com/en/pro-app/tool-reference/3d-analyst/hillshade.htm

5. Remove the 20 DEM layers from the Scene as they are no longer needed

6. Set ```njdem``` as the elevation surface. Start by right-clicking on the Map in Contents to edit the Map Properties
    * ![MapProperties](Screenshot%20References/MapProperties.png)
    * Properties > Elevation Surface > Elevation Sources > Add Elevation Source, choose ```njdem```
    * Set the exaggeration to around 15-20 to see elevation better
    * Click OK
    * Go back to the Elevation Source in properties to check if the Elevation Source from ArcOnline was automatically added. This is not necessary and may use credits, so click the X to remove it
    * ![DeleteArcOnlineElevationSource](Screenshot%20References/DeleteArcOnlineElevationSource.png)
    
 7. Change Symbology/Appearance to improve 3D visuals:
    * Set Hillshade (```hillshd```) transparancy to ~ 50%
    * Set ```njdem``` color scheme to "Condition Numbers" (low elevation = green, high elevation = red)
 
 8. Navigate through the 3D visualization by holding the V key and and dragging. Drag with either left-click or scroll wheel to view at different angles
    
 9. Create a fly-through visualization
    * View > Animation >  Add Animation
    * Go to the Keyframe timeline to add a key frame
    * Navigate to a key frame (a location where the "camera" will go place to place) and Choose "Append" to the animation
    * Use "Fixed" transitions (choice of Fixed, Linear, Hop, etc) and Check off "Maintain Speed"
    * ![KeyFrameTimeline](Screenshot%20References/KeyFrameTimeline.png)
    * [Help Documenation for Creating Flythrough Animations](https://pro.arcgis.com/en/pro-app/help/mapping/animation/animate-the-camera.htm#ESRI_SECTION1_0F98E1F2D6754A019D945D005225375F) 

## Final Output
![3D_flythrough](Video_Gifs/3D_flythrough.gif)

[Videos of Code Working Successfully](jbagtas_project/Videos_Gifs)
