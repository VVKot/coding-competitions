from typing import Dict, List


class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        buckets = {}  # type: Dict[int, int]
        dist = t+1
        for i, num in enumerate(nums):
            bucket_id = self.get_bucket_id(num, dist)
            if bucket_id in buckets:
                return True
            if bucket_id-1 in buckets:
                if abs(num - buckets[bucket_id-1]) < dist:
                    return True
            if bucket_id+1 in buckets:
                if abs(num - buckets[bucket_id+1]) < dist:
                    return True
            buckets[bucket_id] = num
            if i >= k:
                prev_id = self.get_bucket_id(nums[i-k], dist)
                del buckets[prev_id]
        return False

    def get_bucket_id(self, num: int, bucket_size: int) -> int:
        return num // bucket_size
