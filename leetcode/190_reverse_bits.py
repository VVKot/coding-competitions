class Solution:

    def reverseBits(self, n):
        bits = '{0:032b}'.format(n)
        return int(bits[::-1], 2)
