"""
T: O(S+W*L) - L is maximum length of a word
S: O(S+L)

We first compute the number of consecutive characters for the extended word
and a source one. After that, we compare them to see if the first is an
extension of the second. It can only be so if all of the characters are the
same, and the count is either the same of the extension has a bigger count that
is greater than three.

This encoding is called Run-length encoding (RLE).
https://en.wikipedia.org/wiki/Run-length_encoding
"""

import itertools
from typing import List, Tuple


class Solution:

    def expressiveWords(self, S: str, words: List[str]) -> int:
        expressive_word_count = 0
        extended_groups = self.get_groups(S)
        for word in words:
            word_groups = self.get_groups(word)
            if self.is_extension(extended_groups, word_groups):
                expressive_word_count += 1
        return expressive_word_count

    def get_groups(self, S: str) -> List[Tuple[str, int]]:
        return [(ch, len(list(group))) for ch, group in itertools.groupby(S)]

    def is_extension(self, maybe_extension: List[Tuple[str, int]],
                     source: List[Tuple[str, int]]) -> bool:
        if len(maybe_extension) != len(source):
            return False
        for e, s in zip(maybe_extension, source):
            ext_char, ext_count = e
            src_char, src_count = s
            if ext_char != src_char:
                return False
            if not (ext_count == src_count or ext_count >= max(src_count, 3)):
                return False
        return True
