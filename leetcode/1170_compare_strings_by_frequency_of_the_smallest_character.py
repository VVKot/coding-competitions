import bisect
from typing import List


class Solution:

    def numSmallerByFrequency(self,
                              queries: List[str],
                              words: List[str]) -> List[int]:
        words_frequency = sorted(self.get_freq(w) for w in words)
        return [len(words) - bisect.bisect(words_frequency, self.get_freq(q))
                for q in queries]

    def get_freq(self, seq):
        return seq.count(min(seq))
