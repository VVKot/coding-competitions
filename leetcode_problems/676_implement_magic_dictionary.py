from collections import Counter


class MagicDictionary(object):
    def _candidates(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.near = Counter(cand for word in words
                            for cand in self._candidates(word))

    def search(self, word):
        return any(self.near[cand] > 1 or
                   self.near[cand] == 1 and word not in self.words
                   for cand in self._candidates(word))