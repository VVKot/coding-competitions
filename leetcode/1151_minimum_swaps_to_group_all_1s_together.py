from typing import List


class Solution:

    def minSwaps(self, data: List[int]) -> int:
        ones_count = data.count(1)
        N = len(data)
        zeroes_in_window = sum(1 for i in range(ones_count) if data[i] == 0)
        min_swaps = zeroes_in_window
        for i in range(ones_count, N):
            if data[i] == 0:
                zeroes_in_window += 1
            if data[i-ones_count] == 0:
                zeroes_in_window -= 1
            min_swaps = min(min_swaps, zeroes_in_window)
        return min_swaps
