from typing import List


class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:
        result = 0
        conections.sort(key=lambda x: x[2])

        parents = list(range(N+1))
        ranks = [1] * (N+1)

        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            rank1 = ranks[node1]
            rank2 = ranks[node2]
            if rank1 >= rank2:
                if rank1 == rank2:
                    ranks[node1] += 1
                parents[node2] = node1
            else:
                parents[node1] = node2

        for c1, c2, cost in conections:
            n1 = find(c1)
            n2 = find(c2)
            if n1 != n2:
                union(n1, n2)
                result += cost
        parents = [find(x) for x in parents[1:]]
        parent = parents[0]
        if all(parent == p for p in parents):
            return result
        return -1
