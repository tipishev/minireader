#!/usr/bin/env python3

import codecs
import re
from bs4 import BeautifulSoup, Comment

TRASH_TAGS = ['script', 'style']
# INFORMATIVE_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
INFORMATIVE_TAGS = ['title', 'h2']
PARSER = 'html5lib'


# should go to utils


def unify_spaces(string):
    suffix = re.compile(r"\s+", re.UNICODE)
    return suffix.sub(r" ", string)


# soup functions
def drop_tags(soup, tags_to_drop):
    for tag in soup.findAll(tags_to_drop):
        tag.extract()
    return soup


def drop_comments(soup):
    for c in soup.find_all(text=lambda text: isinstance(text, Comment)):
        c.extract()
    return soup

def keep_tags(soup, tags_to_keep):
    return soup.find_all(tags_to_keep)

# tag list functions
def drop_attributes(tags):
    for tag in tags:
            tag.attrs = {}
    return tags

# def drop_empty_tags(source, tags_to_filter):
#     tags_to_filter = [t for t in tags_to_filter if t != 'br']  # <br> is OK to leave unclosed
#     soup = BeautifulSoup(source)
#     for tag_name in tags_to_filter:
#         empty_tags = soup.findAll(lambda tag: tag.name == tag_name
#                                   and not tag.contents
#                                   and (tag.string is None or not tag.string.strip()))
#         [empty_tag.extract() for empty_tag in empty_tags]
#     return str(soup)

# getting the data
def get_raw_html():
    with codecs.open('sources/gazeta', 'r', 'cp1251') as f:
    # with codecs.open('sources/slon', 'r', 'utf8') as f:
    # with codecs.open('sources/lenta', 'r', 'utf8') as f:
    # with codecs.open('sources/slashdot', 'r', 'utf8') as f:
        return f.read()

def extract_text(raw_html):

    soup = BeautifulSoup(raw_html, PARSER)
    soup = drop_comments(soup)
    soup = drop_tags(soup, TRASH_TAGS)
    print(soup)

    tags = keep_tags(soup, INFORMATIVE_TAGS)
    # tags = drop_attributes(tags)
    text = str(tags)
    return text

def main():
    with open('out.txt', 'w') as f:
        f.write(extract_text(get_raw_html()))

if __name__ == "__main__":
    main()
