from itertools import zip_longest


class Solution:
    def addStrings(self, num1, num2):
        result = []
        carry = 0
        for i, j in zip_longest(reversed(num1), reversed(num2)):
            i = 0 if i is None else int(i)
            j = 0 if j is None else int(j)
            carry, curr = divmod(i+j+carry, 10)
            result.append(str(curr))
        if carry:
            result.append(str(carry))
        return "".join(reversed(result))
