class Solution(object):
	def numIslands(self, grid):
		n = len(grid)
		m = len(grid[0])

		if not grid:
			return 0

		count = 0
		for row in range(n):
			for col in range(m):
				if grid[row][col]:
					count += 1
					self.traverse(grid, row, col, n, m)
		return count

	def traverse(self, grid, row, col, n, m):
		if (row < 0) or (col < 0) or (row == n) or (col == m):
			return 0

		if grid[row][col] == 0:
			return 0

		grid[row][col] = 0

		self.traverse(grid, row+1, col, n, m)
		self.traverse(grid, row-1, col, n, m)
		self.traverse(grid, row, col+1, n, m)
		self.traverse(grid, row, col-1, n, m)

		return 1