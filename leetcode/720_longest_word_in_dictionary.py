class Solution:
    def longestWord(self, words):
        result = ""
        words.sort()
        trie = set([""])
        for word in words:
            if word[:-1] in trie:
                trie.add(word)
                if len(word) > len(result):
                    result = word
        return result
