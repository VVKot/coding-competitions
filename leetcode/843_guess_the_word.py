import random


class Solution:

    MAX_CALLS = 10

    def findSecretWord(self, wordlist, master):
        L = len(wordlist[0])
        for _ in range(Solution.MAX_CALLS):
            choice = random.choice(wordlist)
            correct = master.guess(choice)
            if correct == L:
                break
            wordlist = list(filter(lambda word: self.is_at_distance(
                choice, word, L - correct), wordlist))

    def is_at_distance(self, first, second, dist):
        return sum(a != b for a, b in zip(first, second)) == dist
