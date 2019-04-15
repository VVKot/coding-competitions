class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = "*"
        self.trie = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        temp_trie = self.trie
        for letter in word:
            temp_trie = temp_trie.setdefault(letter, {})
        temp_trie[self.end] = self.end

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        temp_trie = self.trie
        for letter in word:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                return False
        return self.end in temp_trie

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp_trie = self.trie
        for letter in prefix:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                return False
        return True
