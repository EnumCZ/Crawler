from link_finder import LinkFinder
import urllib.request
from urllib.parse import urlparse


class Crawler:

    website_url = ''
    queue = []
    crawled = []

    def __init__(self, website_url):
        Crawler.website_url = website_url
        Crawler.queue = self.find_page_links(website_url)
        Crawler.crawled = []
        

    @staticmethod
    def find_page_links(link):
        try:
            html = urllib.request.urlopen(link).read().decode('utf-8')
        # 404 or a file
        except Exception as ex:
            return []
        link_finder = LinkFinder(link)
        link_finder.feed(html)
        
        return link_finder.get_page_links()


    @staticmethod
    def add_links_to_queue(links):
        for link in links:
            # ignoring links outside of given url
            if urlparse(link).netloc == urlparse(Crawler.website_url).netloc:
                if (link not in Crawler.queue) and (link not in Crawler.crawled):
                    Crawler.queue.append(link)


    @staticmethod
    def crawl():
        while len(Crawler.queue) > 0:
            for link in Crawler.queue:
                if link not in Crawler.crawled:
                    # adding links into queue
                    found_links = Crawler.find_page_links(link)
                    Crawler.add_links_to_queue(found_links)
                    Crawler.crawled.append(link)
                    print(link, '|', len(Crawler.queue), 'in queue', '|', len(Crawler.crawled), 'crawled')
                # removing crawled link from queue
                Crawler.queue.remove(link)


    def get_crawled_links(self):
        return Crawler.crawled

