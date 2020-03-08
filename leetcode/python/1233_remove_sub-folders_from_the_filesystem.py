from typing import List


class Trie:

    WORD_MARK = '*'

    def __init__(self):
        self.trie = {}

    def insert(self, word: List[str]) -> None:
        trie = self.trie
        for ch in word:
            trie = trie.setdefault(ch, {})
        trie[self.WORD_MARK] = self.WORD_MARK

    def startsWith(self, prefix: List[str]) -> bool:
        trie = self.trie
        for i, ch in enumerate(prefix):
            if i and self.WORD_MARK in trie:
                return True
            if ch in trie:
                trie = trie[ch]
            else:
                return False
        return self.WORD_MARK in trie


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            word = f.split('/')
            trie.insert(word)
        root_folders = []
        for f in folder:
            word = f.split('/')
            if not trie.startsWith(word[:-1]):
                root_folders.append(f)
        return root_folders
