# import json
#
#
# def read_config(config_json):
#     with open(config_json) as f:
#         data = json.load(f)
#     return data

from config_test import read_config
import arcpy
d = read_config('config.json')

pprint(d)
arcpy.Buffer_analysis(
    d["in_ile"],
    d['bufer_file'],
    "400 feet")