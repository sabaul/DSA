"""
++++++++++++++++++++++++++++++++++++++++++++++++++++
DP ON GRIDS VARIATIONS
++++++++++++++++++++++++++++++++++++++++++++++++++++
1. Fixed starting point and fixed ending point
	-> (0, 0) --> (n-1)(m-1)
2. Fixed starting point and variable ending point
	-> Question 11
3. Variable starting point and variable ending point
	-> This question (question 12)
++++++++++++++++++++++++++++++++++++++++++++++++++++



CODE STUDIO -> max path sum in matrix
-------------------------------------

Given an N*M matrix filled with interger numbers.

Find the maximum sum that can be obtained from a path starting
from any cell in the first row to any cell in the last row.

From a cell in a row, you can move to another cell directly
below that row, or diagonally below left or right.
e.g. from a cell (row, col), we can move in 3 directions:
	 1. down: (row+1, col)
	 2. down left diagonal: (row+1, col-1)
	 3. down right diagonal: (row+1, col+1)

matrix = [[1, 2, 10, 4],
		  [100, 3, 2, 1],
		  [1, 1, 20, 2],
		  [1, 2, 2, 1]]

ans = 2->100->1->2 ====> 105


SOLUTION APPROACHES
===================
* Greedy won't work as it's not uniform, we might miss on something
  more valuable if we approach it greedily

SO TRY ALL POSSIBLE PATHS --> RECURSION
AND TAKE THE BEST OUT OF THEM

RECURSION STEPS
---------------
1. Express in terms of indices
	-> (i, j), base case
2. Explore all paths (down, left diagonal, right diagonal)
3. Max among all paths


say our input matrix (4*4),
we need to check all the ending points at row 4
and find the maximum out of them

i.e. ANS = max(f(n-1, 0), f(n-1, 1), f(n-1, 2), f(n-1, 3))

m = # cols
for j in range(m):
	f(n-1, j)


f(i,j) -> max path sum to reach (i,j) from any cell in 1st row

base case ==> destination OR out of bounds

def f(i, j):

	# base case done
	if i == 0:
		return matrix[i][j]
	if j < 0 or j > (# cols):
		return float('-inf')

	# explore all the paths
	up = matrix[i][j] + f(i-1,j)
	up_left = matrix[i][j] + f(i-1, j-1)
	up_right = matrix[i][j] + f(i-1, j+1)

	return max(up, up_left, up_right)
"""


def recursion(n, m, matrix):

	def f(i, j):
		if j < 0 or j >= m:
			return float('-inf')
		if i == 0:
			return matrix[i][j]

		# explore all paths
		up = matrix[i][j] + f(i-1, j)
		up_left = matrix[i][j] + f(i-1, j-1)
		up_right = matrix[i][j] + f(i-1, j+1)
		return max(up, up_left, up_right)

	maxval = float('-inf')
	for j in range(m):
		maxval = max(maxval, f(n-1, j))
	return maxval


def memoization(n, m, matrix):
	dp = [[-1 for i in range(m)] for j in range(n)]

	def f(i, j):
		if j < 0 or j >= m:
			return float('-inf')
		if i == 0:
			return matrix[i][j]

		if dp[i][j] != -1:
			return dp[i][j]

		# explore all paths
		up = matrix[i][j] + f(i-1, j)
		up_left = matrix[i][j] + f(i-1, j-1)
		up_right = matrix[i][j] + f(i-1, j+1)
		dp[i][j] = max(up, up_left, up_right)
		return dp[i][j]

	maxval = float('-inf')
	for j in range(m):
		maxval = max(maxval, f(n-1, j))
	return maxval


def tabulation(n, m, matrix):
	dp = [[-1 for i in range(m)] for j in range(n)]

	for j in range(m):
		dp[0][j] = matrix[0][j]

	for i in range(1, n):
		for j in range(0, m):
			up = matrix[i][j] + dp[i-1][j]
			up_left = matrix[i][j]
			if (j-1) >= 0:
				up_left += dp[i-1][j-1]
			up_right = matrix[i][j]
			if (j+1) < m:
				up_right += dp[i-1][j+1]

			dp[i][j] = max(up, up_left, up_right)

	# return max(dp[-1]) # return the max from last dp row
	res = dp[-1][0]
	for j in range(1, n):
		res = max(res, dp[-1][j])
	return res


def spaceOptimized(n, m, matrix):
	# prev = [-1 for i in range(m)]
	# for j in range(m):
	# 	prev[j] = matrix[0][j]
	prev = [num for num in matrix[0]]
	cur = [-1 for i in range(m)]
	
	for i in range(1, n):
		for j in range(0, m):
			up = matrix[i][j] + prev[j]
			
			up_left = matrix[i][j]
			if (j-1) >= 0: up_left += prev[j-1]

			up_right = matrix[i][j]
			if (j+1) < m: up_right += prev[j+1]

			cur[j] = max(up, up_left, up_right)
		prev = cur

	# res = prev[0]
	# for j in range(1, m):
	# 	res = max(res, prev[j])
	# return res
	return max(prev)



matrix = [[1, 2, 10, 4],
		  [100, 3, 2, 1],
		  [1, 1, 20, 2],
		  [1, 2, 2, 1]]

n = len(matrix)
m = len(matrix[0])

print(recursion(n, m, matrix))
print(memoization(n, m, matrix))
print(tabulation(n, m, matrix))
print(spaceOptimized(n, m, matrix))