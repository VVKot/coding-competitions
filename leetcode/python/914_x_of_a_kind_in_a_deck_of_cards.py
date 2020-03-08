from collections import Counter
from functools import reduce
from fractions import gcd
from typing import List


class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) >= 2
