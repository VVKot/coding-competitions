import List


class BinarySearch:

    def search(nums: List[int], val: int) -> int:
        index = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) // 2
            at_mid = nums[mid]
            if at_mid < val:
                lo = mid+1
            else:
                if at_mid == val:
                    index = mid
                hi = mid-1
        return index
