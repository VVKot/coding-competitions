class Solution:

    def longestDecomposition(self, text: str) -> int:
        result = 0
        N = len(text)
        left = 0
        right = N-1
        while left <= right:
            i = left
            j = right
            while i < j and text[left:i+1] != text[j:right+1]:
                i += 1
                j -= 1
            if i < j and text[left:i+1] == text[j:right+1]:
                if left == right:
                    result += 1
                else:
                    result += 2
            else:
                result += 1
                break
            left = i+1
            right = j-1
        return result
