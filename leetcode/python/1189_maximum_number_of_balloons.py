import collections


class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = collections.Counter(text)
        balloon_count = collections.Counter('balloon')
        max_balloons = 1 << 32
        for ch, count in balloon_count.items():
            curr_balloons = text_count[ch] // count
            max_balloons = min(max_balloons, curr_balloons)
        return max_balloons
