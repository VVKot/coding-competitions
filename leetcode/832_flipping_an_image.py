from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = self.get_flipped_image(A)
        A = self.get_inverted_image(A)
        return A

    def get_flipped_image(self, A):
        return [list(reversed(line)) for line in A]

    def get_inverted_image(self, A):
        return [self.get_reversed_line(line) for line in A]

    def get_reversed_line(self, line):
        return [0 if x else 1 for x in line]
