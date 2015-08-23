#!/usr/bin/env python3

from bs4 import BeautifulSoup
from config import DEFAULT_HTML_PARSER

from utils import unify_spaces, is_not_made_of_links, find_the_textiest_tag,\
    wrap_links, drop_tags, drop_comments

TRASH_TAGS = ['script', 'style']
INFORMATIVE_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']


class BaseExtractor(object):
    pass


class Extractor(BaseExtractor):
    def __init__(self, parser=DEFAULT_HTML_PARSER):
        self._parser = parser

    def extract(self, html):
        paragraphs = []
        soup = BeautifulSoup(html, self._parser)

        if soup.title:
            paragraphs.append(soup.title.get_text(strip=True))

        content_candidates = soup(INFORMATIVE_TAGS)
        for candidate in content_candidates:
            candidate = drop_comments(candidate)
            candidate = drop_tags(candidate, TRASH_TAGS)

        textiest = find_the_textiest_tag(content_candidates)
        content_parent = textiest.parent
        content = filter(is_not_made_of_links,
                         content_parent(INFORMATIVE_TAGS))
        for tag in content:
            tag = wrap_links(tag)
            paragraphs.append(unify_spaces(tag.get_text()))
        return paragraphs
