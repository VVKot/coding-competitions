"""
T: O(2**N), where N is log10 H 
S: O(2**N), where N is log10 H 

Find all stepping numbers up to high, add them to the result if they are in
the range. Theext stepping number can be either or both of:
1. Current + last digit minus one, if the last digit is not a zero
2. Current + last digit plus one, if the last digit is not a nine
"""

import collections
from typing import List


class Solution:

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        answers = []
        possible_answers = collections.deque(range(1, 10))
        if low == 0:
            answers.append(0)
        while possible_answers:
            num = possible_answers.popleft()
            if num < high:
                last = num % 10
                if last > 0:
                    possible_answers.append(num * 10 + last - 1)
                if last < 9:
                    possible_answers.append(num * 10 + last + 1)
            if low <= num <= high:
                answers.append(num)
        return answers
