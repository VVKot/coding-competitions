import itertools


class Solution:

    def countLetters(self, S: str) -> int:
        count = 0
        for _, seq in itertools.groupby(S):
            seq_len = len(list(seq))
            count += seq_len * (seq_len+1) // 2
        return count
