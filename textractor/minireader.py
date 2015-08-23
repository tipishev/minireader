#!/usr/bin/env python3


from fetchers import Fetcher as DefaultFetcher
from extractors import NaiveExtractor as DefaultExtractor
from combiners import Combiner as DefaultCombiner
from writers import StdOutWriter as DefaultWriter


class MiniReader(object):
    def __init__(self,
                 fetcher=None, extractor=None, combiner=None, writer=None):
        self._fetcher = fetcher or DefaultFetcher()
        self._extractor = extractor or DefaultExtractor()
        self._combiner = combiner or DefaultCombiner()
        self._writer = writer or DefaultWriter()

    def read(self, url):
        self._url = url  # to allow domain-dependent extraction rules
        html = self._fetcher.fetch(self._url)
        paragraphs = self._extractor.extract(html)
        combined = self._combiner.combine(paragraphs)
        self._writer.write(combined)
