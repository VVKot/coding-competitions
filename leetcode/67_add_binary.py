class Solution:
    def addBinary(self, a, b):
        index = 0
        carry = "0"
        sum_ = ""
        while index < max(len(a), len(b)) or carry == "1":
            num_a = a[-1 - index] if index < len(a) else "0"
            num_b = b[-1 - index] if index < len(b) else "0"

            val = self.my_int(num_a) + self.my_int(num_b) + self.my_int(carry)
            sum_ = "%s%s" % (val % 2, sum_)

            carry = "1" if val > 1 else "0"
            index += 1
        return sum_

    def my_int(self, c):
        return 1 if c == "1" else 0

