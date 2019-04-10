from heapq import heapify, heappush, heappushpop, heappop

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return float(self.max_heap[0] - self.min_heap[0]) / 2.0
        else:
            return float(self.max_heap[0])

obj = MedianFinder()
obj.addNum(1)
assert obj.findMedian() == 1.0
obj.addNum(2)
assert obj.findMedian() == 1.5
obj.addNum(3)
assert obj.findMedian() == 2.0
obj.addNum(4)
assert obj.findMedian() == 2.5