from typing import List
from sys import maxsize as maxint


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        total_room_count = 0
        if not intervals:
            return total_room_count
        min_start = maxint
        max_end = -maxint
        for start, end in intervals:
            min_start = min(min_start, start)
            max_end = max(max_end, end)
        currently_booked_rooms = [0] * (max_end - min_start + 1)
        for start, end in intervals:
            currently_booked_rooms[start-min_start] += 1
            currently_booked_rooms[end-min_start] -= 1
        running_total = 0
        for room_count_delta in currently_booked_rooms:
            total_room_count = max(total_room_count, running_total)
            running_total += room_count_delta
        return total_room_count
