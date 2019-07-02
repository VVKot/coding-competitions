from typing import List


class RootTrie:

    END = '*'

    def __init__(self, roots: List[str]) -> None:
        self.trie = dict()
        for root in roots:
            curr_trie = self.trie
            for ch in root:
                if ch not in curr_trie:
                    curr_trie[ch] = dict()
                curr_trie = curr_trie[ch]
            curr_trie[self.END] = root
            curr_trie = self.trie

    def get_shortest_root(self, word: str) -> str:
        default_root = ""
        curr_trie = self.trie
        for ch in word:
            if self.END in curr_trie:
                return curr_trie[self.END]
            if ch not in curr_trie:
                return default_root
            curr_trie = curr_trie[ch]
        return curr_trie[self.END] if self.END in curr_trie else default_root


class Solution:

    def replaceWords(self, roots: List[str], sentence: str) -> str:
        trie = RootTrie(roots)
        result = []
        for word in sentence.split():
            curr_root = trie.get_shortest_root(word) or word
            result.append(curr_root)
        return ' '.join(result)
