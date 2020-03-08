from typing import List


class Solution:

    def dietPlanPerformance(self,
                            calories: List[int],
                            k: int,
                            lower: int,
                            upper: int) -> int:
        total = i = 0
        N = len(calories)
        running_calories_sum = sum(calories[i:i+k])
        while i+k <= N:
            if running_calories_sum < lower:
                total -= 1
            elif running_calories_sum > upper:
                total += 1
            end = min(N-1, i+k)
            running_calories_sum -= calories[i]
            running_calories_sum += calories[end]
            i += 1
        return total
