from typing import Dict


class Solution:

    def word_break_rec(self, word):
        if not word:
            return True
        if word in self.dp:
            return self.dp[word]
        N = len(word)
        for i in range(N):
            curr = word[0:i+1]
            if curr in self.word_set:
                suffix = word[i+1:]
                result = self.word_break_rec(suffix)
                if suffix not in self.dp:
                    self.dp[suffix] = result
                if result:
                    return True
        return False

    def wordBreak(self, s, wordDict):
        self.word_set = set(wordDict)
        self.dp = {}  # type: Dict[str, bool]
        return self.word_break_rec(s)
