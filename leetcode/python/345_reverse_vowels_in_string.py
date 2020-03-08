class Solution:

    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        left, right = 0, len(chars) - 1
        vowels = set('aeiouAEIOU')
        while left < right:
            if chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            if not chars[left] in vowels:
                left += 1
            if not chars[right] in vowels:
                right -= 1
        return ''.join(chars)
