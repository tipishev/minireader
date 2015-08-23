'''Extract content, namely headers and paragraphs from raw HTML
'''

from bs4 import BeautifulSoup
from collections import defaultdict

from utils import unify_spaces, is_not_made_of_links,\
    wrap_links, drop_tags, drop_comments, get_text_length,\
    get_key_with_max_value

from config import HTML_PARSER

TRASH_TAGS = ['script', 'style']
CONTENT_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']


class BaseExtractor(object):
    def __init__(self, parser=HTML_PARSER):
        self._parser = parser
        self._paragraphs = []


class ParentScoreExtractor(BaseExtractor):
    ''' the parent with the highest score (most text) is the content source '''

    def extract(self, html):
        soup = BeautifulSoup(html, self._parser)

        if soup.title:
            self._paragraphs.append(soup.title.get_text(strip=True))

        scoreboard = defaultdict(int)
        content_tags = soup(CONTENT_TAGS)
        for tag in content_tags:
            drop_comments(tag)
            drop_tags(tag, TRASH_TAGS)
            scoreboard[tag.parent] += get_text_length(tag)

        content_parent = get_key_with_max_value(scoreboard)
        content = filter(is_not_made_of_links, content_parent(CONTENT_TAGS))
        for tag in content:
            wrap_links(tag)
            text = unify_spaces(tag.get_text())
            self._paragraphs.append(text)
        return self._paragraphs
