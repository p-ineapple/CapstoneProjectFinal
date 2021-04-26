import json
import csv

def data_dict(filename):
    """
    convert jsons files to list of dictionaries
    """
    mainlist = []
    with open(filename, 'r', encoding='utf-8') as f:
        # data from data.json is deserialised into data_dict
        data_dict = json.load(f)
        for data in data_dict:
            mainlist.append(data)
    return mainlist

def fare_dict(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            data.append(line)
    return data