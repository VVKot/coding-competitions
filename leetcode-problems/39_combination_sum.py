class Solution(object):
    def combinationSum(self, candidates, target):
        sorted_nums = sorted(candidates)
        result = []

        def dfs(remain, combo, index):
            if remain == 0:
                result.append(combo)
                return
            for i in range(index, len(sorted_nums)):
                curr = sorted_nums[i]
                if curr > remain:
                    break

                dfs(remain - curr, combo + [curr], i)

        dfs(target, [], 0)
        return result
