import arcpy

import pandas as pd

def get_fc_fields (fc):
    field_name = []
    fields = arcpy.ListFields (fc)
    for field in fields:
        field names.append(field.name)
    return field_name