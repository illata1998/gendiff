import json
import yaml


def parse_files(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as f:
            return json.load(f)
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path) as f:
            return yaml.load(f, Loader=yaml.SafeLoader)
