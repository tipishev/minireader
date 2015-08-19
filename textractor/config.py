#!/usr/bin/env python3

from enum import Enum

class LinksDisplayMode(Enum):
    ''' how to show <a href="http://www.tensor.ru">Тензор</a> '''
    prefer_text = 1  # Тензор or [http://www.tensor.ru] if the text is missing
    url_only = 2  # [http://www.tensor.ru]
    text_and_url = 3  # Тензор [http://www.tensor.ru]

LINKS_DISPLAY_MODE = LinksDisplayMode.prefer_text
