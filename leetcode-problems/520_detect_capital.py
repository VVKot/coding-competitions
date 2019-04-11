class Solution:
    def detectCapitalUse(self, word):
        return word.islower() or word.isupper() or word.istitle()
