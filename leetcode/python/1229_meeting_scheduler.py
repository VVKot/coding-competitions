from typing import List


class Solution:

    def minAvailableDuration(self,
                             slots1: List[List[int]],
                             slots2: List[List[int]],
                             duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        schedule1, schedule2 = iter(slots1), iter(slots2)
        first, second = next(schedule1), next(schedule2)
        while first and second:
            intersection = self.get_intersection(first, second)
            if intersection:
                start, end = intersection
                if end-start >= duration:
                    return [start, start+duration]
            _, first_end = first
            _, second_end = second
            if first_end < second_end:
                first = next(schedule1, [])
            else:
                second = next(schedule2, [])
        return []

    def get_intersection(self,
                         first: List[int],
                         second: List[int]) -> List[int]:
        s1, e1 = first
        s2, e2 = second
        max_start = max(s1, s2)
        min_end = min(e1, e2)
        if max_start <= min_end:
            return [max_start, min_end]
        return []
