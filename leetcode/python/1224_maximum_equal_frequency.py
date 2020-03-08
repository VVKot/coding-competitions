import collections
from typing import Counter, List


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        number_freq = collections.Counter()  # type: Counter[int]
        freq_count = collections.Counter()  # type: Counter[int]
        max_prefix_size = max_freq = 0
        for i, num in enumerate(nums):
            self._update_frequency_count(number_freq, freq_count, num)
            max_freq = max(max_freq, number_freq[num])
            if self._is_valid_prefix(freq_count, max_freq, i):
                max_prefix_size = i + 1
        return max_prefix_size

    def _update_frequency_count(self,
                                number_freq: Counter[int],
                                freq_count: Counter[int],
                                num: int) -> None:
        number_freq[num] += 1
        freq_count[number_freq[num]-1] -= 1
        freq_count[number_freq[num]] += 1

    def _is_valid_prefix(self,
                         freq_count: Counter[int],
                         max_freq: int,
                         curr_index: int) -> bool:
        all_numbers_appear_once = max_freq == 1
        one_number_appears_once = max_freq * freq_count[max_freq] == curr_index
        one_number_appears_max_frequency_times = \
            (max_freq-1) * (freq_count[max_freq-1]+1) == curr_index
        return all_numbers_appear_once or one_number_appears_once or \
            one_number_appears_max_frequency_times
