from collections import defaultdict


class Solution:
    def findJudge(self, N, trust):
        truct_chain = defaultdict(set)
        for k, v in trust:
            truct_chain[k].add(v)
        for cand in range(1, N+1):
            if not truct_chain[cand]:
                for other in range(1, N+1):
                    if other == cand:
                        continue
                    if not cand in truct_chain[other]:
                        return -1
                return cand
        return -1
