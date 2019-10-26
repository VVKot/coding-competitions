import bisect
import collections
from typing import Dict, List


class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        positions = self._getPositionMap(t)
        low_bound = 0
        for ch in s:
            ch_positions = positions[ch]
            curr_ch_position = bisect.bisect_left(ch_positions, low_bound)
            if curr_ch_position == len(ch_positions):
                return False
            low_bound = ch_positions[curr_ch_position] + 1
        return True

    def _getPositionMap(self, seq: str):
        positions = collections.defaultdict(list)  # type: Dict[str, List[int]]
        for i, ch in enumerate(seq):
            positions[ch].append(i)
        return positions
