class Solution:
    def twoCitySchedCost(self, costs):
        result = 0
        mid = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        for i, (first, second) in enumerate(costs):
            if i < mid:
                result += first
            else:
                result += second
        return result
