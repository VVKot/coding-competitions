from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        candies_b = set(B)
        for candy in A:
            comp = candy - diff
            if comp in candies_b:
                return [candy, comp]
        return [-1, -1]
