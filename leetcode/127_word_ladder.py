import string
import collections
from typing import List


class Solution:
    def ladderLength(self,
                     beginWord: str,
                     endWord: str,
                     wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        q = collections.deque([(beginWord, 1)])
        while q:
            curr, dist = q.popleft()
            if curr == endWord:
                return dist
            near = self.get_near(wordList, curr)
            for word in near:
                wordList.remove(word)
                q.append((word, dist + 1))
        return 0

    def get_near(self, words, curr):
        result = []
        for i, ch in enumerate(curr):
            for new_ch in string.ascii_lowercase:
                if ch == new_ch:
                    continue
                new_word = curr[:i] + new_ch + curr[i+1:]
                if new_word in words:
                    result.append(new_word)
        return result
