#!/usr/bin/env python3

import codecs
import re
from bs4 import BeautifulSoup, Comment #, NavigableString, CData, Tag

TRASH_TAGS = ['script', 'style']
INFORMATIVE_TAGS = ['title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
PARSER = 'html5lib'


def is_link(tag):
    return tag.name == 'a'

# should go to utils
def unify_spaces(string):
    suffix = re.compile(r"\s+", re.UNICODE)
    return suffix.sub(r" ", string)

# # soup functions
def drop_tags(soup, tags_to_drop):
    for subtree in soup.find_all(tags_to_drop):
        for tag in subtree:
            tag.extract()
    return soup

def drop_comments(soup):
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()
    return soup

# def keep_tags(soup, tags_to_keep):
#     return soup.find_all(tags_to_keep)

# tag list functions
def drop_attributes(tags):
    for tag in tags:
            tag.attrs = {}
    return tags

def drop_empty(soup):
    empty_tags = soup.find_all(lambda tag: not tag.contents
                                  and (tag.string is None or not tag.string.strip()))
    [empty_tag.extract() for empty_tag in empty_tags]
    return soup

# getting the data
def get_raw_html():
    with codecs.open('sources/gazeta', 'r', 'cp1251') as f:
    # with codecs.open('sources/slon', 'r', 'utf8') as f:
    # with codecs.open('sources/lenta', 'r', 'utf8') as f:
    # with codecs.open('sources/slashdot', 'r', 'utf8') as f:
        return f.read()

def count_text_length(tag):
    return sum([len(string) for string in tag.stripped_strings])

def find_the_textiest_tag(tags):
    return max(tags, key=count_text_length)

def not_only_links(tag):
    return not all([is_link(child) for child in tag.contents])

def wrap_links(tag):
    for child in tag.contents:
        if is_link(child):
            from termcolor import cprint; cprint(child.attrs, 'green')
            child.string = "{} [{}]".format(child.string, child.get('href'))


def extract_text(raw_html):
    soup = BeautifulSoup(raw_html, PARSER)
    # title = soup.title  # ok, that was easy
    soup = drop_tags(soup, TRASH_TAGS)
    # soup = drop_comments(soup)
    textiest = max(soup(INFORMATIVE_TAGS), key=count_text_length)
    content_parent = textiest.parent
    content = filter(not_only_links, content_parent(INFORMATIVE_TAGS))
    for tag in content:
        wrap_links(tag)
        from termcolor import cprint; cprint(tag, 'yellow')
        print(unify_spaces(tag.get_text()))  # strip messes up spaces before links

def main():
    raw = get_raw_html()
    text = extract_text(raw)
    # with open('out.txt', 'w') as f:
    #     f.write(text)

if __name__ == "__main__":
    main()
