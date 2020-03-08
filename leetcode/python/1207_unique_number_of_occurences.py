"""
T: O(N)
S: O(N)

Find the number of occurences of the each element, find unique number of
occurences, compare the two. If they are the same - all occurences numbers
are unique.
"""

import collections
from typing import List


class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_counts = collections.Counter(arr)
        occurences = num_counts.values()
        return len(occurences) == len(set(occurences))
