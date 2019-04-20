class Solution:
    def canThreePartsEqualSum(self, A):
        array_sum = sum(A)
        div, mod = divmod(array_sum, 3)
        if mod:
            return False
        curr_sum = 0
        points = [div*2, div]
        for num in A:
            curr_sum += num
            if curr_sum == points[-1]:
                points.pop()
            if not points:
                return True
        return False