class Solution:
    def get_set_bits_count(self, num):
        count = 0
        while num:
            count += 1
            num &= num - 1
        return count

    def countBits(self, num):
        result = []
        for n in range(num + 1):
            result.append(self.get_set_bits_count(n))
        return result
