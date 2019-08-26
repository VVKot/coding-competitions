from typing import List


class Solution:

    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for i, val in enumerate(data):
            if count:
                if not self._is_valid_data(val):
                    return False
                count -= 1
            else:
                bytes_count = self._get_bytes_count(val)
                if not self._is_valid_bytes_count(bytes_count):
                    return False
                count = bytes_count-1 if bytes_count else 0
        return not count

    def _get_bytes_count(self, val: int) -> int:
        highest_bit_mask = 1 << 7
        count = 0
        while val & highest_bit_mask:
            count += 1
            highest_bit_mask >>= 1
        return count

    def _is_valid_bytes_count(self, count: int) -> bool:
        return count in (0, 2, 3, 4)

    def _is_valid_data(self, val: int) -> int:
        first_bit_mask = 1 << 7
        second_bit_mask = 1 << 6
        return (val & first_bit_mask) and not (val & second_bit_mask)
