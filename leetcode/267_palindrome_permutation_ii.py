import collections
import copy
from typing import Counter, List


class Solution:

    def generatePalindromes(self, s: str) -> List[str]:
        if len(s) == 1:
            return [s]
        half_palindromes = []
        char_count = collections.Counter(s)
        if not self._can_make_palindrome(char_count):
            return []
        half_counter = self.get_half_counter(char_count)

        def make_palidrome(curr_seq, counts):
            if not counts:
                half_palindromes.append(curr_seq[::])  # TODO track visited
                return
            for ch in copy.deepcopy(counts):
                curr_seq.append(ch)
                counts[ch] -= 1
                if counts[ch] == 0:
                    del counts[ch]
                make_palidrome(curr_seq, counts)
                curr_seq.pop()
                counts[ch] += 1

        make_palidrome([], half_counter)
        return self.make_palindromes_from_halves(half_palindromes, char_count)

    def make_palindromes_from_halves(self,
                                     half_palindromes: List[List[str]],
                                     char_count: Counter[str]):
        middle_char = self.get_middle_char(char_count)
        return [''.join(half + [middle_char] + half[::-1])
                for half in half_palindromes]

    def _can_make_palindrome(self, char_count: Counter[str]) -> bool:
        seen_odd_count = False
        for count in char_count.values():
            if count & 1:
                if seen_odd_count:
                    return False
                seen_odd_count = True
        return True

    def get_half_counter(self, char_count: Counter[str]) -> Counter[str]:
        half = collections.Counter()  # type: Counter[str]
        for ch, count in char_count.items():
            half_count = count // 2
            if half_count:
                half[ch] = half_count
        return half

    def get_middle_char(self, char_count: Counter[str]) -> str:
        for ch, count in char_count.items():
            if count & 1:
                return ch
        return ""
