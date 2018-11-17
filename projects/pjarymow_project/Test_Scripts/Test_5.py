import Functions

project_dir = r'C:/Users/pjarymow/Documents/GitHub/pratt-savi-810-2018-10/projects/pjarymow_project'
bike_json_addr = 'https://tor.publicbikesystem.net/ube/gbfs/v1/'
bikelane_data_url = 'http://opendata.toronto.ca/gcc/bikeways_mtm3.zip'

Functions.import_bikeshare_data(project_dir, bike_json_addr, bikelane_data_url)
