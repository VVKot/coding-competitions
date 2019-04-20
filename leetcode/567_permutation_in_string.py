from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        if not s1 or not s2 or l1 > l2:
            return False
        need = Counter(s1)
        curr = Counter(s2[:l1-1])
        for i, ch in enumerate(s2[l1-1:], l1-1):
            curr[ch] += 1
            if curr == need:
                return True
            start = i - l1 + 1
            ch_at_start = s2[start]
            curr[ch_at_start] -= 1
            if not curr[ch_at_start]:
                del curr[ch_at_start]
        return False
