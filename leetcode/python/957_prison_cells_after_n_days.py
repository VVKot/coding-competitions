from typing import Dict, List, Tuple


class Solution:

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen_at_day = {}  # type: Dict[Tuple[int, ...], int]
        K = len(cells)

        while N:
            key = tuple(cells)
            if key in seen_at_day:
                N %= seen_at_day[key] - N
            seen_at_day[key] = N
            if N >= 1:
                N -= 1
                cells = [int(i > 0 and i < K-1 and cells[i-1] == cells[i+1])
                         for i in range(K)]
        return cells
