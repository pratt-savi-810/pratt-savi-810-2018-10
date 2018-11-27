fc = feature_class


# need to geocode address in csv



# # geocoding via ArcGIS Pro

# arcpy.geocoding.GeocodeAddresses(r"csv_file_location", "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/ArcGIS World Geocoding Service", "'Address or Place' Address VISIBLE NONE;Address2 <None> VISIBLE NONE;Address3 <None> VISIBLE NONE;Neighborhood <None> VISIBLE NONE;City City VISIBLE NONE;Subregion <None> VISIBLE NONE;State State VISIBLE NONE;ZIP <None> VISIBLE NONE;ZIP4 <None> VISIBLE NONE;Country <None> VISIBLE NONE", r"output_fc_location", "STATIC", "US", "ROUTING_LOCATION", None)



# importing xy data from csv (already-geocoded addresses)

arcpy.management.XYTableToPoint("csv_file_location", r"output_fc_location", "Lng", "Lat", None, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

# add MapPLUTO layer to MapPLUTO

lyrTest = r"pluto_feature_class"
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps("Map")[0]
aprxMap.addDataFromPath(lyrTest)

# select by location (selecting MapPluto lots that intersect with the address points)

arcpy.management.SelectLayerByLocation("pluto_feature_class", "INTERSECT", "geocoded_points", None, "NEW_SELECTION")


# exporting selected MapPluto lots to a shapefile or geodatabase

arcpy.management.CopyFeatures("pluto_feature_class", r"output_fc_selected_lots")


# exporting selected MapPluto lots to a csv

arcpy.management.CopyRows("output_fc_selected_lots", r"output_csv_location", None)







# making a Table View (test)

arcpy.management.MakeTableView("BKMapPLUTO selection", "BKMapPLUTO_View", None, r"C:\Users\dgoodma7\Documents\ArcGIS\Projects\ddg_project\_data", "FID FID HIDDEN NONE;Shape Shape HIDDEN NONE;Borough Borough HIDDEN NONE;Block Block HIDDEN NONE;Lot Lot HIDDEN NONE;CD CD HIDDEN NONE;CT2010 CT2010 HIDDEN NONE;CB2010 CB2010 HIDDEN NONE;SchoolDist SchoolDist HIDDEN NONE;Council Council HIDDEN NONE;ZipCode ZipCode HIDDEN NONE;FireComp FireComp HIDDEN NONE;PolicePrct PolicePrct HIDDEN NONE;HealthCent HealthCent HIDDEN NONE;HealthArea HealthArea HIDDEN NONE;SanitBoro SanitBoro HIDDEN NONE;SanitDistr SanitDistr HIDDEN NONE;SanitSub SanitSub HIDDEN NONE;Address Address VISIBLE NONE;ZoneDist1 ZoneDist1 HIDDEN NONE;ZoneDist2 ZoneDist2 HIDDEN NONE;ZoneDist3 ZoneDist3 HIDDEN NONE;ZoneDist4 ZoneDist4 HIDDEN NONE;Overlay1 Overlay1 HIDDEN NONE;Overlay2 Overlay2 HIDDEN NONE;SPDist1 SPDist1 HIDDEN NONE;SPDist2 SPDist2 HIDDEN NONE;SPDist3 SPDist3 HIDDEN NONE;LtdHeight LtdHeight HIDDEN NONE;SplitZone SplitZone HIDDEN NONE;BldgClass BldgClass HIDDEN NONE;LandUse LandUse HIDDEN NONE;Easements Easements HIDDEN NONE;OwnerType OwnerType HIDDEN NONE;OwnerName OwnerName HIDDEN NONE;LotArea LotArea HIDDEN NONE;BldgArea BldgArea HIDDEN NONE;ComArea ComArea HIDDEN NONE;ResArea ResArea HIDDEN NONE;OfficeArea OfficeArea HIDDEN NONE;RetailArea RetailArea HIDDEN NONE;GarageArea GarageArea HIDDEN NONE;StrgeArea StrgeArea HIDDEN NONE;FactryArea FactryArea HIDDEN NONE;OtherArea OtherArea HIDDEN NONE;AreaSource AreaSource HIDDEN NONE;NumBldgs NumBldgs HIDDEN NONE;NumFloors NumFloors HIDDEN NONE;UnitsRes UnitsRes HIDDEN NONE;UnitsTotal UnitsTotal HIDDEN NONE;LotFront LotFront HIDDEN NONE;LotDepth LotDepth HIDDEN NONE;BldgFront BldgFront HIDDEN NONE;BldgDepth BldgDepth HIDDEN NONE;Ext Ext HIDDEN NONE;ProxCode ProxCode HIDDEN NONE;IrrLotCode IrrLotCode HIDDEN NONE;LotType LotType HIDDEN NONE;BsmtCode BsmtCode HIDDEN NONE;AssessLand AssessLand HIDDEN NONE;AssessTot AssessTot HIDDEN NONE;ExemptLand ExemptLand HIDDEN NONE;ExemptTot ExemptTot HIDDEN NONE;YearBuilt YearBuilt HIDDEN NONE;YearAlter1 YearAlter1 HIDDEN NONE;YearAlter2 YearAlter2 HIDDEN NONE;HistDist HistDist HIDDEN NONE;Landmark Landmark HIDDEN NONE;BuiltFAR BuiltFAR HIDDEN NONE;ResidFAR ResidFAR HIDDEN NONE;CommFAR CommFAR HIDDEN NONE;FacilFAR FacilFAR HIDDEN NONE;BoroCode BoroCode HIDDEN NONE;BBL BBL VISIBLE NONE;CondoNo CondoNo HIDDEN NONE;Tract2010 Tract2010 HIDDEN NONE;XCoord XCoord HIDDEN NONE;YCoord YCoord HIDDEN NONE;ZoneMap ZoneMap HIDDEN NONE;ZMCode ZMCode HIDDEN NONE;Sanborn Sanborn HIDDEN NONE;TaxMap TaxMap HIDDEN NONE;EDesigNum EDesigNum HIDDEN NONE;APPBBL APPBBL HIDDEN NONE;APPDate APPDate HIDDEN NONE;PLUTOMapID PLUTOMapID HIDDEN NONE;FIRM07_FLA FIRM07_FLA HIDDEN NONE;PFIRM15_FL PFIRM15_FL HIDDEN NONE;Version Version HIDDEN NONE;MAPPLUTO_F MAPPLUTO_F HIDDEN NONE;SHAPE_area SHAPE_area HIDDEN NONE;SHAPE_len SHAPE_len HIDDEN NONE")


# possible use of MapPLUTO from web

lyrTest = 'http://services5.arcgis.com/GfwWNkhOj9bNBqoJ/arcgis/rest/services/MAPPLUTO/FeatureServer/0/query?where=1=1&outFields=*&outSR=4326&f=geojson'
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps("Map")[0]
aprxMap.addDataFromPath(lyrTest)


# use pandas and data frames
