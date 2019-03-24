class Solution:
    def findComplement(self, num: int) -> int:
        temp = 1
        while temp <= num:
            temp <<= 1
        return (temp - 1) ^ num
