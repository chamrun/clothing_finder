import json
import os


def read_config(file_name, key=None, config_path=None):
    if config_path is None:
        config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config')
    config_file = os.path.join(config_path, file_name)

    with open(config_file, 'r') as f:
        config = json.load(f)

    if key is None:
        return config

    if key not in config:
        raise Exception(f'Key {key} not found in config file {file_name}')

    return config[key]
