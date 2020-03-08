class Solution:

    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        N = len(s)
        i, result = 0, 0
        while i < N:
            curr = self.roman_map[s[i]]
            if i != N - 1 and curr < self.roman_map[s[i + 1]]:
                result -= curr
            else:
                result += curr
            i += 1
        return result
