class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates or not target:
            return []
        result = []
        cand = sorted(candidates)
        N = len(candidates)

        def dfs(remainder, curr_combo, start):
            if remainder == 0:
                result.append(curr_combo)
                return
            for i in range(start, N):
                curr = cand[i]
                if i > start and curr == cand[i-1]:
                    continue
                if curr > remainder:
                    break
                dfs(remainder - curr, curr_combo + [curr], i+1)
        dfs(target, [], 0)
        return result
