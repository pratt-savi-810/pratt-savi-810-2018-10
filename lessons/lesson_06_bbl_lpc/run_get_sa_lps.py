from get_sa_lps import get_sa_lps

points_dir = 'Z:/Windows/Individual Landmarks'
footprint_dir = 'Z:/Windows/LPC_IL_HD_Bld_DB_10_19_18'

DANNYs_input_list_bins = [1077813, 1008701]
input_list_bins = '10008707'

lp_points = '{}/geo_export_bb96e157-2828-4424-b504-750f90762fa6.shp'.format(points_dir)
lp_footprints = '{}/LPC_IL_HD_Bld_DB_10_19_18.shp'.format(footprint_dir)
output_csv = 'Z:/Windows/Individual Landmarks/selected3.csv'


get_sa_lps(
    input_list_bins,
    lp_points,
    lp_footprints,
    '400 Feet',
    output_csv,
)

