import os
import sys
from crawler import Crawler
from link_finder import LinkFinder


def crawl(website_url, file_path):
    crawler = Crawler(website_url)
    crawler.crawl()
    links = crawler.get_crawled_links()
    with open(file_path, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(links))


website_url = sys.argv[1]
file_path = sys.argv[2]

crawl(website_url, file_path)
