"""
T: O(N)
S: O(1) - additional

The simplest idea possible - fill the array with N-1 number and then balance
it with negative sum of them. We start from the zero to avoid duplication for
the case of N = 2. Otherwise, we end up with two zeroes as an answer.
"""

from typing import List


class Solution:

    def sumZero(self, n: int) -> List[int]:
        zero_sum_list = list(range(1, n))
        zero_sum_list.append(-sum(zero_sum_list))
        return zero_sum_list
