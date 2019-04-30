from typing import List


class Solution:

    def is_word_smaller(self, word1: str, word2: str):
        l1, l2 = len(word1), len(word2)
        for i in range(min(l1, l2)):
            ch1 = word1[i]
            ch2 = word2[i]
            diff = self.order_dict[ch2] - self.order_dict[ch1]
            if diff < 0:
                return False
            if diff > 0:
                return True
        return l1 <= l2

    def set_order(self, order: str):
        self.order_dict = {ch: i for i, ch in enumerate(order)}

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.set_order(order)
        for i in range(1, len(words)):
            if not self.is_word_smaller(words[i-1], words[i]):
                return False
        return True
