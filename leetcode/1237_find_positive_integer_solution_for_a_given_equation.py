from typing import List


"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution:
    def findSolution(self,
                     customfunction,
                     z: int) -> List[List[int]]:
        x = 1000
        y = 1
        result = []
        while 1 <= x <= 1000 and 1 <= y <= 1000:
            curr_value = customfunction.f(x, y)
            if curr_value == z:
                result.append([x, y])
                x -= 1
                y += 1
            elif curr_value > z:
                x -= 1
            elif curr_value < z:
                y += 1
        return result
