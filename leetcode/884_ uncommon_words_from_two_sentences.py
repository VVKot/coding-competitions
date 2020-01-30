class Solution:

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        all_words = collections.Counter(A.split()) + collections.Counter(B.split())
        return [word for word, count in all_words.items() if count == 1]
