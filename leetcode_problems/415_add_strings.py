from itertools import zip_longest


class Solution:
    def addStrings(self, num1, num2):
        result = []
        carry = 0
        for i, j in zip_longest(reversed(num1), reversed(num2), fillvalue=0):
            carry, curr = divmod(int(i)+int(j)+carry, 10)
            result.append(str(curr))
        if carry:
            result.append(str(carry))
        return "".join(reversed(result))
