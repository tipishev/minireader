'''A container for the conveyor components with reasonable defaults
'''

import logging

from fetchers import Fetcher as DefaultFetcher
from extractors import VotingExtractor as DefaultExtractor
from combiners import Combiner as DefaultCombiner
from writers import StdOutWriter as DefaultWriter  # won't write any files


class MiniReader(object):
    def __init__(self,
                 fetcher=None, extractor=None, combiner=None, writer=None):
        self._fetcher = fetcher or DefaultFetcher()
        self._extractor = extractor or DefaultExtractor()
        self._combiner = combiner or DefaultCombiner()
        self._writer = writer or DefaultWriter()

    def read(self, url):
        try:
            html = self._fetcher.fetch(url)
            paragraphs = self._extractor.extract(html)
            pretty_string = self._combiner.combine(paragraphs)
            self._writer.write(pretty_string)
        except Exception as e:
            logging.exception('Failed to read %s: %s', url, e)
