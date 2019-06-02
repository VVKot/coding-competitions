class Solution:

    def binaryGap(self, N: int) -> int:
        str_rep = bin(N)[2:]
        prev = None
        dist = 0
        for i, num in enumerate(str_rep):
            if num == "0":
                continue
            if prev is not None:
                dist = max(dist, i - prev)
            prev = i
        return dist
