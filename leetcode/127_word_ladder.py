from collections import deque, defaultdict


class Solution(object):

    def get_word_without_char(self, word, i):
        return word[:i] + "_" + word[i+1:]

    def construct_dict(self, words):
        similar_words = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                new_word = self.get_word_without_char(word, i)
                similar_words[new_word].append(word)
        return similar_words

    def ladderLength(self, beginWord, endWord, wordList):
        sim_words = self.construct_dict(wordList)
        stack = deque([(beginWord, 1)])
        while stack:
            curr, path = stack.popleft()
            if curr == endWord:
                return path
            for i in range(len(curr)):
                new_curr = self.get_word_without_char(curr, i)
                words = sim_words[new_curr]
                for word in words:
                    stack.append((word, path+1))
                sim_words[new_curr] = []
        return 0
