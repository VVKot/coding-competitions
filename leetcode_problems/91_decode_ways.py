class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        second_last, last = 0, 1
        for i, ch in enumerate(s):
            ways = 0
            curr = int(ch)
            # current number is not 0
            if curr:
                # there is at least one way to decode
                ways = last
                # we are at the second number of further
                if i:
                    prev = int(s[i-1])
                    # 10 <= s[prev:curr+1] <=26
                    if 1 <= prev < 2 or (prev == 2 and curr <= 6):
                        ways += second_last
            # current number is 0
            else:
                # string starts with zero
                if not i:
                    return 0
                prev = int(s[i-1])
                # string contains 00 or 30, 40...
                if not prev or prev > 2:
                    return 0
                ways = second_last
            second_last, last = last, ways
        return last
