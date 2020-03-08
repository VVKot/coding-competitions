from typing import List


class Solution:

    roman_map = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    def intToRoman(self, num: int) -> str:
        result = ""
        digits = self.get_digit_list(num)
        N = len(digits)
        for i, digit in enumerate(digits):
            result += self.get_roman(digit, N - i)
        return result

    def get_digit_list(self, num: int) -> List[int]:
        return list(int(ch) for ch in str(num))

    def get_roman(self, digit: int, power: int) -> str:
        multiplier = 10 ** (power - 1)
        val_for_one = self.roman_map[1 * multiplier]
        val_for_five = self.roman_map[5 * multiplier] if power != 4 else ""
        val_for_ten = self.roman_map[10 * multiplier] if power != 4 else ""
        if digit < 4:
            return val_for_one * digit
        elif digit == 4:
            return val_for_one + val_for_five
        elif digit < 9:
            return val_for_five + val_for_one * (digit - 5)
        elif digit == 9:
            return val_for_one + val_for_ten
        raise ValueError("Invalid digit value")
