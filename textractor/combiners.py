'''Classes for combining a paragraphs iterator to a single printable string.
'''

from textwrap import fill
from config import DEFAULT_LINE_WIDTH


class BaseCombiner():
    pass


class Combiner(BaseCombiner):
    def __init__(self, width=DEFAULT_LINE_WIDTH):
        self._width = width

    def combine(self, paragraphs):
        paragraphs = [fill(paragraph, self._width) for paragraph in paragraphs]
        return '\n\n'.join(paragraphs)
