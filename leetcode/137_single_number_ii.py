class Solution(object):

    def singleNumber(self, nums):
        seen = set()
        seen_more_than_one = set()
        for num in nums:
            if num in seen_more_than_one:
                continue
            if num in seen:
                seen_more_than_one.add(num)
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]
