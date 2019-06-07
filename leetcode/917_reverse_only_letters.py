class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        chars = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            is_i_letter = chars[i].isalpha()
            is_j_letter = chars[j].isalpha()
            if is_i_letter and is_j_letter:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
            elif is_i_letter:
                j -= 1
            else:
                i += 1
        return ''.join(chars)
