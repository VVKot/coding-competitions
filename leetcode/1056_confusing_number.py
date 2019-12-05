"""
T: O(N)
S: O(N)

Just do as the description says, find the reverse mapping and compare
it to the number itself.
"""


from typing import List


class Solution:

    DIGITS_MAP = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }

    def confusingNumber(self, N: int) -> bool:
        digits = list(str(N))
        if any(digit not in self.DIGITS_MAP for digit in digits):
            return False
        return N != self._get_flipped_number(digits)

    def _get_flipped_number(self, digits: List[str]) -> int:
        flipped_number = []
        for digit in digits:
            flipped_number.append(self.DIGITS_MAP[digit])
        return int("".join(reversed(flipped_number)))
