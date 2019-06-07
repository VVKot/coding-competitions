import collections
from typing import List


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        max_num, count_max = self.get_max_count(tasks)
        idle_interval_count = max_num - 1
        idle_interval_len = n - (count_max - 1)
        available_spots = idle_interval_count * idle_interval_len
        tasks_to_do = N - max_num * count_max
        idle_count = max(0, available_spots - tasks_to_do)
        return N + idle_count

    def get_max_count(self, seq):
        max_num, count_max = 0, 0
        counter = collections.defaultdict(int)
        for ch in seq:
            counter[ch] += 1
            count = counter[ch]
            if count == max_num:
                count_max += 1
            elif count > max_num:
                max_num = count
                count_max = 1
        return max_num, count_max
