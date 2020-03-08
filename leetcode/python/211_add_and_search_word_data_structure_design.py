class Trie:

    WORD_MARK = '*'
    ANY_CHAR_MARK = '.'

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for ch in word:
            trie = trie.setdefault(ch, {})
        trie[self.WORD_MARK] = self.WORD_MARK

    def search_regex(self, regex: str) -> bool:
        pattern_len = len(regex)
        prefixes_to_check = [(0, self.trie)]
        while prefixes_to_check:
            index, curr_trie = prefixes_to_check.pop()
            if index == pattern_len:
                if self.WORD_MARK in curr_trie:
                    return True
                continue
            curr_char = regex[index]
            if curr_char == self.ANY_CHAR_MARK:
                for next_ch in curr_trie:
                    if next_ch == self.WORD_MARK:
                        continue
                    prefixes_to_check.append((index+1, curr_trie[next_ch]))
            if curr_char in curr_trie:
                prefixes_to_check.append((index+1, curr_trie[curr_char]))
        return False


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search_regex(word)
