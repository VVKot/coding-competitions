class Solution:

    def calculateTime(self, keyboard: str, word: str) -> int:
        indices = {ch: i for i, ch in enumerate(keyboard)}
        prev = keyboard[0]
        time = 0
        for ch in word:
            time += abs(indices[ch] - indices[prev])
            prev = ch
        return time
