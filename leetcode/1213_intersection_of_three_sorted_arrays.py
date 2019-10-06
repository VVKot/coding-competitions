from typing import List


class Solution:

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        intersection = []
        i = j = k = 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                intersection.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                if arr1[i] < arr2[j]:
                    i += 1
                elif arr2[j] < arr3[k]:
                    j += 1
                else:
                    k += 1
        return intersection
