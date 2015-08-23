#!/usr/bin/env python3

from codecs import open
from requests import get


class BaseFetcher(object):
    pass


class Fetcher(object):

    def fetch(self, url=None):
        return get(url).text


class DummyFetcher(object):
    ''' can be used for testing '''
    def fetch(self, url=None):
        # with codecs.open('sources/slon', 'r', 'utf8') as f:
        # with codecs.open('sources/lenta', 'r', 'utf8') as f:
        # with codecs.open('sources/slashdot', 'r', 'utf8') as f:
        with open('sources/gazeta', 'r', 'cp1251') as f:
            return f.read()
