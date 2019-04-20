class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        g.sort()
        s.sort()
        child_index = 0
        for size in s:
            if child_index == len(g):
                break
            if size >= g[child_index]:
                result += 1
                child_index += 1
        return result
