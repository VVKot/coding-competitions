from typing import List


class Solution:

    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        puzzles = set()
        N = len(phrases)
        for i in range(N):
            first = phrases[i].split()
            for j in range(N):
                if i != j:
                    second = phrases[j].split()
                    if first[-1] == second[0]:
                        puzzle = ' '.join(first + second[1:])
                        puzzles.add(puzzle)
        result = list(puzzles)
        result.sort()
        return result
