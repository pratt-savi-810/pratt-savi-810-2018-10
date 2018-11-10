import arcpy.mapping

Folder = "C:\Users\ashaiban\Desktop\Lesson 6\test"  # Alter this for your output folder
mxd = arcpy.mapping.MapDocument("C:\Users\ashaiban\Desktop\Lesson 6\Untitled.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

for bkmk in arcpy.mapping.ListBookmarks(mxd, "", data_frame=df):
    df.extent = bkmk.extent
    dfname = bkmk.name
    arcpy.RefreshActiveView()
    arcpy.mapping.ExportToPNG(mxd, Folder + "/" + OutText[:-11] + ".png", resolution=600)