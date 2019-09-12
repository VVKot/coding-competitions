import bisect
from typing import List


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        if index == len(letters):
            index = 0
        return letters[index]
