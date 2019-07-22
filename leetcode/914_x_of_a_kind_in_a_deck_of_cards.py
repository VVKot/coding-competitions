import collections
from typing import List


class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        card_counts = collections.Counter(deck)
        min_count = min(card_counts.values())
        for group_count in range(2, min_count+1):
            for count in card_counts.values():
                if count % group_count != 0:
                    break
            else:
                return True
        return False
