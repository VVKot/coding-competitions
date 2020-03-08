from heapq import nsmallest


class Solution(object):

    def kClosest(self, points, K):
        return nsmallest(K, points, lambda x: x[0]**2 + x[1]**2)
