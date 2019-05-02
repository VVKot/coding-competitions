from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        # more than median
        self.min_heap = []
        # less than median
        self.max_heap = []

    def addNum(self, num: int) -> None:
        len_min = len(self.min_heap)
        len_max = len(self.max_heap)
        if len_min == len_max:
            max_num = heappushpop(self.min_heap, num)
            heappush(self.max_heap, -max_num)
        else:
            min_num = heappushpop(self.max_heap, -num)
            heappush(self.min_heap, -min_num)

    def findMedian(self) -> float:
        len_min = len(self.min_heap)
        len_max = len(self.max_heap)
        if len_max == len_min:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
