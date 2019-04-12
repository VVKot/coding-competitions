from math import factorial

class Solution:
    def uniquePaths(self, m, n):
        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)
