class Solution:
    def combinationSum3(self, k, n):
        result = [[]]
        for _ in range(k):
            result = [curr + [num]
                      for curr in result
                      for num in range(1, curr[-1] if curr else 10)]
        return [c for c in result if sum(c) == n]
