import json

def read_json_file(path):
    with open(path, mode='rt') as f:
        data = json.load(f)
        return data
