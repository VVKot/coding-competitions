class Solution:
	def hasAlternatingBits(self, n):
		if not n:
			return False
		prev = None
		while n:
			if prev is not None and prev == n & 1:
				return False
			else:
				prev = n & 1
				n >>= 1
		return True