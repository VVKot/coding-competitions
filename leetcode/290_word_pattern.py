from typing import Dict, Set


class Solution:

    def wordPattern(self, pattern: str, sequence: str) -> bool:
        words = sequence.split()
        if len(words) != len(pattern):
            return False
        mapping = {}  # type: Dict[str, str]
        used_words = set()  # type: Set[str]
        for letter, word in zip(pattern, words):
            if letter in mapping:
                if mapping[letter] != word:
                    return False
            else:
                if word in used_words:
                    return False
                mapping[letter] = word
                used_words.add(word)
        return True
