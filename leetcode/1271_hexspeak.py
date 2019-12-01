"""
T: O(N)
S: O(N)

Do as the description says.
"""


class Solution:

    def toHexspeak(self, num: str) -> str:
        allowed_chars = {"A", "B", "C", "D", "E", "F", "I", "O"}
        hex_representation = hex(int(num))[2:].upper()
        result = hex_representation.replace('0', 'O').replace('1', 'I')
        return result if all(ch in allowed_chars for ch in result) else "ERROR"
