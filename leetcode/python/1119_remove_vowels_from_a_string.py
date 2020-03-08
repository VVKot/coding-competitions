class Solution:

    def removeVowels(self, S: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return ''.join(s for s in S if s not in vowels)
