import heapq
from typing import List


def sort_k_messed_array(arr: List[int], k: int) -> List[int]:
    N = len(arr)
    sliding_window = arr[:min(k+1, N)]
    heapq.heapify(sliding_window)
    write = 0
    read = k + 1
    while sliding_window:
        min_elem = heapq.heappop(sliding_window)
        arr[write] = min_elem
        write += 1
        if read < N:
            heapq.heappush(sliding_window, arr[read])
            read += 1
    return arr
