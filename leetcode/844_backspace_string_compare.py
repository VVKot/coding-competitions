class Solution:

    BACKSPACE_CHARACTER = '#'

    def backspaceCompare(self, S: str, T: str) -> bool:
        len_s, len_t = len(S), len(T)
        i, j = len_s - 1, len_t - 1
        while i > -1 or j > -1:
            i, at_i = self.get_next(S, i)
            j, at_j = self.get_next(T, j)
            if at_i != at_j:
                return False
        return i == j

    def get_next(self, seq, index):
        backspace_count = 0
        while index >= 0:
            curr = seq[index]
            if curr == Solution.BACKSPACE_CHARACTER:
                backspace_count += 1
            else:
                if backspace_count == 0:
                    new_index = index - 1
                    return new_index, curr
                backspace_count -= 1
            index -= 1
        return -1, Solution.BACKSPACE_CHARACTER
