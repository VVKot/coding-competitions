from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        first_len, second_len = len(str1), len(str2)
        possible_gcds = self.get_possible_gcds(first_len, second_len)
        for div_len in possible_gcds:
            gcd = str1[:div_len]
            divided_s1 = gcd * (first_len // div_len)
            divided_s2 = gcd * (second_len // div_len)
            if divided_s1 == str1 and divided_s2 == str2:
                return gcd
        return ''

    def get_possible_gcds(self, num1: int, num2: int) -> List[int]:
        gdcs = []
        min_num = min(num1, num2)
        for i in reversed(range(1, min_num + 1)):
            if not num1 % i and not num2 % i:
                gdcs.append(i)
        return gdcs
