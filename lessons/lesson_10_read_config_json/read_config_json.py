import json


def read_configasdfsadf(config_json):
    with open(config_json) as f:
        data = json.load(f)
    return data


# https://github.com/pratt-savi-810/pratt-savi-810-2018-10/blob/master/lessons/lesson_10_read_config_json/read_config_json.py#L6