from collections import Counter
from typing import List


class Solution(object):

    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        pattern_len = len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[:pattern_len-1])
        for i in range(len(s)-pattern_len+1):
            next_char = i + pattern_len - 1
            s_counter[s[next_char]] += 1
            if s_counter == p_counter:
                result.append(i)
            s_counter[s[i]] -= 1
            if s_counter[s[i]] == 0:
                del s_counter[s[i]]
        return result
