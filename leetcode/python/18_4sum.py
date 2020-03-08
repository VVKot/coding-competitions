from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def find_n_sum(left: int,
                     right: int,
                     target: int,
                     N: int,
                     result: List[int],
                     results: List[List[int]]):
            if right-left+1 < N or N < 2:
                return
            if target < nums[left]*N or target > nums[right]*N:
                return
            if N == 2:
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(left, right+1):
                    if i == left or (i > left and nums[i-1] != nums[i]):
                        find_n_sum(i+1, right, target -
                                 nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        four_sums = []  # type: List[List[int]]
        find_n_sum(0, len(nums)-1, target, 4, [], four_sums)
        return four_sums
