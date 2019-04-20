class Solution(object):

    def get_pivot(self, left, right):
        return (left + right) // 2

    def partition(self, nums, pivot_index, left, right):
        pivot = nums[pivot_index]
        nums[-1], nums[pivot_index] = nums[pivot_index], nums[-1]
        read, write = left, left
        while read <= right:
            if nums[read] >= pivot:
                read += 1
                continue
            if read != write:
                nums[read], nums[write] = nums[write], nums[read]
            read += 1
            write += 1
        nums[write], nums[-1] = nums[-1], nums[write]
        return write, nums

    def findKthLargest(self, nums, k):
        n = len(nums)
        left, right, target = 0, n - 1, n - k
        while True:  # TODO check
            pivot_index = self.get_pivot(left, right)
            final, nums = self.partition(nums, pivot_index, left, right)
            if final == target:
                return nums[final]
            if final > target:
                right = final - 1
            else:
                left = final + 1
