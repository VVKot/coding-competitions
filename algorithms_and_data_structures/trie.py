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
