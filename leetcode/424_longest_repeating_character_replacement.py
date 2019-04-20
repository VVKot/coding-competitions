from collections import Counter

class Solution:
    def characterReplacement(self, s, k):
        low = high = 0
        char_counts = Counter()
        for high in range(1, len(s)+1):
            char_counts[s[high-1]] += 1
            most_common_count = char_counts.most_common(1)[0][1]
            if high - low - most_common_count > k:
                char_counts[s[low]] -= 1
                low += 1
        return high - low
