from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row) // 2
        parents = {}

        def union(a, b):
            min_, max_ = min(a, b), max(a, b)
            if min_ != max_:
                if min_ in parents:
                    union(parents[min_], max_)
                else:
                    parents[min_] = max_

        for i in range(N):
            a, b = row[2*i], row[2*i + 1]
            union(a//2, b//2)

        return len(parents)
