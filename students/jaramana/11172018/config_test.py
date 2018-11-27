import json


def read_config(config_json):
    with open(config_json) as f:
        data = json.load(f)

    return data


def some_function(params):
    empty list = []

    #did some stuff

    for bin in list_of_bins:
        # did some stuff to the bin
        the_stuff_we_did_output = stuff(bin)
        empty_list.append(the_stuff_we_did)

    return empty_list


my_empty_list = some_function(joes_list_of_bins)