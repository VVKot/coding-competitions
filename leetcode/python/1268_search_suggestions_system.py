"""
T: O(NlogN)
S: O(1)

We can solve the question without a trie. First, we sort all products.
After that, we can find the first next suggestion position using binary search.
The only thing left is to check the next two following products. We can reuse
the previous location of the suggestion for further searches since we know
it will only increase.
"""

import bisect
from typing import List


class Solution:

    def suggestedProducts(self,
                          products: List[str],
                          searchWord: str) -> List[List[str]]:
        products.sort()
        prefix_position = 0
        prefix = ''
        suggestions = []
        for ch in searchWord:
            prefix += ch
            prefix_position = bisect.bisect_left(
                products, prefix, prefix_position)
            suggestions.append(
                [p for p in products[prefix_position:prefix_position+3]
                 if p.startswith(prefix)])
        return suggestions
