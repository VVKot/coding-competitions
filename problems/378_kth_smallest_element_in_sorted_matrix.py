from heapq import heappush, heappop, heapreplace, heapify


class Solution(object):
    def kthSmallest(self, matrix, k):
        m_heap = [(row[0], row, 1) for row in matrix]
        heapify(m_heap)
        for _ in range(k - 1):
            _, row, row_pos = m_heap[0]
            if row_pos < len(row):
                heapreplace(m_heap, (row[row_pos], row, row_pos + 1))
            else:
                heappop(m_heap)

        return m_heap[0][0]