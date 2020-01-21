"""
T: O(N**3)
S: O(N) -> does not consider output space

We move through the text and collect prefixes that are present in words.
When we seen an actual word, we add its position to the result.
"""

from typing import List


class Trie:

    WORD_MARK = '*'

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for ch in word:
            trie = trie.setdefault(ch, {})
        trie[self.WORD_MARK] = self.WORD_MARK

    def search(self, word: str) -> bool:
        trie = self.trie
        for ch in word:
            if ch in trie:
                trie = trie[ch]
            else:
                return False
        return self.WORD_MARK in trie

    def starts_with(self, prefix: str) -> bool:
        trie = self.trie
        for ch in prefix:
            if ch in trie:
                trie = trie[ch]
            else:
                return False
        return bool(trie)


class Solution:

    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = self.build_trie(words)
        index_pairs = []
        S = len(text)
        for left in range(S):
            for right in range(left, S):
                curr_substring = text[left:right + 1]
                if not trie.starts_with(curr_substring):
                    break
                if trie.search(curr_substring):
                    index_pairs.append([left, right])
        return index_pairs

    def build_trie(self, words: List[str]) -> Trie:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie
