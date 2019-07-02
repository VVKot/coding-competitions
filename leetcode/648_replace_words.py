import collections
import functools
from typing import List


class RootTrie:

    def replaceWords(self, roots: List[str], sentence: str) -> str:
        def Trie():
            return collections.defaultdict(Trie)
        trie = Trie()
        END_SYMBOL = '*'

        for root in roots:
            functools.reduce(dict.__getitem__, root, trie)[END_SYMBOL] = root

        def replace(word):
            curr_trie = trie
            for letter in word:
                if letter not in curr_trie or END_SYMBOL in curr_trie:
                    break
                curr_trie = curr_trie[letter]
            return curr_trie.get(END_SYMBOL, word)

        return " ".join(map(replace, sentence.split()))
