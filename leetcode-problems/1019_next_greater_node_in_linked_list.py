# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def nextLargerNodes(self, head):
		result, stack = [], []
		while head:
			while stack and stack[-1][1] < head.val:
				result[stack.pop()[0]] = head.val
			stack.append((len(result), head.val))
			result.append(0)
			head = head.next
		return result