
#  Use Mosaic to New Raster to combine all 20 DEM layers into 1 raster layer.
#  This makes it easier to use as a 3D Elevation Surface
#  Help Documentation: https://pro.arcgis.com/en/pro-app/tool-reference/data-management/mosaic-to-new-raster.htm

import arcpy.mp

aprx = arcpy.mp.ArcGISProject("Current")
map1 = aprx.activeMap

project_data_folder = r"C:\Users\bagta\Documents\810 Project"

all_data = "wma01lat;" \
           "wma02lat;" \
           "wma03lat;" \
           "wma04lat;" \
           "wma05lat;" \
           "wma06lat;" \
           "wma07lat;" \
           "wma08lat;" \
           "wma09lat;" \
           "wma10lat;" \
           "wma11lat;" \
           "wma12lat;" \
           "wma13lat;" \
           "wma14lat;" \
           "wma15lat;" \
           "wma16lat;" \
           "wma17lat;" \
           "wma18lat;" \
           "wma19lat;" \
           "wma20lat"


arcpy.management.MosaicToNewRaster(
    all_data,
    project_data_folder,
    "njdem",
    #  the following are simply the same parameters from the original DEM layers, copied from the metadata
    "PROJCS['NAD_1983_StatePlane_New_Jersey_FIPS_2900_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',492125.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-74.5],PARAMETER['Scale_Factor',0.9999],PARAMETER['Latitude_Of_Origin',38.83333333333334],UNIT['Foot_US',0.3048006096012192]]",
    "32_BIT_FLOAT",
    32.8194748234876,
    1,
)

