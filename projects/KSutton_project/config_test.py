import json

def read_config(config_json):
    with open(config_json) as f:
        data = json.load(f)

    return data