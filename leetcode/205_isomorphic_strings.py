from typing import Dict, Set


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        swaps = {}  # type: Dict[str, str]
        targets = set()  # type: Set[str]
        for ch_s, ch_t in zip(s, t):
            if ch_s in swaps:
                if swaps[ch_s] != ch_t:
                    return False
            else:
                if ch_t in targets:
                    return False
                targets.add(ch_t)
                swaps[ch_s] = ch_t
        return True
