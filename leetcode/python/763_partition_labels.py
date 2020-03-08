from typing import List


class Solution:

    def partitionLabels(self, S: str) -> List[int]:
        last_occurences = {ch: i for i, ch in enumerate(S)}
        partitions = []
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last_occurences[ch])
            if i == end:
                partitions.append(end-start+1)
                start = i+1
        return partitions
