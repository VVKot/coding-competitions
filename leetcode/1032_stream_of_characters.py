class Trie:

    def __init__(self):
        self.end = "*"
        self.trie = dict()

    def insert(self, word):
        temp_trie = self.trie
        for letter in word:
            temp_trie = temp_trie.setdefault(letter, {})
        temp_trie[self.end] = self.end

    def search(self, word):
        temp_trie = self.trie
        for letter in word:
            if letter in temp_trie:
                if self.end in temp_trie[letter]:
                    return True
                temp_trie = temp_trie[letter]
            else:
                return False
        return False

class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.rev = ''

    def query(self, letter):
        self.rev = letter + self.rev
        return self.trie.search(self.rev)
