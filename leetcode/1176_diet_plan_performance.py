class Solution:

    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = i = 0
        T = sum(calories[i:i+k])
        while i+k <= len(calories):
            if T < lower:
                res -= 1
            elif T > upper:
                res += 1
            end = min(len(calories)-1, i+k)
            T -= calories[i]
            T += calories[end]
            i += 1
