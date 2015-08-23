#!/usr/bin/env python3

from minireader import MiniReader
from fetchers import DummyFetcher
from combiners import Combiner
from writers import SimpleWriter

def main():
    # URL = 'http://www.gazeta.ru/politics/2015/08/22_a_7711805.shtml'
    # URL = 'http://edition.cnn.com/2015/08/22/europe/europe-macedonia-migrant-crisis/index.html'
    # URL = 'https://slon.ru/posts/55437'
    # URL = 'http://tensor.ru/news/906'
    # URL = 'http://www.1tv.ru/news/social/290613'  # fail
    URL = None
    WIDTH = 80

    mini_reader = MiniReader(
            combiner=Combiner(width=WIDTH),
            fetcher=DummyFetcher(),
            writer=SimpleWriter(),
    )
    mini_reader.read(URL)

if __name__ == '__main__':
    main()
