# pip install elasticsearch==7.13.0
from elasticsearch import Elasticsearch
import json
import os


def get_es_connection():
    # es_host = choice(['localhost'])
    # es_port = 9200
    # es = Elasticsearch([{'host': es_host, 'port': es_port}], timeout=30, max_retries=10, retry_on_timeout=True)
    es = Elasticsearch(['http://localhost:9200'])
    return es


def create_index(index_name):
    es = get_es_connection()
    mapping = read_config('es_setting.json', key=index_name)

    res = es.indices.create(
        index=index_name, ignore=400, body=mapping,
        include_type_name=True
    )

    return res


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
