class DSU:

    def __init__(self, N: int):
        self.parents = list(range(N))
        self.ranks = [0] * N

    def find(self, node: int) -> int:
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, n1: int, n2: int) -> None:
        p1, p2 = map(self.find, (n1, n2))
        rank1, rank2 = map(self.ranks.__getitem__, (p1, p2))
        if rank1 >= rank2:
            if rank1 == rank2:
                rank1 += 1
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
