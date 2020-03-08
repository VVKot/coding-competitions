"""
T: O(N)
S: O(N)

We need to only store one mapping using this scheme. Also, the performance of
the encoding method can be treated as O(1) due to the total number of short
URLs being quite large - 62**6.
"""

import random
import string


class Codec:

    ALPHABET = string.digits + string.ascii_letters

    def __init__(self, url_len=6):
        self.url_len = url_len
        self.url_map = {}

    def encode(self, longUrl: str) -> str:
        short_url = self._get_short_url()
        while short_url in self.url_map:
            short_url = self._get_short_url()
        self.url_map[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl]

    def _get_short_url(self) -> str:
        return "".join(
            random.choice(self.ALPHABET) for _ in range(self.url_len))
