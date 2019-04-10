from heapq import heapify, heappush, heappushpop, heappop

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            heappush(self.max_heap, -heappushpop(self.min_heap, num))

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return float(self.min_heap[0])