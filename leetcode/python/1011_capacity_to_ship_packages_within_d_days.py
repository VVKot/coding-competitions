from typing import List


class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def get_days_to_ship(capacity):
            days = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w <= capacity:
                    curr_weight += w
                else:
                    days += 1
                    curr_weight = w
            return days

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo+hi) // 2
            days_to_ship = get_days_to_ship(mid)
            if days_to_ship > D:
                lo = mid+1
            else:
                hi = mid
        return lo
