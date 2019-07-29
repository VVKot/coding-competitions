from typing import Dict, List


class Solution:

    def partitionLabels(self, S: str) -> List[int]:
        positions = {}  # type: Dict[str, List[int]]
        for i, ch in enumerate(S):
            if ch in positions:
                positions[ch][1] = i
            else:
                positions[ch] = [i, i]
        intervals = list(sorted(positions.values()))
        i, j, N = 0, 0, len(intervals)
        result_intervals = []
        while i < N:
            start, end = intervals[i]
            j += 1
            while j < N and end > intervals[j][0]:
                end = max(end, intervals[j][1])
                j += 1
            result_intervals.append(end-start+1)
            i = j
        return result_intervals
