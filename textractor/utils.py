#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup

def unify_spaces(string):
    suffix = re.compile(r"\s+", re.UNICODE)
    return suffix.sub(r" ", string)

def filter_scripts(source):
    soup = BeautifulSoup(source)
    [s.extract() for s in soup.findAll('script')]
    return soup

def filter_styles(source):
    soup = BeautifulSoup(source)
    [s.extract() for s in soup.findAll('style')]
    return soup
