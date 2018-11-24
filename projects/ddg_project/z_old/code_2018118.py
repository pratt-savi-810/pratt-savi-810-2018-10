import arcpy
import json


def read_config(config_json):
    with open(config_json) as f:
        data = json.load(f)
    return data

# Map points from geocoded csv file

arcpy.management.XYTableToPoint(r"C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project_20181117\tables\brooklyn_addresses_for_project_geo.csv", r"C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project_20181117\shapefiles\address_pts.shp", "Lng", "Lat", None, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

# Import MapPLUTO layer (from local drive) into current map

lyrTest = r"F:\Python Class\bk_mappluto\BKMapPLUTO.shp"
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps("Map")[0]
aprxMap.addDataFromPath(lyrTest)

# Select (by location) the MapPLUTO lots that intersect with the address points

arcpy.management.SelectLayerByLocation('BKMapPLUTO', "INTERSECT", 'address_pts', None, "NEW_SELECTION")

# Export the selected MapPLUTO lots to a new shapefile

arcpy.management.CopyFeatures("BKMapPLUTO", r"C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project_20181117\shapefiles\selected_lots.shp", None, None, None, None)

# Make Table View of curated table of selected MapPLUTO lots 

arcpy.management.MakeTableView('selected_lots', "selected_lots_view", None, r"C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project_20181117\tables", "FID FID HIDDEN NONE;Shape Shape HIDDEN NONE;Borough Borough VISIBLE NONE;Block Block VISIBLE NONE;Lot Lot VISIBLE NONE;CD CD VISIBLE NONE;CT2010 CT2010 VISIBLE NONE;CB2010 CB2010 HIDDEN NONE;SchoolDist SchoolDist HIDDEN NONE;Council Council HIDDEN NONE;ZipCode ZipCode VISIBLE NONE;FireComp FireComp HIDDEN NONE;PolicePrct PolicePrct HIDDEN NONE;HealthCent HealthCent HIDDEN NONE;HealthArea HealthArea HIDDEN NONE;SanitBoro SanitBoro HIDDEN NONE;SanitDistr SanitDistr HIDDEN NONE;SanitSub SanitSub HIDDEN NONE;Address Address VISIBLE NONE;ZoneDist1 ZoneDist1 HIDDEN NONE;ZoneDist2 ZoneDist2 HIDDEN NONE;ZoneDist3 ZoneDist3 HIDDEN NONE;ZoneDist4 ZoneDist4 HIDDEN NONE;Overlay1 Overlay1 HIDDEN NONE;Overlay2 Overlay2 HIDDEN NONE;SPDist1 SPDist1 HIDDEN NONE;SPDist2 SPDist2 HIDDEN NONE;SPDist3 SPDist3 HIDDEN NONE;LtdHeight LtdHeight HIDDEN NONE;SplitZone SplitZone HIDDEN NONE;BldgClass BldgClass HIDDEN NONE;LandUse LandUse VISIBLE NONE;Easements Easements HIDDEN NONE;OwnerType OwnerType VISIBLE NONE;OwnerName OwnerName VISIBLE NONE;LotArea LotArea HIDDEN NONE;BldgArea BldgArea HIDDEN NONE;ComArea ComArea HIDDEN NONE;ResArea ResArea HIDDEN NONE;OfficeArea OfficeArea HIDDEN NONE;RetailArea RetailArea HIDDEN NONE;GarageArea GarageArea HIDDEN NONE;StrgeArea StrgeArea HIDDEN NONE;FactryArea FactryArea HIDDEN NONE;OtherArea OtherArea HIDDEN NONE;AreaSource AreaSource HIDDEN NONE;NumBldgs NumBldgs VISIBLE NONE;NumFloors NumFloors VISIBLE NONE;UnitsRes UnitsRes VISIBLE NONE;UnitsTotal UnitsTotal VISIBLE NONE;LotFront LotFront HIDDEN NONE;LotDepth LotDepth HIDDEN NONE;BldgFront BldgFront HIDDEN NONE;BldgDepth BldgDepth HIDDEN NONE;Ext Ext HIDDEN NONE;ProxCode ProxCode HIDDEN NONE;IrrLotCode IrrLotCode HIDDEN NONE;LotType LotType HIDDEN NONE;BsmtCode BsmtCode HIDDEN NONE;AssessLand AssessLand HIDDEN NONE;AssessTot AssessTot HIDDEN NONE;ExemptLand ExemptLand HIDDEN NONE;ExemptTot ExemptTot HIDDEN NONE;YearBuilt YearBuilt VISIBLE NONE;YearAlter1 YearAlter1 HIDDEN NONE;YearAlter2 YearAlter2 HIDDEN NONE;HistDist HistDist VISIBLE NONE;Landmark Landmark VISIBLE NONE;BuiltFAR BuiltFAR VISIBLE NONE;ResidFAR ResidFAR VISIBLE NONE;CommFAR CommFAR VISIBLE NONE;FacilFAR FacilFAR VISIBLE NONE;BoroCode BoroCode HIDDEN NONE;BBL BBL VISIBLE NONE;CondoNo CondoNo VISIBLE NONE;Tract2010 Tract2010 HIDDEN NONE;XCoord XCoord HIDDEN NONE;YCoord YCoord HIDDEN NONE;ZoneMap ZoneMap HIDDEN NONE;ZMCode ZMCode HIDDEN NONE;Sanborn Sanborn HIDDEN NONE;TaxMap TaxMap HIDDEN NONE;EDesigNum EDesigNum HIDDEN NONE;APPBBL APPBBL HIDDEN NONE;APPDate APPDate HIDDEN NONE;PLUTOMapID PLUTOMapID HIDDEN NONE;FIRM07_FLA FIRM07_FLA HIDDEN NONE;PFIRM15_FL PFIRM15_FL HIDDEN NONE;Version Version HIDDEN NONE;MAPPLUTO_F MAPPLUTO_F HIDDEN NONE;SHAPE_area SHAPE_area HIDDEN NONE;SHAPE_len SHAPE_len HIDDEN NONE")

# Export the curated table of the selected MapPLUTO lots to a csv

arcpy.management.CopyRows("selected_lots_view", r"C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project_20181117\tables\curated_lots.csv", None)