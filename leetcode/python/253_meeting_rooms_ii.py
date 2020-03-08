from typing import List


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        total_room_count = 0
        if not intervals:
            return 0
        N = len(intervals)
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)
        start_pointer = end_pointer = 0
        while start_pointer < N:
            if starts[start_pointer] >= ends[end_pointer]:
                total_room_count -= 1
                end_pointer += 1

            start_pointer += 1
            total_room_count += 1
        return total_room_count
