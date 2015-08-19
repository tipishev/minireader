#!/usr/bin/env python3

import codecs
import re
from bleach import clean, linkify, ALLOWED_TAGS
from utils import unify_spaces, drop_tags, drop_empty_tags
from config import *

from bs4 import BeautifulSoup  # FIXME remove

def get_raw_html():
    with codecs.open('sources/gazeta', 'r', 'cp1251') as f:
    # with codecs.open('sources/slon', 'r', 'utf8') as f:
    # with codecs.open('sources/lenta', 'r', 'utf8') as f:
    # with codecs.open('sources/slashdot', 'r', 'utf8') as f:
        return f.read()

def escape_links(attrs, new, allowed_prefixes=('http://', 'https://')):
    href = attrs.get('href', '').lstrip()  # to fix hrefs starting with blanks
    text = attrs.get('_text')
    if not new and href.startswith(allowed_prefixes):
        # attrs['_text'] = '{}[{}]'.format(text, href)
        attrs['_text'] = '[{}]'.format(href)
    else:
        attrs['_text'] = ''
    return attrs
    return None

def extract_text(raw_html):
    text = raw_html
    text = unify_spaces(text)
    text = drop_tags(text, ['script', 'style'])
    informative_tags = ['a', 'p', 'title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    text = clean(
        text,
        tags=informative_tags,
        strip=True,
        strip_comments=True,
    )
    text = linkify(text, callbacks=[escape_links])
    text = clean(text, tags=['p'], strip=True)  # keep only text from <a> tags
    soup = BeautifulSoup(text)
    text = soup.prettify()
    # text = drop_empty_tags(text, informative_tags)

    return str(text)

def main():
    with open('out.txt', 'w') as f:
        f.write(extract_text(get_raw_html()))

if __name__ == "__main__":
    main()
