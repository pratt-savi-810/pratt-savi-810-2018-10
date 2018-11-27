DRAWING THE BUSHWICK REZONING PROPOSAL

Project Description

After downloading the PLUTO tax lots shapefile, I also downloaded the street centerline shapefile in order to make buffer selections. 
I separated out by selection each major centerline to conduct more finely-grained/accurate estimations. There are 7 centerline shapefiles
in total: Wyckoff Ave, Irving Ave, Knickerbocker Ave, Wilson Ave, Myrtle Ave, Central Ave, and Broadway.Each corridor will be uniquely 
zoned so this is why I've separated them. I would like to select by buffer for each of these centerlines and then assign FAR values based 
on their location.

150' buffer for corridors


Proposed FAR by corridors:
3.6
- Wyckoff Ave
- Myrtle Ave
- Knickerbocker Ave

3.44
-Broadway

2.2
- Irving Ave
- Wilson Ave
- Central Ave

Data Input:
-NYC Street Centerline
-PLUTO tax lot database
-Bushwick Draft Community Plan

def project_upzoning(line_fc, buffer_distance, mappluto)
	buffer the line

	select mappluto by buffer (or poly if poly is input )

	make feature layer from selection

	feature class to feature class

	for feature layer add field

	calculate far field, based on expected increase
	
I would also like to come up with a function that would populate the remaining fields within this data column i.e. matching <null> values.

![image placeholder](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjIjp_b7creAhVkneAKHV7sC-gQjRx6BAgBEAU&url=https%3A%2F%2Fwww.brownstoner.com%2Fdevelopment%2Fbrooklyn-development-bushwick-rheingold-oda-all-year-123-melrose%2F&psig=AOvVaw0UDRPo2LCTKxQwajys_3Fz&ust=1541974715581659)
