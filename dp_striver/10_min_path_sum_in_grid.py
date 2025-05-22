"""
MINIMUM PATH SUM
================

A country in the shape of 2D grid "GRID"
with "N" rows and "M" columns.
Each point on grid has some cost associated with it.

Find a path from top left (0, 0) to bottom right (N-1, M-1)
which minimizes the sum of the cost of all the numbers
along the path.

Find the minimum path sum of that path.

NOTE:
=====
You can only move down or right at any point in time.
"""


def f(i, j, grid):
	if i == 0 and j == 0:
		return grid[i][j]
	if i < 0 or j < 0:
		return float('inf')

	up = grid[i][j] + f(i, j - 1, grid)
	left = grid[i][j] + f(i - 1, j, grid)
	return min(up, left)


def fm(i, j, grid, dp):
	if i == 0 and j == 0:
		return grid[i][j]
	if i < 0 or j < 0:
		return float('inf')

	if dp[i][j] != -1:
		return dp[i][j]

	up = grid[i][j] + fm(i-1, j, grid, dp)
	left = grid[i][j] + fm(i, j-1, grid, dp)
	dp[i][j] = min(up, left)
	return dp[i][j]


def ftabulation(m, n, grid):
	dp = [[-1 for i in range(n)] for j in range(m)]
	# dp[0][0] = grid[0][0]

	for i in range(m):
		for j in range(n):
			if i == 0 and j == 0:
				dp[i][j] = grid[0][0]
			else:
				up, left = float('inf'), float('inf')
				if i > 0:
					up = grid[i][j] + dp[i-1][j]
				if j > 0:
					left = grid[i][j] + dp[i][j-1]
				dp[i][j] = min(up, left)
	# return dp[-1][-1]
	return dp[m-1][n-1]



def fspaceOptimized(m, n, grid):
	prev = [-1] * n

	for i in range(m):
		cur = [-1] * n
		for j in range(n):
			if i == 0 and j == 0:
				cur[j] = grid[0][0]
			else:
				up, left = float('inf'), float('inf')
				if i > 0:
					up = grid[i][j] + prev[j]
				if j > 0:
					left = grid[i][j] + cur[j-1]
				cur[j] = min(up, left)
		prev = cur
	return cur[-1]



grid = [[5, 9, 6],
		[11, 5, 2]]
m = len(grid)
n = len(grid[0])

print(f(m-1, n-1, grid))

dp = [[-1 for i in range(n)] for j in range(m)]
print(fm(m-1, n-1, grid, dp))

print(ftabulation(m, n, grid))

print(fspaceOptimized(m, n, grid))