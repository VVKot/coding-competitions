import collections


class Solution:

    def customSortString(self, S: str, T: str) -> str:
        if not T or not S:
            return T
        result = []
        chars_count = collections.Counter(T)
        for ch in S:
            for _ in range(chars_count[ch]):
                result.append(ch)
            del chars_count[ch]
        for ch, count in chars_count.items():
            for _ in range(count):
                result.append(ch)
        return "".join(result)
