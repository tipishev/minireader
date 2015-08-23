#!/usr/bin/env python3

from codecs import open
from config import DEFAULT_FILE_ENCODING


class BaseWriter(object):
    pass


class StdOutWriter(BaseWriter):
    def write(self, long_line):
        print(long_line)


class SimpleWriter(BaseWriter):
    def __init__(self, filename='output.txt'):
        self._filename = filename

    def write(self, long_line):
        with open(self._filename, 'w', DEFAULT_FILE_ENCODING) as f:
            f.write(long_line)
