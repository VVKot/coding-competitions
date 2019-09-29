class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append([ch, 1])
            else:
                prev_ch, prev_count = stack[-1]
                if prev_ch != ch:
                    stack.append([ch, 1])
                else:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
        return ''.join(ch * count for ch, count in stack)
