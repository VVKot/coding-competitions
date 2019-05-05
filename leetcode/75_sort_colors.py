from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, two = 0, 0, len(nums) - 1
        while one <= two:
            curr = nums[one]
            if curr == 1:
                one += 1
            elif curr == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1
