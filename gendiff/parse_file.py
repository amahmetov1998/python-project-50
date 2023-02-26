import json
import yaml


def parse_file(f, file_format):
    if file_format == 'json':
        return json.loads(f)
    else:
        return yaml.safe_load(f)
