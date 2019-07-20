from typing import List
from sys import maxsize as maxint


class Solution:

    def minHeightShelves(self,
                         books: List[List[int]],
                         shelf_width: int) -> int:
        if not books:
            return 0
        if not self.are_books_valid(books, shelf_width):
            return -1
        N = len(books)
        heights = [0] + [maxint] * N
        for book in range(1, N+1):
            width, height = books[book-1]
            curr_width = shelf_width
            curr_height = 0
            for prev_book in range(book, 0, -1):
                prev_width, prev_height = books[prev_book-1]
                curr_width -= prev_width
                if curr_width < 0:
                    break
                curr_height = max(curr_height, prev_height)
                heights[book] = min(heights[book],
                                    curr_height + heights[prev_book-1])
        return heights[N]

    def are_books_valid(self, books, shelf_width):
        for width, _ in books:
            if width > shelf_width:
                return False
        return True
