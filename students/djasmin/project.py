
buffer_dist = '150 Feet'
streets_dir = 'E:/Python Project/Shapefiles/Streets'

far_file_list = [
	['Wyckoff_Avenue', 3.6],
	['Myrtle_Avenue', 3.6],
	['Knickerbocker_Avenue', 3.6],
	['Broadway', 3.44],
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
    
    # dissolve tool name will be something like '{}'.format(street.replace('.shp', '_buf_dis.shp'))
    # select bbl by location intersect w/ buffer
    # for selected features calculate new far field
    
   
    
# add field to mappluto, called new far


for i in far_file_list:
    street = i[0]
    far = i[1]
    buffer_street_apply_far(
        '{0}/{1}.shp'.format(streets_dir, street), 
        far, 
        '150 Feet',
    )
    
# select bbl's where new far field is null 
# calculate selected bb's where new far field is null 



    
    
