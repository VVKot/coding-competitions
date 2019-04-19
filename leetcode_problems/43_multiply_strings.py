from itertools import zip_longest


class Solution(object):

    def my_int(self, num):
        return ord(num) - ord('0')

    def add(self, num1, num2):
        carry = 0
        result = []
        for i, j in zip_longest(num1, num2, fillvalue=0):
            carry, curr = divmod(i + j + carry, 10)
            result.append(curr)
        if carry != 0:
            result.append(carry)
        return result

    def multiply(self, num1, num2):
        result = []
        for i, n1 in enumerate(reversed(num1)):
            temp = [0] * i
            carry = 0
            for n2 in reversed(num2):
                carry, curr = divmod(self.my_int(n1) * self.my_int(n2) + carry, 10)
                temp.append(curr)
            if carry != 0:
                temp.append(carry)
            result = self.add(result, temp)
        while len(result) > 1:
            if result[-1] == 0:
                result.pop()
            else:
                break
        return "".join(str(x) for x in reversed(result))
