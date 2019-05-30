class Solution:

    def bitwiseComplement(self, N: int) -> int:
        count = len(bin(N)) - 2
        mult = int("0b" + "1" * count, 2)
        return N ^ mult
