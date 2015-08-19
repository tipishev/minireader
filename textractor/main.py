#!/usr/bin/env python3

import codecs
import re
from bleach import clean, linkify
from utils import unify_spaces, filter_scripts, filter_styles

def get_raw_html():
    with codecs.open('sources/gazeta', 'r', 'cp1251') as f:
        return f.read()

def extract_text(raw_html):
    raw_html = unify_spaces(raw_html)
    raw_html = filter_scripts(raw_html)
    raw_html = filter_styles(raw_html)
    tags = ['p']
    text = clean(raw_html, tags, strip=True)
    return text

def main():
    print(extract_text(get_raw_html()))

if __name__ == "__main__":
    main()
