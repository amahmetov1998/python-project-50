import json
import yaml


def parse(f, format):
    if format == 'json':
        return json.loads(f)
    else:
        return yaml.safe_load(f)
