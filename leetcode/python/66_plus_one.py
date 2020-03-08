from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        for i in reversed(range(N)):
            digit = digits[i]
            if digit == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
