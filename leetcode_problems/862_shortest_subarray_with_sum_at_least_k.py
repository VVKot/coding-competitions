from collections import deque


class Solution:
    def shortestSubarray(self, A, K):
        N = len(A)
        prefix_sums = [0] * (N + 1)
        for i in range(N):
            prefix_sums[i + 1] = prefix_sums[i] + A[i]
        index_queue = deque()
        result = N + 1
        for i in range(N + 1):
            while index_queue and prefix_sums[i] - prefix_sums[index_queue[0]] >= K:
                result = min(result, i - index_queue.popleft())
            while index_queue and prefix_sums[i] <= prefix_sums[index_queue[-1]]:
                index_queue.pop()
            index_queue.append(i)
        return result if result <= N else -1
