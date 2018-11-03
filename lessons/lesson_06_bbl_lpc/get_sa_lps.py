from select_bin_ids import select_bin_ids
from lp_points_to_df import get_lps_from_bbls


def get_sa_lps(
        input_list_bins,
        lpc_points,
        lpc_footprints,
        distance,
        output_csv,
):
    selected_bins = select_bin_ids(input_list_bins, lpc_footprints, distance)

    get_lps_from_bbls(lpc_points, selected_bins).to_csv(output_csv, index=False)
