from itertools import zip_longest
from typing import Generator


class Solution:

    BACKSPACE_CHARACTER = '#'

    def backspaceCompare(self, S: str, T: str) -> bool:
        s_gen = self.get_next(S)
        t_gen = self.get_next(T)
        for s_ch, t_ch in zip_longest(s_gen, t_gen):
            if s_ch != t_ch:
                return False
        return True

    def get_next(self, seq: str) -> Generator[str, None, None]:
        backspace_count = 0
        for ch in reversed(seq):
            if ch == Solution.BACKSPACE_CHARACTER:
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                yield ch
