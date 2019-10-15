import collections
from typing import Counter, List


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        num_frequencies = collections.Counter()  # type: Counter[int]
        frequencies_count = collections.Counter()  # type: Counter[int]
        max_prefix_size = 0
        for i, num in enumerate(nums):
            prev = num_frequencies[num]
            num_frequencies[num] += 1
            self._update_frequency_count(frequencies_count, num, prev)
            if self._is_valid_prefix(frequencies_count):
                max_prefix_size = i + 1
        return max_prefix_size

    def _update_frequency_count(self,
                                frequencies_count: Counter[int],
                                num: int,
                                prev_count: int) -> None:
        if prev_count > 0:
            frequencies_count[prev_count] -= 1
        if frequencies_count[prev_count] == 0:
            del frequencies_count[prev_count]
        frequencies_count[prev_count+1] += 1

    def _is_valid_prefix(self, frequencies_count: Counter[int]) -> bool:
        if len(frequencies_count) > 2:
            return False
        if len(frequencies_count) == 1:
            [a] = frequencies_count.keys()
            [b] = frequencies_count.values()
            return a == 1 or b == 1
        [(low_freq, low_count), (hi_freq, hi_count)] = \
            sorted(frequencies_count.items())
        return (low_freq == 1 and low_count == 1) or \
            (hi_freq - low_freq == 1 and hi_count == 1)
