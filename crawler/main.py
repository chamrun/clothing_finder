from crawler import Crawler
import schedule


def main():
    crawler = Crawler()
    crawler.run(mod='dev')


if __name__ == '__main__':
    main()
