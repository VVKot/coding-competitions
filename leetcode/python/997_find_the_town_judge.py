"""
T: O(N+T)
S: O(N)

We can represent this as a graph problem. The judge is the person that trusts
nobody(i.e. out-degree of 0) and the person that is trusted by everybody(i.e.
in-degree of N-1). So, we create a counter for each citizen and decrement it
if the person trusts somebody, and increment if it is trusted by somebody. The
person that ends up with a count of N-1 is a judge since the counter is simply
in-degree minus out-degree.
"""

import collections
from typing import Counter, List


class Solution:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_count = collections.Counter()  # type: Counter[int]
        for who, trusts_whom in trust:
            trust_count[who] -= 1
            trust_count[trusts_whom] += 1
        for i in range(1, N + 1):
            if trust_count[i] == N - 1:
                return i
        return -1
