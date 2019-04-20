from collections import defaultdict


class Solution(object):

    def numPairsDivisibleBy60(self, time):
        comp = defaultdict(int)
        result = 0
        for t in time:
            result += comp[-t % 60]
            comp[t % 60] += 1
        return result
