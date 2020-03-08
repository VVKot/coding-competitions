from typing import List


class Solution:

    limit = 10000

    def removeStones(self, stones: List[List[int]]) -> int:
        components = self.get_components(stones)
        return len(stones) - len(set(components))

    def get_components(self, stones: List[List[int]]) -> List[int]:
        components = list(range(self.limit * 2))
        ranks = [1] * (self.limit * 2)

        def union(node1, node2):
            rank1 = ranks[node1]
            rank2 = ranks[node2]
            if rank1 >= rank2:
                if rank1 == rank2:
                    ranks[node1] += 1
                components[node2] = node1
            else:
                components[node1] = node2

        def find(node):
            if components[node] == node:
                return node
            components[node] = find(components[node])
            return components[node]

        for y, x in stones:
            y_node = find(y)
            x_node = find(x + self.limit)
            union(y_node, x_node)
        return [find(y) for y, _ in stones]
