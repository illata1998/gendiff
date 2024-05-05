import json
import yaml


def parse_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


def parse_yaml(file_path):
    with open(file_path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data
