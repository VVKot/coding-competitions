class Solution:
    def totalHammingDistance(self, nums):
        bits = [[0, 0] for _ in range(32)]
        for x in nums:
            for bit in bits:
                bit[int(x % 2)] += 1
                x /= 2
        return sum(x*y for x, y in bits)
