"""
T: O(N**2)
S: O(N) -> does not consider output space

We move through the text and collect prefixes that are present in words.
When we seen an actual word, we add its position to the result.
"""


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
    def indexPairs(self, text, words):
        word_trie = Trie()
        for word in words:
            word_trie.insert(word)
        index_pairs = []
        prefixes = []
        for end, ch in enumerate(text):
            prefixes.append("")
            new_prefixes = []
            for prefix in prefixes:
                new_prefix = prefix + ch
                if word_trie.search(new_prefix):
                    start = end - len(new_prefix) + 1
                    index_pairs.append([start, end])
                if word_trie.starts_with(new_prefix):
                    new_prefixes.append(new_prefix)
            prefixes = new_prefixes[:]
        return sorted(index_pairs)
