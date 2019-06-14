from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row) // 2
        unions = N
        parents = list(range(N))

        def find(i):
            if i == parents[i]:
                return i
            parents[i] = find(parents[i])
            return parents[i]

        def union(s, e):
            parent_s = find(s)
            parent_e = find(e)
            if parent_s != parent_e:
                nonlocal unions
                unions -= 1
                parents[parent_e] = parent_s

        for i in range(N):
            a, b = row[2*i], row[2*i + 1]
            union(a//2, b//2)

        return N - unions
