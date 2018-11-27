import arcpy
import json

arcpy.env.overwriteOutput = True  # this allows the shapefile to be overwritten


def read_config(config_json):
    with open(config_json) as f:
        data = json.load(f)
    return data


def bridge_export(config_file, map_frames):
    data = read_config(config_file)

    # Declare Variable for Location of csv File with Data
    in_csv = data['in_csv']

    # Project xy Coordinates
    arcpy.MakeXYEventLayer_management(
         in_csv,
         'Brg_Lng',
         'Brg_Lat',
         'in_memory_xy_layer',
     )

    # Declare Variable for Output Location of Shapefile & Location of Workspace for Loading Shapefile
    out_shp_worksp = data['shp_workspace']

    # Create a Shapefile
    arcpy.FeatureClassToFeatureClass_conversion(
         'in_memory_xy_layer',
         out_shp_worksp,
         'brg.shp'
    )

    # Loading Shapefile in Map Document
    # Declare Variable of Location of mxd File with Basemap for Shapefile Load
    load_base = data['basemap']
    # get the map document
    mxd = arcpy.mapping.MapDocument(load_base)
    # Set the workspace
    arcpy.env.workspace = out_shp_worksp
    # get the data frame
    df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
    # Declare Variable of Location to Save Shapefile
    save_ly = data['save_ly']
    # create a new layer
    newlayer = arcpy.mapping.Layer(save_ly)
    # add the layer to the map at the bottom of the TOC in data frame 0
    arcpy.mapping.AddLayer(df, newlayer, "AUTO_ARRANGE")

    # Adding Labeling
    layer = arcpy.mapping.ListLayers(mxd, "brg")[0]  # Indexing list for 1st layer
    if layer.supports("LABELCLASSES"):
        for lblclass in layer.labelClasses:
            lblclass.showClassLabels = True  # type: bool

    layer.showLabels = True
    arcpy.RefreshActiveView()

    for m in map_frames:
        map_frame_sql, map_name = m[0], m[1]

        # Select Features & Zoom
        nycbrg = arcpy.mapping.ListLayers(mxd)[0]
        arcpy.SelectLayerByAttribute_management(nycbrg, "NEW_SELECTION", map_frame_sql)
        df.zoomToSelectedFeatures()


        # Declare Variable of Where to Save Map Export
        make_export = '{}{}.png'.format(data['map_export_dir'], map_name)  # PEP-8 variables should be lowercase
        # Export Map
        arcpy.mapping.ExportToPNG(mxd, make_export, df)
