# -*- coding: utf-8 -*-
"""
file.py
"""
import csv
import codecs
import json
import pandas as pd

def read_csv(filepath):
    """
    read_csv
    """
    dataframe = pd.read_csv(filepath, encoding='Shift_JIS', dtype='str')
    return dataframe.columns.tolist(), dataframe.values

def write_csv(header, data, filepath):
    """
    write_csv
    """
    with open(filepath, 'w') as file_object:
        writer = csv.writer(file_object, lineterminator='\n')
        writer.writerow(header)
        writer.writerows(data)

def read_json(filepath):
    """
    read_json
    """
    with codecs.open(filepath, "r", "utf-8") as file_object:
        return json.loads(file_object.read())
