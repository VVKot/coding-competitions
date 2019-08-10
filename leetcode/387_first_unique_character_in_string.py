import collections
from typing import Dict, List


class Solution:

    def firstUniqChar(self, s: str) -> int:
        ordered_chars_count = \
            collections.OrderedDict()  # type: Dict[str, List[int, int]]
        for i, char in enumerate(s):
            if char in ordered_chars_count:
                ordered_chars_count[char][1] += 1
            else:
                ordered_chars_count[char] = [i, 1]
        for first_occ, count in ordered_chars_count.values():
            if count == 1:
                return first_occ
        return -1
