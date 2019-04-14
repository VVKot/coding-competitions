class Solution:
    def findRedundantConnection(self, edges):
        N = len(edges) + 1
        parent = [None] * N

        def find(x):
            if parent[x] is None:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            parent[root_x] = root_y
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]
