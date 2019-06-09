from typing import List


class Solution:
    def findAndReplacePattern(self,
                              words: List[str],
                              pattern: str) -> List[str]:
        def is_match(word):
            mapping = dict()
            used = set()
            for wch, pch in zip(word, pattern):
                if wch in mapping:
                    if mapping[wch] != pch:
                        return False
                else:
                    if pch in used:
                        return False
                    mapping[wch] = pch
                    used.add(pch)
            return True

        return [w for w in words if is_match(w)]
