class Solution:

    def addDigits(self, num: int) -> int:
        while num >= 10:
            digit_sum = 0
            while num:
                num, mod = divmod(num, 10)
                digit_sum += mod
            num = digit_sum
        return num
