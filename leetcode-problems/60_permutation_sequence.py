import math


class Solution:
    def getPermutation(self, n, k):
        result = ""
        k -= 1
        nums = [j for j in range(1, n+1)]
        for i in range(1, n+1):
            div, k = divmod(k, math.factorial(n-i)) if k else (0, 0)
            result += str(nums[div])
            nums.pop(div)
        return result
