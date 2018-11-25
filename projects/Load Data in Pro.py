#  do the following after opening a ArcGIS Pro Project & adding a local scene
# This should be done in the Analysis > Python window to properly reference "Current"

#  Each DEM layers should have been extracted to a path like the following:
#  "C:/Users/bagta/Documents/810 Project/" (your project folder) + "wma01/wma01lat"
#  Use addDataFromPath to add layers like so:
#  map1.addDataFromPath(r'C:\Users\bagta\Documents\810 Project\wma01\wma01lat')
#  Use a for loop to ease loading

import arcpy.mp

aprx = arcpy.mp.ArcGISProject("Current")

map1 = aprx.activeMap

project_data_folder = r"C:\Users\bagta\Documents\810 Project"

for i in range(1, 21):
    if i < 10:
        map1.addDataFromPath(project_data_folder + "\wma0" + str(i) + "\wma0" +str(i) + "lat")
    else:
        map1.addDataFromPath(project_data_folder + "\wma" + str(i) + "\wma" + str(i) + "lat")

