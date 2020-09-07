from bs4 import BeautifulSoup


class parserss():
    def __init__(self, url_content):
        self.url_content = url_content
        self.soup = BeautifulSoup(url_content, 'xml')

    def prettify(self):
        return(self.soup.prettify())

    def find_all(self, tag):
        soup = self.soup
        tag_raw_content = soup.find_all(tag)
        tag_content = tag_raw_content
        return(tag_content)

    def find(self, tag):
        soup = self.soup
        tag_raw_content = soup.find(tag)
        tag_content = tag_raw_content
        return(tag_content)
