import bisect
from typing import List


class Solution:

    def numSmallerByFrequency(self,
                              queries: List[str],
                              words: List[str]) -> List[int]:
        words_frequency = [self.get_word_frequency(w) for w in words]
        words_frequency.sort()
        N = len(words_frequency)
        smaller_than_num_words = []
        for query in queries:
            query_frequency = self.get_word_frequency(query)
            index = bisect.bisect(words_frequency, query_frequency)
            smaller_than_num_words.append(N-index)
        return smaller_than_num_words

    def get_word_frequency(self, seq):
        N = len(seq)
        smallest = seq[0]
        for i in range(1, N):
            smallest = min(smallest, seq[i])
        return seq.count(smallest)
