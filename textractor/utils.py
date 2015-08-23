'''Various low-level helpers
'''

from bs4 import Comment
from operator import itemgetter
import re
import logging


# Dict helpers
def get_key_with_max_value(scoreboard):
    return max(scoreboard.items(), key=itemgetter(1))[0]


# String helpers
def unify_spaces(string):
    suffix = re.compile(r"\s+", re.UNICODE)
    return suffix.sub(r" ", string)


# Soup helpers
def drop_tags(soup, tags_to_drop):
    try:
        for tag in soup.find_all(tags_to_drop):
            tag.extract()
    except Exception as e:
        logging.warning('Exception while dropping tags: %s', e)


def drop_comments(soup):
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()


def drop_empty(soup):
    empty_tags = soup.find_all(lambda tag: not tag.contents
                               and (tag.string is None
                                    or not tag.string.strip()))
    [empty_tag.extract() for empty_tag in empty_tags]
    return soup


# Tag helpers
def is_link(tag):
    return tag.name == 'a'


def is_not_made_of_links(tag):
    return not all([is_link(child) for child in tag.contents])


def get_text_length(tag):
    try:
        return len(tag.get_text(strip=True))
    except AttributeError:
        return 0


def wrap_links(tag):
    for child in tag.contents:
        if is_link(child):
            text = str(child.string or '')
            href = child.get('href')
            child.string = "%s [%s]" % (text, href) if text else "[%s]" % href
