from typing import List


class Solution:

    def findRedundantDirectedConnection(self,
                                        edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = [0] * (N + 1)
        cand1, cand2 = [], []  # type: List[int], List[int]

        for start, end in edges:
            if parents[end] == 0:
                parents[end] = start
            else:
                cand1 = [parents[end], end]
                cand2 = [start, end]
                break

        parents = list(range(N + 1))

        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        for start, end in edges:
            if [start, end] == cand2:
                continue
            parent_start = find(start)
            if parent_start == end:
                if not cand1:
                    return [start, end]
                return cand1
            parents[end] = parent_start
        return cand2
