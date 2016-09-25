from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.found_links = []
        

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    self.found_links.append(parse.urljoin(self.base_url, value))

    
    def get_page_links(self):
        return self.found_links

