import string
from typing import Dict, List


class Solution:

    MAX_WIDTH = 100

    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        char_widths = self._get_char_widths(widths)
        number_of_lines = 1
        current_width = 0
        for char in S:
            width = char_widths[char]
            current_width += width
            if current_width > self.MAX_WIDTH:
                number_of_lines += 1
                current_width = width
        return [number_of_lines, current_width]

    def _get_char_widths(self,  widths: List[int]) -> Dict[str, int]:
        return {char: width for char, width in
                zip(string.ascii_lowercase, widths)}
