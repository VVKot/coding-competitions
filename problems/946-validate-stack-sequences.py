class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pp_idx = 0
        for ps in pushed:
            if ps != popped[pp_idx]:
                stack.append(ps)
            else:
                pp_idx += 1
                while pp_idx < len(popped) and stack and popped[pp_idx] == stack[-1]:
                    stack.pop()
                    pp_idx += 1
        return False if stack else True
