class Solution:
    def findCircleNum(self, M):
        N = len(M)
        result = 0
        visited = set()
        for i in range(N):
            if i not in visited:
                stack = [i]
                while stack:
                    curr = stack.pop()
                    if curr not in visited:
                        visited.add(curr)
                        stack.extend(i for i, is_friend in enumerate(
                            M[curr]) if i not in visited and is_friend)
                result += 1
        return result
