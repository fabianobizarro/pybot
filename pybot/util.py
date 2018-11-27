import json


def read_json_file(path) -> dict:
    with open(path, mode='rt') as f:
        data = json.load(f)
        return data
