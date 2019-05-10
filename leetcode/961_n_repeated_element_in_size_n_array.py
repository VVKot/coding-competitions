import collections
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return collections.Counter(A).most_common(1)[0][0]
