from collections import Counter


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = []
        if not A:
            return result
        counters = [Counter(word) for word in A]
        insersect = counters[0]
        for i in range(1, len(counters)):
            insersect &= counters[i]
        for k, v in insersect.items():
            for _ in range(v):
                result.append(k)
        return result
