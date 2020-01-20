"""
T: O((S-P) * P)
S: O(S-P)

Brute-force solution - find all possible substrings, remember seen ones, and
add to the results those that we have seen before.
"""

from typing import List, Set


class Solution:

    DNA_LEN = 10

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < self.DNA_LEN:
            return []
        repeated_dna_sequences = set()
        dna_sequences = set()  # type: Set[str]
        for i in range(len(s) - self.DNA_LEN + 1):
            current_sequence = s[i:i + self.DNA_LEN]
            if current_sequence in dna_sequences:
                repeated_dna_sequences.add(current_sequence)
            else:
                dna_sequences.add(current_sequence)
        return list(repeated_dna_sequences)
