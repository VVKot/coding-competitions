class Solution:

    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        dlen = len(digits)
        i, j = dlen - 2, dlen - 1
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return -1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = digits[i + 1:][::-1]
        result = int(''.join(digits))
        if result == n or result >= 2 ** 31:
            return -1
        return result
