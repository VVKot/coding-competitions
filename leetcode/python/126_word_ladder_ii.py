class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        result = []
        def dfs(curr, curr_path):
            for word in wordList:
                if word in curr_path:
                    continue
                if not self.is_near(word, curr):
                    continue
                if word == endWord:
                    result.append(curr_path + [word])
                    return
                dfs(word, curr_path + [word])
        dfs(beginWord, [beginWord])
        if not result:
            return result
        min_len = min([len(x) for x in result])
        return [x for x in result if len(x) == min_len]

    def is_near(self, word1, word2):
        diff = 0
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

s = Solution()
s.findLadders(
"hit",
"cog",
["hot","dot","dog","lot","log","cog"])