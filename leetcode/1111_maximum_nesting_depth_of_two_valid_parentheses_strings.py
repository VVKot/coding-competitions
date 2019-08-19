from typing import List


class Solution:

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        return [i & 1 ^ (ch == '(') for i, ch in enumerate(seq)]
