from operator import xor
from functools import reduce


class Solution(object):

    def findTheDifference(self, s, t):
        return chr(reduce(xor, map(ord, s+t)))
