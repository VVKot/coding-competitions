class Solution:
    def countBits(self, num):
        result = [0]
        while len(result) < num + 1:
            result += [i + 1 for i in result]
        return result[:num + 1]
