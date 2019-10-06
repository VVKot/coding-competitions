import collections
from typing import List


class Solution:

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        stepping_numbers = []
        possible_answers = collections.deque(range(1, 10))
        if low == 0:
            stepping_numbers.append(0)
        while possible_answers:
            num = possible_answers.popleft()
            if num < high:
                last = num % 10
                if last > 0:
                    possible_answers.append(num*10 + last-1)
                if last < 9:
                    possible_answers.append(num*10 + last+1)
            if low <= num <= high:
                stepping_numbers.append(num)
        return stepping_numbers
