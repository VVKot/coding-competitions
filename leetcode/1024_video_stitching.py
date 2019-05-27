from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        prev_prev, prev, result = -1, 0, 0
        for i, j in sorted(clips):
            if prev >= T or i > prev:
                break
            elif prev_prev < i <= prev:
                result, prev_prev = result + 1, prev
            prev = max(prev, j)
        return result if prev >= T else -1
