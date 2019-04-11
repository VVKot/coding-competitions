class Solution:
    def maxChunksToSorted(self, arr):
        max_so_far = arr[0]
        result = 0
        for i, num in enumerate(arr):
            max_so_far = max(max_so_far, num)
            if max_so_far == i:
                result += 1
        return result
