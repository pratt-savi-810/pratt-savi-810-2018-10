from select_bin_ids import select_bin_ids
from lp_points_to_df import get_lps_from_bbls


def get_sa_lps(
        input_list_bins,
        lpc_points,
        lpc_footprints,
        distance,
        output_csv_dir,
):
    for input_bin in input_list_bins:
        print('Running for BIN: {}'.format(input_bin))
        selected_bins = select_bin_ids(input_bin, lpc_footprints, distance)

        get_lps_from_bbls(lpc_points, selected_bins).to_csv(
            '{}/selected_bin_and_lp_for_bin_{}.csv'.format(output_csv_dir, input_bin),
            index=False,
        )
