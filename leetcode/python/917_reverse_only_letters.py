"""
T: O(N)
S: O(N)

Using two pointers, find the left and right letters. Then swap them. Doing this
in O(1) time is not possible due to the immutability of strings.
"""


class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        chars = list(S)
        left, right = 0, len(S) - 1
        while left < right:
            is_left_letter = chars[left].isalpha()
            is_right_letter = chars[right].isalpha()
            if is_left_letter and is_right_letter:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            elif is_left_letter:
                right -= 1
            else:
                left += 1
        return "".join(chars)
