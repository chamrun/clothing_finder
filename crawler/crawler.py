import time
from multiprocessing import Pool
from os.path import join
import requests
from urllib3.exceptions import MaxRetryError

from helpers.es_helper import get_es_connection, create_index


class Crawler:
    def __init__(self):
        self.base_url = 'https://mobapi.banimode.com/api/v1/products'
        self.es = get_es_connection()
        self.index_name = 'banimode-product'
        create_index(self.index_name)

    def run(self, mod='prod'):
        categories = [3, 2, 1]

        if mod == 'prod':
            pool = Pool(processes=3)
            pool.map(self.crawl, categories)
        elif mod == 'dev':
            for i in categories:
                self.crawl(i)

    def crawl(self, category_id):

        page_number = 1
        while True:

            raw_response = requests.request(
                method='GET',
                url=self.base_url,
                params={
                    'page_size': 50,
                    'filter[product_categories.id][eq]': category_id,
                    'sort[desc]': 'date',
                    'page': page_number,
                }
            )

            response = raw_response.json()

            if not response.get('data', []):
                break

            self.insert_to_es(response.get('data', {}), category_id)

            page_number += 1

    def insert_to_es(self, data, category_id):
        for raw_product in data.get('data', []):
            _id = str(raw_product['id_product'])

            product = {
                "title": raw_product.get('product_name', ''),
                "price": raw_product.get('product_price', 0),
                "description": '',
                "category": str(category_id),
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

    def _req(self, **kwargs):
        if 'url' not in kwargs:
            raise Exception('url is required')
        kwargs['url'] = join(self.base_url, kwargs['url'])

        try:
            response = requests.request(**kwargs)
        except MaxRetryError:
            time.sleep(3)
            return self._req(**kwargs)

        return response


if __name__ == '__main__':
    crawler = Crawler()
    crawler.crawl(3)
