from itertools import zip_longest


class Solution(object):

    def my_int(self, num):
        return ord(num) - ord('0')

    def multiply(self, num1, num2):
        M = len(num1)
        N = len(num2)
        nums = [0] * (M + N)
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                low = i + j + 1
                high = i + j
                n1 = self.my_int(num1[i])
                n2 = self.my_int(num2[j])
                carry, curr = divmod(n1 * n2 + nums[low], 10)
                nums[low] = curr
                nums[high] += carry
        result = ""
        for num in nums:
            if result or num:
                result += str(num)
        return result if result else "0"
