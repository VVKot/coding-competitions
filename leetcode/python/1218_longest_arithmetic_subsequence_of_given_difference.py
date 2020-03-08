import collections
from typing import Dict, List


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        sequence_lengths = collections.defaultdict(int)  # type: Dict[int, int]
        for num in arr:
            sequence_lengths[num] = sequence_lengths[num - difference] + 1
        return max(sequence_lengths.values())
