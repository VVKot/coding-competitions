class Solution:
	def solveNQueens(self, n):
		def DFS(queens, diag_left, diag_right):
			col = len(queens)
			if col==n:
				result.append(queens)
				return None
			for row in range(n):
				if row not in queens and col-row not in diag_left and col+row not in diag_right: 
					DFS(queens+[row], diag_left+[col-row], diag_right+[col+row])  
		result = []
		DFS([],[],[])
		return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
