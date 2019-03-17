class Solution:
    def decodeString(self, s: str) -> str:
        curr = ''
        stack = []
        times = 0
        for ch in s:
            if ch == '[':
                stack.append((curr, times))
                curr = ''
                times = 0
            elif ch == ']':
                before, before_times = stack.pop()
                curr = before + curr * before_times
            elif ch.isdigit():
                times = times * 10 + int(ch)
            else:
                curr += ch
        return curr
