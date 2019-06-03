import collections
import string


class Solution:

    def customSortString(self, S: str, T: str) -> str:
        letter_count = collections.Counter(T)
        other_letters = set(string.ascii_lowercase) - set(S)
        order = S + ''.join(other_letters)
        result = []
        for letter in order:
            result.extend([letter * letter_count[letter]])
        return ''.join(result)
