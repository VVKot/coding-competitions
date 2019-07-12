class Solution:

    def wordPattern(self, pattern: str, sequence: str) -> bool:
        words = sequence.split()
        if len(words) != len(pattern):
            return False
        if len(set(words)) != len(set(pattern)):
            return False
        return len(set(zip(words, pattern))) == len(set(pattern))
