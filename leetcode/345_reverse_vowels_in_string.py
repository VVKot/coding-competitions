class Solution:

    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        char_len = len(chars)
        left, right = 0, char_len - 1
        while left < char_len and not self.is_vowel(chars[left]):
            left += 1
        while right >= 0 and not self.is_vowel(chars[right]):
            right -= 1

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            while left < char_len and not self.is_vowel(chars[left]):
                left += 1
            while right >= 0 and not self.is_vowel(chars[right]):
                right -= 1
        return ''.join(chars)

    def is_vowel(self, ch: str) -> bool:
        return ch.lower() in {'a', 'e', 'i', 'o', 'u'}
