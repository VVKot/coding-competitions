class Solution:

    def decodeString(self, s: str) -> str:
        curr, mult, stack = '', 0, []
        for ch in s:
            if ch.isalpha():
                curr += ch
            elif ch.isdigit():
                mult = mult * 10 + int(ch)
            elif ch == '[':
                stack.append((mult, curr))
                mult, curr = 0, ''
            else:
                times, prev = stack.pop()
                curr = prev + curr * times
        return curr
