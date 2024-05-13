import json
import yaml


def parser(data, extension):
    match extension:
        case 'json':
            return json.loads(data)
        case 'yaml' | 'yml':
            return yaml.load(data, Loader=yaml.SafeLoader)
