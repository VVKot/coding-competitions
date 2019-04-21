class Solution:
    def numTrees(self, n):
        if not n:
            return 1
        cache = {0: 1, 1: 1}

        def get_ways(nums_len):
            if nums_len in cache:
                return cache[nums_len]
            result = 0
            for i in range(nums_len):
                result += get_ways(i) * get_ways(nums_len-i-1)
                cache[nums_len] = result
            return result
        return get_ways(n)
