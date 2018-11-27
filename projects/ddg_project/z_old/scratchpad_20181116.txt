arcpy.management.XYTableToPoint(r"W:\Departments\Publications\DG_Graphics-Pubs\__GIS-Graphics\pratt\python_class\brooklyn_addresses_for_project_geo.csv", r"W:\Departments\Publications\DG_Graphics-Pubs\__GIS-Graphics\pratt\python_class\shapes\address_pts.shp", "Lng", "Lat", None, "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

lyrTest = r"O:\Data\1 - New York City\DCP\MapPLUTO 18v1\MapPLUTO_18v1.gdb\MapPLUTO_18v1"
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps("Map")[0]
aprxMap.addDataFromPath(lyrTest)

arcpy.management.SelectLayerByLocation('MapPLUTO_18v1', "INTERSECT", "address_pts", None, "NEW_SELECTION")
arcpy.management.CopyFeatures('MapPLUTO_18v1', r"W:\Departments\Publications\DG_Graphics-Pubs\__GIS-Graphics\pratt\python_class\shapes\selected_lots.shp")
arcpy.management.CopyRows("selected_lots", r"W:\Departments\Publications\DG_Graphics-Pubs\__GIS-Graphics\pratt\python_class\selected_lots.csv", None)
