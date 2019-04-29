from typing import List


class Solution:

    def reverse_part(self, arr: List[str], left: int, right: int):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def reverseWords(self, s: str) -> str:
        N = len(s)
        result = [c for c in s]
        left = 0
        right = 1
        while right < N:
            if result[right].isspace():
                self.reverse_part(result, left, right - 1)
                left = right + 1
            right += 1
        if left < right and left < N:
            self.reverse_part(result, left, right - 1)
        return ''.join(result)
