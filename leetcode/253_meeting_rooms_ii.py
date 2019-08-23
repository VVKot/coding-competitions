import collections
from typing import Counter, List


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        total_room_count = 0
        if not intervals:
            return total_room_count
        room_deltas = collections.Counter()  # type: Counter[int]
        for start, end in intervals:
            room_deltas[start] += 1
            room_deltas[end] -= 1
        running_total = 0
        for timestamp in sorted(room_deltas):
            total_room_count = max(total_room_count, running_total)
            running_total += room_deltas[timestamp]
        return total_room_count
