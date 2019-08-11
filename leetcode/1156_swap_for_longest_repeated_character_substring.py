from collections import Counter, defaultdict
from typing import DefaultDict, List


class Solution:

    def maxRepOpt1(self, text: str) -> int:
        interval_map = self.get_intervals(text)
        ch_count = Counter(text)
        global_max = 0
        for ch, intervals in interval_map.items():
            interval_length = [e-b+1 for b, e in intervals]
            curr_max = max(interval_length)
            if curr_max < ch_count[ch]:
                curr_max += 1
            for i in range(1, len(intervals)):
                if self.is_one_position_away(intervals[i-1], intervals[i]):
                    total = interval_length[i] + interval_length[i-1]
                    if total < ch_count[ch]:
                        total += 1
                    curr_max = max(curr_max, total)

            global_max = max(global_max, curr_max)
        return global_max

    def get_intervals(self, text: str) -> DefaultDict[str, List[List[int]]]:
        intervals = \
            defaultdict(list)  # type: DefaultDict[str, List[List[int]]]
        N = len(text)
        for i, ch in enumerate(text):
            if i == 0 or ch != text[i-1]:
                intervals[ch].append([i, -1])
            if i == N-1 or ch != text[i+1]:
                intervals[ch][-1][1] = i
        return intervals

    def is_one_position_away(self, prev: List[int], curr: List[int]) -> bool:
        _, prev_end = prev
        curr_start, _ = curr
        return curr_start - prev_end == 2
