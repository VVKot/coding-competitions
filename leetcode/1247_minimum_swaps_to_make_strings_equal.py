import collections


class Solution:

    NO_SOLUTION = -1

    def minimumSwap(self, s1: str, s2: str) -> int:
        if not self._has_solution(s1, s2):
            return self.NO_SOLUTION
        chars1, chars2 = list(s1), list(s2)
        swaps_needed = 0
        N = len(s1)
        for i in range(N):
            if chars1[i] != chars2[i]:
                same = chars2[i]
                j = i+1
                while j < N:
                    if chars2[j] == same and chars2[j] != chars1[j]:
                        break
                    j += 1
                if j == N:
                    swaps_needed += 1
                    continue
                chars1[i], chars2[j] = chars2[j], chars1[i]
                swaps_needed += 1
        return swaps_needed

    def _has_solution(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        c1, c2 = collections.Counter(s1), collections.Counter(s2)
        for count in (c1+c2).values():
            if count & 1:
                return False
        return True
