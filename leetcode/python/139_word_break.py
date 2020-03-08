from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        N = len(s)
        can_break = [True]
        for i in range(1, N+1):
            for j in range(i):
                if can_break[j] and s[j:i] in words:
                    can_break.append(True)
                    break
            else:
                can_break.append(False)
        return can_break[N]
