from typing import List


class Solution:

    BASKET_WEIGHT_CAP = 5000

    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        total_weight = 0
        apples_count = 0
        for apple in arr:
            total_weight += apple
            if total_weight > self.BASKET_WEIGHT_CAP:
                break
            apples_count += 1
        return apples_count
