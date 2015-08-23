#!/usr/bin/env python3

from sys import argv

from minireader import MiniReader

from extractors import ParentScoreExtractor
from combiners import Combiner
from writers import SimpleWriter, UrlWriter

def main():
    # URL = 'http://www.gazeta.ru/politics/2015/08/22_a_7711805.shtml'
    # URL = 'http://edition.cnn.com/2015/08/22/europe/europe-macedonia-migrant-crisis/index.html'
    # URL = 'https://slon.ru/posts/55437'
    # URL = 'https://simple.wikipedia.org/wiki/Bishop'
    # URL = 'http://tensor.ru/news/906'
    # URL = 'http://www.1tv.ru/news/social/290613'
    # URL = 'http://shender.ru/paper/text/?.file=979'
    # URL = 'http://lenta.ru/news/2015/08/23/boat'
    # URL = 'http://ya.ru'

    if len(argv) != 2:
        print('USAGE: main.py <url>')
    else:
        url = argv[1].rstrip('/')
        mini_reader = MiniReader()
        mini_reader.read(url)

if __name__ == '__main__':
    main()
