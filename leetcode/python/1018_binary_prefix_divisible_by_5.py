"""
T: O(N)
S: O(1)

To figure out the next number, we can observe that is it just a previous number
shifted to the left by one-bit with one bit value added to the right. The code
also demonstrates how to deal with the overflow issue using modulo.
"""

from typing import List


class Solution:

    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        answers = []
        current_number = 0
        for num in A:
            current_number = (current_number * 2 + num) % 5
            answers.append(current_number == 0)
        return answers
