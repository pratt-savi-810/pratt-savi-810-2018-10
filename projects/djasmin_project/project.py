buffer_dist = '150 Feet'
streets_dir = 'G:/Python Project/Shapefiles/Streets'
tax_lots_dir = 'G:/Python Project/Shapefiles'

far_file_list = [
	['Wyckoff_Avenue', 3.6],
	['Myrtle_Avenue', 3.6],
	['Knickerbocker_Avenue', 3.6],
	['Broadway', 3.44],
	['Irving_Avenue', 2.2],
	['Wilson_Avenue', 2.2],
	['Central_Avenue', 2.2],
	['Bushwick_Avenue', 2]
]


def buffer_street_apply_far(
        street,
        far,
        buffer,
):
        arcpy.Buffer_analysis(
        street,
        '{}'.format(street.replace('.shp', '_buf.shp')),
        buffer_dist,
        )


for i in far_file_list:
        street = i[0]
        far = i[1]
        buffer_street_apply_far(
            '{0}/{1}.shp'.format(streets_dir, street),
            far,
            '150 Feet',
        )

    # dissolve tool name will be something like '{}'.format(street.replace('.shp', '_buf_dis.shp'))
    # select bbl by location intersect w/ buffer
    # for selected features calculate new far field


# dissolve function
import arcpy
arcpy.Dissolve_management("far_file_list[0]_buf.shp",
			  "far_file_list[0]_dissolved.shp",
                          "",
			  "SINGLE_PART", 
                          "DISSOLVE_LINES")


for buffer, i in zip("far_file_list[0]_dissolved.shp", len("far_file_list[0]_dissolved.shp")):
    arcpy.MakeFeatureLayer_management("tax_lots_dir_Bushwick_TaxLots.shp", "parcels_lyr_{0}".format(i))

    arcpy.SelectLayerByLocation_management(
         "parcel_lyr_{0}".format(i),
         "INTERSECT",
         "tax_lots_dir_Bushwick_TaxLots.shp".format(i)
    )

    arcpy.FeatureClassToFeatureClass_conversion(
        "parcel_lyr",  # feature layer
        "tax_lots_dir",   # output location
        "Bushwick_NewLots.shp".format(i),  # output name
   )
    
    
# select bbl's where new far field is null (zip codes 11206, 11237 = FAR 2.0; 11207, 11221 = FAR 1.35)
# calculate selected bb's where new_far field is null