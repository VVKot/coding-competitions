class Solution:
    def findCircleNum(self, M):
        N = len(M)
        visited = set()

        def dfs(friend):
            for i, is_friend in enumerate(M[friend]):
                if is_friend and i not in visited:
                    visited.add(i)
                    dfs(i)
        result = 0
        for i in range(N):
            if i not in visited:
                dfs(i)
                result += 1
        return result
