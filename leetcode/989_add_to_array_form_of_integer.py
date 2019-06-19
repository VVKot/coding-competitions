from itertools import zip_longest
from typing import List


class Solution:

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result = []
        to_add = self.get_array_form(K)
        carry = 0
        for a, b in zip_longest(reversed(A), reversed(to_add), fillvalue=0):
            carry, curr = divmod(a + b + carry, 10)
            result.append(curr)
        if carry:
            result.append(carry)
        return list(reversed(result))

    def get_array_form(self, number):
        return [int(i) for i in str(number)]
