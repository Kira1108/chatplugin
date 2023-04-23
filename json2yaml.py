import yaml
import json


def json2yaml(json_file, yaml_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    with open(yaml_file, 'w') as f:
        yaml.dump(data, f, sort_keys=False)


if __name__ == '__main__':
    json2yaml('openapi.json', 'openapi.yaml')