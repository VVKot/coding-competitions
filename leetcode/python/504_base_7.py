class Solution:

    def convertToBase7(self, num: int) -> str:
        result = ''
        n = abs(num)
        while n:
            n, curr = divmod(n, 7)
            result = str(curr) + result
        return '-' * (num < 0) + result or '0'
