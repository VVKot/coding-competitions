from functools import reduce


class Solution:

    def titleToNumber(self, s):
        return reduce(lambda x, y: x*26 + y, map(lambda ch: ord(ch) - ord('A') + 1, s))
