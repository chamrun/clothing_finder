# pip install elasticsearch==7.13.0
from elasticsearch import Elasticsearch

from crawler.helpers.config_reader import read_config


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
