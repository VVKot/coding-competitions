from typing import List


class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        ranks = [1] * (n)

        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            parent1, parent2 = map(find, [node1, node2])
            rank1 = ranks[parent1]
            rank2 = ranks[parent2]
            if rank1 >= rank2:
                if rank1 == rank2:
                    ranks[parent1] += 1
                parents[parent2] = parent1
            else:
                parents[parent1] = parent2

        for node1, node2 in edges:
            union(node1, node2)
        return len(set(find(p) for p in parents))
