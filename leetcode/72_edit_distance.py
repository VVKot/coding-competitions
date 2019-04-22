class Solution:

    def minDistance(self, word1, word2, cache={}):
        cache_key = (word1, word2)
        if cache_key in cache:
            return cache[cache_key]
        result = 0
        if not word1 or not word2:
            result = len(word1) + len(word2)
            cache[cache_key] = result
            return result
        char1 = word1[0]
        char2 = word2[0]
        if char1 == char2:
            result = self.minDistance(word1[1:], word2[1:], cache)
        else:
            first = self.minDistance(word1[1:], word2, cache)
            second = self.minDistance(word1, word2[1:], cache)
            third = self.minDistance(word2[0] + word1[1:], word2, cache)
            fourth = self.minDistance(word1, word1[0] + word2[1:], cache)
            result = min([first, second, third, fourth]) + 1
        cache[cache_key] = result
        return result
