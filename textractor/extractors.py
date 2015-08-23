#!/usr/bin/env python3

from bs4 import BeautifulSoup
from config import DEFAULT_HTML_PARSER
from operator import itemgetter

from utils import unify_spaces, is_not_made_of_links, find_the_textiest_tag,\
    wrap_links, drop_tags, drop_comments, get_text_length

TRASH_TAGS = ['script', 'style']
INFORMATIVE_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']


class BaseExtractor(object):
    def __init__(self, parser=DEFAULT_HTML_PARSER):
        self._parser = parser
        self._paragraphs = []


class NaiveExtractor(BaseExtractor):
    ''' finds the textiest tag and extracts its siblings '''

    def extract(self, html):
        soup = BeautifulSoup(html, self._parser)

        if soup.title:
            self._paragraphs.append(soup.title.get_text(strip=True))

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
            self._paragraphs.append(unify_spaces(tag.get_text()))
        return self._paragraphs


class VotingExtractor(BaseExtractor):
    ''' finds the parent with the most text in children '''

    def extract(self, html):
        soup = BeautifulSoup(html, self._parser)

        if soup.title:
            self._paragraphs.append(soup.title.get_text(strip=True))

        content_candidates = soup(INFORMATIVE_TAGS)
        for candidate in content_candidates:
            candidate = drop_comments(candidate)
            candidate = drop_tags(candidate, TRASH_TAGS)

        score = dict()

        for candidate in content_candidates:
            parent = candidate.parent
            if parent in score:
                score[parent] += get_text_length(candidate)
            else:
                score[parent] = get_text_length(candidate)

        content_parent = max(score.items(), key=itemgetter(1))[0]
        from termcolor import cprint; cprint(len(content_parent.contents), 'yellow')
        content = filter(is_not_made_of_links,
                         content_parent(INFORMATIVE_TAGS))
        for tag in content:
            tag = wrap_links(tag)
            self._paragraphs.append(unify_spaces(tag.get_text()))
        return self._paragraphs
