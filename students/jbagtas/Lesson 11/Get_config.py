from config_test import read_config
from pprint import pprint
import arcpy

d = read_config('config.json')

pprint(d)

arcpy.Buffer_analysis(
    d['in_file'],
    d['buffer_file'],
    "400 Feet"
)