from crawler.crawler import Crawler
import schedule


def main():
    crawler = Crawler()
    crawler.run()


if __name__ == '__main__':
    main()
