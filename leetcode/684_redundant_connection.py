from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents, ranks = {}, {}

        def insert(node):
            parents[node] = node
            ranks[node] = 1

        def find(node):
            curr_parent = parents[node]
            if curr_parent == node:
                return node
            parents[node] = find(curr_parent)
            return parents[node]

        def union(node1, node2):
            rank1, rank2 = ranks[node1], ranks[node2]
            if rank1 == rank2:
                ranks[node1] += 1
                parents[node2] = node1
            elif rank1 > rank2:
                parents[node2] = node1
            else:
                parents[node1] = node2

        for s, e in edges:
            if s not in parents:
                insert(s)
            if e not in parents:
                insert(e)
            s_parent, e_parent = find(s), find(e)
            if s_parent == e_parent:
                return list(sorted([s, e]))
            else:
                union(s_parent, e_parent)
        return [-1, -1]
