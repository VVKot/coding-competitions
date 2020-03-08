class Solution:

    def bitwiseComplement(self, N: int) -> int:
        mult = 1
        while N > mult:
            mult <<= 1
            mult += 1
        return N ^ mult
