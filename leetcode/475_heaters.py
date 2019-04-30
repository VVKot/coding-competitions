from typing import List
from bisect import bisect_left


class Solution:

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for i in houses:
            pos = bisect_left(heaters, i)
            curr = 0
            if pos == 0:
                curr = heaters[0] - i
            elif pos == len(heaters):
                curr = i - heaters[-1]
            else:
                curr = min(heaters[pos] - i, i - heaters[pos - 1])
            radius = max(radius, curr)
        return radius
