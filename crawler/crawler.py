from multiprocessing import Pool

import requests
from helpers.es_helper import get_es_connection, create_index


class Crawler:
    def __init__(self):
        self.base_url = 'https://mobapi.banimode.com/api/v1/products'
        self.es = get_es_connection()
        self.index_name = 'banimode-product'
        create_index(self.index_name)

    def run(self):
        categories = [1, 2, 3]
        pool = Pool(processes=3)
        pool.map(self.crawl, categories)

    def crawl(self, category_id):

        page_number = 1
        while True:
            # raw_response = requests.request(
            #     method='GET',
            #     url=self.base_url,
            #     params={
            #         'page_size': 50,
            #         'filter[product_categories.id][eq]': category_id,
            #         'sort[desc]': 'date',
            #         'page': page_number,
            #     }
            # )
            #
            # response = raw_response.json()

            from tmp_response import saved_res
            response = saved_res

            if not response.get('data', []):
                break

            self.insert_to_es(response.get('data', {}))

    def insert_to_es(self, data):
        for raw_product in data.get('data', []):
            _id = str(raw_product['id_product'])

            # product = {
            #     'doc': {
            #         "title": raw_product.get('product_name', ''),
            #         "price": raw_product.get('product_price', 0),
            #         "description": '',
            #         "category": '',
            #         "image": raw_product['images']['large_default'][0],
            #         "rating": {
            #             "rate": 0,
            #             "count": 0
            #         }
            #     },
            #     '_id': _id
            # }

            product = {
                "title": raw_product.get('product_name', ''),
                "price": raw_product.get('product_price', 0),
                "description": '',
                "category": '',
                "image": raw_product['images']['large_default'][0],
                "rating": {
                    "rate": 0,
                    "count": 0
                }
            }

            self.es.index(
                index=self.index_name,
                doc_type='product',
                body=product,
                id=_id
            )


if __name__ == '__main__':
    crawler = Crawler()
    crawler.crawl(3)
