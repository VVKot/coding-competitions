from typing import List


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        visited = [WHITE] * len(graph)
        result = []

        def in_cycle(node):
            visited[node] = GRAY
            for neig in graph[node]:
                if visited[neig] == GRAY:
                    return True
                if not visited[neig] and in_cycle(neig):
                    return True
            visited[node] = BLACK
            result.append(node)
            return False
        for i in range(len(graph)):
            if not visited[i]:
                in_cycle(i)
        return sorted(result)
