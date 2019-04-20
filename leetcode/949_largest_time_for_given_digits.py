from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A):
        return max(["%d%d:%d%d" % perm for perm in permutations(A) if perm[:2] < (2, 4) and perm[2] < 6] or [""])