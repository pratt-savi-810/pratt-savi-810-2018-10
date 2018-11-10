from get_sa_lps import get_sa_lps

points_dir = 'Z:/Windows/Individual Landmarks'
footprint_dir = 'Z:/Windows/LPC_IL_HD_Bld_DB_10_19_18'

input_bin_list = ['1008707', '1077813', '1008701']

lp_points = '{}/geo_export_bb96e157-2828-4424-b504-750f90762fa6.shp'.format(points_dir)
lp_footprints = '{}/LPC_IL_HD_Bld_DB_10_19_18.shp'.format(footprint_dir)
output_csv_dir = 'Z:/Windows/'


get_sa_lps(
    input_bin_list,
    lp_points,
    lp_footprints,
    '400 Feet',
    output_csv_dir,
)
