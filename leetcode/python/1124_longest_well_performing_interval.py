from typing import List, Dict


class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        limit = 8
        tiring = result = 0
        seen = {}  # type: Dict[int, int]
        for i, val in enumerate(hours):
            if val > limit:
                tiring += 1
            else:
                tiring -= 1
            if tiring > 0:
                result = i + 1
            seen.setdefault(tiring, i)
            if tiring-1 in seen:
                result = max(result, i - seen[tiring-1])
        return result
