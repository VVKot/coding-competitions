from typing import List


class Solution:

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, result = [], [0] * len(T)  # type: List[int], List[int]
        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result
