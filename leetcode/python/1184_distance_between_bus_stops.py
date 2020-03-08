from typing import List


class Solution:

    def distanceBetweenBusStops(self,
                                distance: List[int],
                                start: int,
                                destination: int) -> int:
        start, destination = sorted([start, destination])
        direct_route = detour_route = 0
        for i, dist in enumerate(distance):
            if start <= i < destination:
                direct_route += dist
            else:
                detour_route += dist
        return min(direct_route, detour_route)
