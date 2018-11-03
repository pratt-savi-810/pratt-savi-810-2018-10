from get_sa_lps import get_sa_lps

points_dir = 'Z:/Windows/Individual Landmarks'
footprint_dir = 'Z:/Windows/LPC Individual Landmark and Historic District Building Database'

input_list_bins = [1077813, 1008701]
lp_points = '{}geo_export_bb96e157-2828-4424-b504-750f90762fa6.shp'.format(points_dir)
lp_footprints = '/geo_export_66ac46a8-1dd1-4930-8599-64f8728f1e8c.shp'.format(points_dir)
out_csv = 'Z:/Windows/Individual Landmarks/selected.csv'

get_sa_lps(input_list_bins, lp_points, lp_footprints, out_csv)
