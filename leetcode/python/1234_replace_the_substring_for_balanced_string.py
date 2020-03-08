import collections


class Solution:

    LETTERS = ('Q', 'W', 'E', 'R')

    def balancedString(self, s):
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in self.LETTERS):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
