from typing import List, Set


class Solution:

    def maxLength(self, arr: List[str]) -> int:
        result = [set()]  # type: List[Set]
        for seq in arr:
            if len(set(seq)) < len(seq):
                continue
            seq_chars = set(seq)
            for prev_seq_chars in result:
                if seq_chars & prev_seq_chars:
                    continue
                result.append(seq_chars | prev_seq_chars)
        return max(len(seq_chars) for seq_chars in result)
