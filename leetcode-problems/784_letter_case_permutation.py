class Solution:
    def letterCasePermutation(self, S):
        result = ['']
        for ch in S:
            if ch.isalpha():
                result = [
                    pre+suf for pre in result for suf in [ch.upper(), ch.lower()]]
            else:
                result = [pre+ch for pre in result]
        return result
