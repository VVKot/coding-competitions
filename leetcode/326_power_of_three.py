import string


class Solution:

    digs = string.digits

    def int2base(self, x: int, base: int) -> str:
        if x == 0:
            return self.digs[0]
        digits = []
        while x:
            x, mod = divmod(x, base)
            digits.append(str(mod))
        digits.reverse()
        return ''.join(digits)

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        in_thriary_system = self.int2base(n, 3)
        return in_thriary_system.count('1') == 1 and \
            in_thriary_system.count('2') == 0
