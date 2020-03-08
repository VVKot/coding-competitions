class Solution:
    def generateParenthesis(self, num):
        N = num
        cache = [[] for _ in range(N+1)]
        cache[0] = ['']
        for i in range(N+1):
            for j in range(N):
                cache[i] += ['(' + x + ')' + y for x in cache[j]
                             for y in cache[i-j-1]]
        return cache[N]
