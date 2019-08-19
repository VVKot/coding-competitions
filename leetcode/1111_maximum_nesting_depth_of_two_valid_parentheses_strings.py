from typing import List


class Solution:

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        half_depth = self.get_max_depth(seq) // 2
        depth = 0
        split = [0] * len(seq)
        for i, ch in enumerate(seq):
            if ch == '(':
                depth += 1
                if depth > half_depth:
                    split[i] = 1
            else:
                if depth > half_depth:
                    split[i] = 1
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
