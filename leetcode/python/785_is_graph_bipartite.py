from typing import List


class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        W, R, B = range(3)
        N = len(graph)
        colors = [W] * N
        for vertex in range(N):
            if colors[vertex] != W:
                continue
            stack = [vertex]
            colors[vertex] = R
            while stack:
                curr = stack.pop()
                curr_color = colors[curr]
                for neig in graph[curr]:
                    neig_color = colors[neig]
                    if neig_color == W:
                        stack.append(neig)
                        colors[neig] = R if curr_color == B else B
                    elif neig_color == curr_color:
                        return False
        return True
