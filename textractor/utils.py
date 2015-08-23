#!/usr/bin/env python3

from bs4 import BeautifulSoup, Comment #, NavigableString, CData, Tag
import re

# formatting
def unify_spaces(string):
    suffix = re.compile(r"\s+", re.UNICODE)
    return suffix.sub(r" ", string)


# # soup functions
def drop_tags(soup, tags_to_drop):
    try:
        for tag in soup.find_all(tags_to_drop):
            tag.extract()
    except Exception:
        pass
    return soup

def drop_comments(soup):
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()
    return soup

def drop_empty(soup):
    empty_tags = soup.find_all(lambda tag: not tag.contents
                                  and (tag.string is None or not tag.string.strip()))
    [empty_tag.extract() for empty_tag in empty_tags]
    return soup

# tags stuff
def is_link(tag):
    return tag.name == 'a'

def is_not_made_of_links(tag):
    return not all([is_link(child) for child in tag.contents])

def get_text_length(tag):
    try:
        return len(tag.get_text(strip=True))
    except AttributeError:
        return 0

def find_the_textiest_tag(tags):
    return max(tags, key=get_text_length)

def wrap_links(tag):
    for child in tag.contents:
        if is_link(child):
            text = str(child.string or '')
            href = child.get('href')
            child.string = "%s [%s]" % (text, href) if text else "[%s]" % href
    return tag

