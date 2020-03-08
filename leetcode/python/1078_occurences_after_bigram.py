from typing import List


class Solution:

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        words = text.split()
        for i in range(2, len(words)):
            if words[i - 2] == first and words[i - 1] == second:
                result.append(words[i])
        return result
