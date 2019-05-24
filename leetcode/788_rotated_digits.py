class Solution:

    def rotatedDigits(self, N: int) -> int:
        good = {i for i in '2569'}
        bad = {i for i in '347'}
        result = 0
        for num in range(1, N+1):
            seq = str(num)
            maybe_good = False
            for ch in seq:
                if ch in bad:
                    break
                if not maybe_good:
                    maybe_good = ch in good
            else:
                if maybe_good:
                    result += 1
        return result
