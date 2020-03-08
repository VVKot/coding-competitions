class Solution(object):

    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left+right) // 2
            res = guess(mid)
            if not res:
                return mid
            if res == -1:
                right = mid - 1
            else:
                left = mid + 1
