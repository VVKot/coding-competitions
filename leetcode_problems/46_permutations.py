class Solution:
    def permute(self, nums):
        result = []

        def helper(curr, rest):
            if not rest:
                result.append(curr)
            else:
                for i, num in enumerate(rest):
                    helper(curr + [num], rest[:i] + rest[i+1:])
        helper([], nums)
        return result
