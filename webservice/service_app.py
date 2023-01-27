from flask import Flask, request

from helpers.es_helper import get_es_connection

app = Flask(__name__)
es = get_es_connection()


def create_query(raw_query):
    query = {
        "query": {
            "bool": {
                "must": []
            }
        }
    }
    for key, value in raw_query.items():
        query['query']['bool']['must'].append(
            {
                "match": {
                    key: value
                }
            }
        )

    return query


@app.route("/products", methods=['GET'])
def products():
    # raw_query = request.args
    # query = create_query(raw_query)

    raw_result = es.search(
        index="banimode-product",
        # body={"query": query}
    )

    response = []

    for hit in raw_result['hits']['hits']:
        hit['_source']['id'] = hit['_id']
        response.append(hit['_source'])

    return response
