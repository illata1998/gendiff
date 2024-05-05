import json
import yaml
from yaml.loader import SafeLoader


def parse_json(file_path):
    with open(file_path) as f:
        data = json.load(f, Loader=SafeLoader)
    return data


def parse_yaml(file_path):
    with open(file_path) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data
