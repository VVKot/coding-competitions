class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for ch in s:
            if stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        return ''.join(ch * count for ch, count in stack)
