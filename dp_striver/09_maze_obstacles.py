"""
Code Studio - Maze Obstacles
============================

Given a N * M maze with obstacles. Count and return the
number of paths to reach the right-bottom cell from the
top-left cell.

A cell in the given maze has a value -1 if it is a blockage
or dead-end, else 0.

From a given cell, we are allowed to move to cells 
(i+1,j) and (i,j+1) only.

Since answer can be large, print the modulo (10^9 + 7).
"""


def f(i, j, maze):
	if i >= 0 and j >= 0 and maze[i][j] == -1:
		return 0
	if i == 0 and j == 0:
		return 1
	if i < 0 or j < 0:
		return 0
	up = f(i - 1, j, maze)
	left = f(i, j - 1, maze)
	return up + left


def fm(i, j, maze, dp):
	if i >= 0 and j >= 0 and maze[i][j] == -1:
		return 0
	if i == 0 and j == 0:
		return 1
	if i < 0 or j < 0:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]

	up = fm(i - 1, j, maze, dp)
	left = fm(i, j - 1, maze, dp)
	dp[i][j] = up + left
	return dp[i][j]


def f_tabulation(m, n, maze):
	dp = [[-1 for i in range(n)] for j in range(m)]

	for i in range(m):
		for j in range(n):
			if maze[i][j] == -1:
				dp[i][j] = 0
			elif i == 0 and j == 0:
				dp[i][j] = 1
			else:
				up = 0
				left = 0
				if i > 0:
					up = dp[i-1][j]
				if j > 0:
					left = dp[i][j-1]
				dp[i][j] = up + left
	return dp[-1][-1]



def f_spaceOptimized(m, n, maze):
	prev = [0] * n

	for i in range(m):
		cur = [0] * n
		for j in range(n):
			if maze[i][j] == -1:
				cur[j] = 0
			elif i == 0 and j == 0:
				cur[j] = 1
			else:
				up, left = 0, 0
				if i > 0:
					up = prev[j]
				if j > 0:
					left = cur[j-1]
				cur[j] = up + left
		prev = cur
	return prev[-1]



maze = [[0, 0, 0],
		[0,-1, 0],
		[0, 0, 0]]

m = len(maze)
n = len(maze[0])
print(f(m-1, n-1, maze))

dp = [[-1 for i in range(n)] for j in range(m)]
print(fm(m-1, n-1, maze, dp))

print(f_tabulation(m, n, maze))

print(f_spaceOptimized(m, n, maze))