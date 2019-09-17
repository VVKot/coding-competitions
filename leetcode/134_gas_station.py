from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff = sum(g-c for g, c in zip(gas, cost))
        if total_diff < 0:
            return -1
        curr = start = running_total = 0
        while curr != len(gas) - 1:
            diff = gas[curr] - cost[curr]
            running_total += diff
            if running_total < 0:
                running_total = 0
                start = curr + 1
            curr += 1
        return start
