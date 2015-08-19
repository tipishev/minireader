#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup

def unify_spaces(string):
    suffix = re.compile(r"\s+", re.UNICODE)
    return suffix.sub(r" ", string)

def drop_tags(source, tags=[]):
    soup = BeautifulSoup(source)
    for trash in soup.findAll(tags):
        trash.extract()
    return soup

def drop_empty_tags(source, tags_to_filter):
    tags_to_filter = [t for t in tags_to_filter if t != 'br']  # <br> is OK to leave unclosed
    soup = BeautifulSoup(source)
    for tag_name in tags_to_filter:
        empty_tags = soup.findAll(lambda tag: tag.name == tag_name
                                  and not tag.contents
                                  and (tag.string is None or not tag.string.strip()))
        [empty_tag.extract() for empty_tag in empty_tags]
    return str(soup)

