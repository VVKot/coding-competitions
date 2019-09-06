from typing import List


class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = list(range(n))
        
        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return False
            parents[p1] = p2
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return False
            
        parents = [find(node) for node in parents]
        return all(parents[0] == node for node in parents)
