from string import ascii_lowercase
from typing import List, Dict, Tuple


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}  # type: Dict[Tuple[int, ...], int]
        groups = []  # type: List[List[str]]
        for s in strs:
            letter_count = self.get_letter_count(s)
            group_index = mapping.setdefault(letter_count, len(groups))
            if group_index >= len(groups):
                groups.append([s])
            else:
                groups[group_index].append(s)
        return groups

    def get_letter_count(self, s: str) -> Tuple[int, ...]:
        letter_count = [0] * len(ascii_lowercase)
        for ch in s:
            letter_count[ord(ch) - ord(ascii_lowercase[0])] += 1
        return tuple(letter_count)
