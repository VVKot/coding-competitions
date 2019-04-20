import re


class Solution:
    def checkRecord(self, s):
        return not re.search('A.*A|LLL', s)
