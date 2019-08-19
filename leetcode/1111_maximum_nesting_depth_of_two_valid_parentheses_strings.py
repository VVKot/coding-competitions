import math
from typing import List


class Solution:

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        max_depth = self.get_max_depth(seq)
        max_allowed_depth = math.ceil(max_depth) // 2
        depth = 0
        split = []
        for ch in seq:
            if ch == '(':
                depth += 1
                if depth <= max_allowed_depth:
                    split.append(1)
                else:
                    split.append(0)
            else:
                if depth <= max_allowed_depth:
                    split.append(1)
                else:
                    split.append(0)
                depth -= 1
        return split

    def get_max_depth(self, seq: str) -> int:
        depth = 0
        max_depth = 0
        for ch in seq:
            if ch == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            else:
                depth -= 1
        return max_depth
