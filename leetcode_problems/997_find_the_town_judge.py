from collections import defaultdict


class Solution:
    def findJudge(self, N, trust):
        ts = defaultdict(set)
        for k, v in trust:
            ts[k].add(v)
        for i in range(1, N+1):
            if not ts[i]:
                for j in range(1, N+1):
                    if j == i:
                        continue
                    if not i in ts[j]:
                        return -1
                return i
        return -1
