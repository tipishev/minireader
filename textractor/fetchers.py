'''Get raw HTML
'''

from requests import get


class BaseFetcher(object):
    pass


class Fetcher(BaseFetcher):

    def fetch(self, url=None):
        return get(url).text
