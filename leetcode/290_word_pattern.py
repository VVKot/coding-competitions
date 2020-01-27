"""
T: O(P + S)
S: O(P + S)

This solution is based on the following observations:
1. If number of words is different from the length of pattern
2. Or if number of unique words is different from number of unique letters
3. Or if number of unique mappings is different from number of unique letters
the answer is false. Otherwise, it is true, no matter the exact mapping from
letters to words.
"""

class Solution:

    def wordPattern(self, pattern: str, sequence: str) -> bool:
        words = sequence.split()
        if len(words) != len(pattern):
            return False
        if len(set(words)) != len(set(pattern)):
            return False
        return len(set(zip(words, pattern))) == len(set(pattern))
