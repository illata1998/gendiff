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


def is_json(file_path):
    return file_path.endswith('.json')


def is_yaml(file_path):
    file_path.endswith('.yaml') or file_path.endswith('.yml')


def parse(file_path):
    if is_json(file_path):
        return parse_json(file_path)
    elif is_yaml(file_path):
        return parse_yaml(file_path)
