from typing import Dict, List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        N = len(s)
        dp = {}  # type: Dict[int, bool]

        def can_construct(start):
            if start == N:
                return True
            if start in dp:
                return dp[start]
            for i in range(start, N):
                curr_word = s[start:i+1]
                if curr_word in words:
                    result = can_construct(i+1)
                    if result:
                        dp[start] = True
                        return dp[start]
            dp[start] = False
            return dp[start]

        return can_construct(0)
