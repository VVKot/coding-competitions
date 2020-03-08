"""
T: O(NlogN + W**2*N)
S: O(N)

We operate on a sorted list of words to find the correct result.
On each iteration, we find all words which are one letter smaller
then the current one, and check if they have been seen already.
The chain length for the previous word plus one is the current
chain length. The answer is the maximum of those chains.
"""


from typing import Dict, List


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = {}  # type: Dict[str, int]
        for word in sorted(set(words), key=len):
            dp[word] = max(dp.get(word[:i] + word[i+1:], 0) + 1
                           for i in range(len(word)))
        return max(dp.values())
