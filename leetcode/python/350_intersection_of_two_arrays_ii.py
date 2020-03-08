class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        i, j = 0, 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        while i < len(nums1) and j < len(nums2):
            left = nums1[i]
            right = nums2[j]
            if left > right:
                j += 1
            elif left < right:
                i += 1
            else:
                result.append(left)
                i += 1
                j += 1
        return result
