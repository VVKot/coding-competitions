import re
import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^A-Za-z]', ' ', paragraph.lower())
        words = paragraph.split()
        word_count = collections.Counter(words)
        banned_set = set(banned)
        for word, _ in word_count.most_common():
            if word not in banned_set:
                return word
        return ''
