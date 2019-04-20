class Solution:
    def is_one_row(self, word):
        w_set = set(word.lower())
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        return w_set <= first or w_set <= second or w_set <= third

    def findWords(self, words):
        return list(filter(lambda x: self.is_one_row(x), words))
