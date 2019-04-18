from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        len_one_short = len(p) - 1
        p_counter = Counter(p)
        s_counter = Counter(s[:len_one_short])
        for i in range(len_one_short, len(s)):
            s_counter[s[i]] += 1
            seq_start_idx = i - len_one_short
            if s_counter == p_counter:
                result.append(seq_start_idx)
            s_counter[s[seq_start_idx]] -= 1
            if s_counter[s[seq_start_idx]] == 0:
                del s_counter[s[seq_start_idx]]
        return result
