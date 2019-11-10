"""
T: O(2^W + W*L)
S: O(W + L)

The problem is solvable in this way because a number of words is small.
First, find all the auxiliary data. After that, iterate over every
the possible combination of the words.
At each step, if the combination is valid, we try to update the maximum score.
"""


import collections
from string import ascii_lowercase
from typing import List


class Solution:

    def maxScoreWords(self,
                      words: List[str],
                      letters: List[str],
                      score: List[int]) -> int:
        scores = self._get_scores(score)
        word_scores = self._get_word_scores(words, scores)
        word_letter_counts = self._get_word_counts(words)

        self.letter_count = collections.Counter(letters)
        self.max_score = 0

        def get_score(curr_word, curr_score):
            if curr_word >= len(words):
                return
            word_letter_count = word_letter_counts[curr_word]
            if not word_letter_count - self.letter_count:
                curr_score += word_scores[curr_word]
                self.letter_count -= word_letter_count
                self.max_score = max(self.max_score, curr_score)
                get_score(curr_word+1, curr_score)
                curr_score -= word_scores[curr_word]
                self.letter_count += word_letter_count
            get_score(curr_word+1, curr_score)

        get_score(0, 0)
        return self.max_score

    def _get_scores(self, score):
        return {letter: s for letter, s in zip(ascii_lowercase, score)}

    def _get_word_scores(self, words, scores):
        def get_score(word):
            return sum(map(scores.get, word))

        return list(map(get_score, words))

    def _get_word_counts(self, words):
        return list(map(collections.Counter, words))
