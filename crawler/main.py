import time

from crawler import Crawler
import schedule


def main():
    crawler = Crawler()
    schedule.every(1).day.do(crawler.run)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
