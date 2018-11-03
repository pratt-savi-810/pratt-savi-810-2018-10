from select_bbl_ids import select_bbl_ids

def get_sa_lps(
        list_bbls,
        lpc_points,
        lpc_footprints,
):
    lp_df = lp_points_to_df(lpc_points)

    dict_of_bbls_with_list_of_lps = {}

    for bbl in list_bbls:
        selected_bbls = select_bbl_ids(bbl, "400 Feet")
        return selected_bbls







        
    export_excel(dict_of_bbls_with_list_of_lps)

