'''Writers handle the formatted string
'''

from os import makedirs
from os.path import abspath, dirname, join as join_path
from codecs import open as copen
from config import DEFAULT_FILE_ENCODING


class BaseWriter(object):
    pass


class StdOutWriter(BaseWriter):
    ''' writes to STDOUT, useful for debugging '''
    def write(self, long_line):
        print(long_line)


class SimpleWriter(BaseWriter):
    ''' writes to a file with a given filename '''
    def __init__(self, filename='output.txt'):
        self._filename = filename

    def write(self, long_line, encoding=DEFAULT_FILE_ENCODING):
        full_path = abspath(self._filename)
        makedirs(dirname(full_path), exist_ok=True)
        with copen(full_path, 'w', encoding) as f:
            f.write(long_line)


class UrlWriter(SimpleWriter):
    ''' creates the output file path according to URL '''
    @staticmethod
    def _url_to_filename(url):
        assert url.startswith(('http://', 'https://')),\
            "the URL provided does not start with http:// or https://"
        url_parts = url.split('/')
        del url_parts[0:2]
        url_parts[-1] = url_parts[-1].split('.')[0] + '.txt'
        return join_path(*url_parts)

    def __init__(self, url):
        self._filename = self._url_to_filename(url)
