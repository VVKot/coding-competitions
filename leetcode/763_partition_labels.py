from typing import List


class Solution:

    def partitionLabels(self, S: str) -> List[int]:
        result = []
        last = {ch: i for i, ch in enumerate(S)}
        start = j = 0
        for i, ch in enumerate(S):
            j = max(j, last[ch])
            if i == j:
                result.append(i-start+1)
                start = i + 1
        return result
