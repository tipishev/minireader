#!/usr/bin/env python3

from sys import argv

from minireader import MiniReader
from writers import SimpleWriter, UrlWriter

from config import FANCY_FILENAME, FILENAME


def main():
    if len(argv) != 2:
        print('USAGE: main.py <url>')
    else:
        url = argv[1].rstrip('/')
        writer = UrlWriter(url) if FANCY_FILENAME else SimpleWriter(FILENAME)
        mini_reader = MiniReader(writer=writer)
        mini_reader.read(url)

if __name__ == '__main__':
    main()
