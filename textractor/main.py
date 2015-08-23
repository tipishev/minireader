#!/usr/bin/env python3

import codecs
import re
from bs4 import BeautifulSoup, Comment #, NavigableString, CData, Tag
from textwrap import fill
from requests import get

from config import HTML_PARSER, DEFAULT_LINE_WIDTH

from utils import unify_spaces,\
                  is_link, is_not_made_of_links,\
                  find_the_textiest_tag,\
                  wrap_links, drop_tags, drop_comments, drop_empty

TRASH_TAGS = ['script', 'style']
INFORMATIVE_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']

class HtmlFetcher(object):
    # def fetch(url):
    #     return get(url).text

    def fetch(self, url=None):
        with codecs.open('sources/gazeta', 'r', 'cp1251') as f:
        # with codecs.open('sources/slon', 'r', 'utf8') as f:
        # with codecs.open('sources/lenta', 'r', 'utf8') as f:
        # with codecs.open('sources/slashdot', 'r', 'utf8') as f:
            return f.read()

class TextExtractor(object):
    def extract(self, html):
        paragraphs = []
        soup = BeautifulSoup(html, HTML_PARSER)
        content_candidates = soup(INFORMATIVE_TAGS)
        for c in content_candidates:
            c = drop_comments(c)
            c = drop_tags(c, TRASH_TAGS)

        textiest = find_the_textiest_tag(content_candidates)
        content_parent = textiest.parent
        content = filter(is_not_made_of_links, content_parent(INFORMATIVE_TAGS))
        for tag in content:
            tag = wrap_links(tag)
            paragraphs.append(unify_spaces(tag.get_text()))
        return paragraphs

class TextFormatter(object):
    def __init__(self, width=DEFAULT_LINE_WIDTH):
        self._width = width

    def combine(self, paragraphs):
        paragraphs = [fill(paragraph, self._width) for paragraph in paragraphs]
        return '\n\n'.join(paragraphs)


class FileWriter(object):
    def write(self, long_line):
        print(long_line)

class MiniReader(object):
    def __init__(self, html_fetcher=None,
                       text_extractor=None,
                       text_formatter=None,
                       file_writer=None):
        self._html_fetcher = html_fetcher or HtmlFetcher()
        self._text_extractor = text_extractor or TextExtractor()
        self._text_formatter = text_formatter or TextFormatter()
        self._file_writer = file_writer or  FileWriter()

    def read(self, url):
        self._url = url
        html = self._html_fetcher.fetch(self._url)
        paragraphs = self._text_extractor.extract(html)
        formatted = self._text_formatter.combine(paragraphs)
        self._file_writer.write(formatted)


def main():
    URL = 'http://www.gazeta.ru/politics/2015/08/22_a_7711805.shtml'
    mini_reader = MiniReader(
            text_formatter=TextFormatter(width=80),
    )
    mini_reader.read('ololo')

if __name__ == '__main__':
    main()
