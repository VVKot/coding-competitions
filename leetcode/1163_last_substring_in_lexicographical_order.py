from typing import List


class Solution:

    def lastSubstring(self, s: str) -> str:
        last_letter = ""
        last_letter_occurences = []  # type: List[int]
        self.s = s
        for i, ch in enumerate(s):
            if ch > last_letter:
                last_letter = ch
                last_letter_occurences = [i]
            elif ch == last_letter:
                last_letter_occurences.append(i)
        return max(s[i:] for i in last_letter_occurences)
