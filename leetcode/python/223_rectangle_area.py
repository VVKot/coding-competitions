class Solution:

    def computeArea(self,
                    A: int,
                    B: int,
                    C: int,
                    D: int,
                    E: int,
                    F: int,
                    G: int,
                    H: int) -> int:
        left = max(A, E)
        right = max(left, min(C, G))
        bottom = max(B, F)
        top = max(bottom, min(D, H))
        first = self.get_area(A, B, C, D)
        second = self.get_area(E, F, G, H)
        intersection = self.get_area(left, bottom, right, top)
        return first + second - intersection

    def get_area(self,
                 left: int,
                 bottom: int,
                 right: int, top: int) -> int:
        return (right - left) * (top - bottom)
