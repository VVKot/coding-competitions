import string


class Solution:

    def convertToTitle(self, n):
        result = []
        while n:
            n = n - 1
            n, curr = divmod(n, 26)
            result.append(string.ascii_uppercase[curr])
        return ''.join(reversed(result))
