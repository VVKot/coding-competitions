class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = p_ptr = 0
        match = 0
        star = -1
        lenp, lens = len(p), len(s)
        while s_ptr < lens:
            if p_ptr < lenp and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
                s_ptr = s_ptr + 1
                p_ptr = p_ptr + 1
            elif p_ptr < lenp and p[p_ptr] == '*':
                match = s_ptr
                star = p_ptr
                p_ptr = p_ptr+1
            elif (star != -1):
                p_ptr = star+1
                match = match+1
                s_ptr = match
            else:
                return False
        while p_ptr < lenp and p[p_ptr] == '*':
            p_ptr = p_ptr+1

        if p_ptr == lenp:
            return True
        return False
