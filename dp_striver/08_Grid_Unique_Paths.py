"""
DP on Grids/2D Matrix
=====================
-> count paths
-> count paths with obstacle
-> min path sum
-> max path sum
-> triangle problem
-> 2 start point


Q -> TOTAL UNIQUE PATHS
=======================
You are present at point A, which is the top-left cell of an
MxN matrix, your destination is point B, which is the bottom
right cell of the same matrix.

Find the total number of unique paths from point A to B.

Matrix Dimension = M x N
Find total no. of unique paths from Matrix[0][0] to Matrix[M-1][N-1]
"""

"""
All possible ways: RECURSION
----------------------------

How to write recursion:
1. express everything in terms of indices
2. do all stuff at the index
3. sum up all ways (for counting)
   max/min (if max/min is required)
"""

"""
Solution approach
-----------------

Step 1 -> Express problem in terms of indices
======
f(i, j) -> no. of unique ways to go from (0, 0) to (i, j)

we need -> f(m-1, n-1)

base case:
	if reached your destination  -> return 1
	if haven't reach destination -> return 0

if i == 0 and j == 0:
	return 1

if out of bounds -> return 0
if i < 0 or j < 0:
	return 0


Step 2 -> Do all stuffs on that particular indices
======
up = f(i - 1, j)   -> move up
left = f(i, j - 1) -> move left

Step 3 -> Sum up (if required total number of ways)
======
return up + left



MEMOIZATION TO TABULATION
-------------------------
1. Declare base case
2. Express all states in for loop
3. Copy the recurrence and write
"""


def f(i, j):
	if i == 0 and j == 0:
		return 1
	if i < 0 or j < 0:
		return 0

	up = f(i - 1, j)
	left = f(i, j - 1)
	return up + left


def memoized_f(i, j, dp):
	if i == 0 and j == 0:
		return 1
	if i < 0 or j < 0:
		return 0

	if dp[i][j] != -1:
		return dp[i][j]

	up = memoized_f(i - 1, j, dp)
	left = memoized_f(i, j - 1, dp)
	dp[i][j] = up + left
	return dp[i][j]

def fm(m, n):
	dp = [[-1 for i in range(n)] for j in range(m)]
	# print(len(dp), len(dp[0]))
	return memoized_f(m - 1, n - 1, dp)


def fiterative(m, n):
	dp = [[0 for i in range(n)] for j in range(m)]
	# dp[0][0] = 1

	for i in range(0, m):
		for j in range(0, n):
			if i == 0 and j == 0:
				dp[0][0] = 1
			else:
				up, left = 0, 0
				if i > 0:
					up = dp[i-1][j]
				if j > 0:
					left = dp[i][j-1]
				dp[i][j] = up + left
	return dp[m-1][n-1]


# def f_space_optimized(m, n):
# 	dp = [0 for i in range(n)]

# 	for i in range(m):
# 		temp = [0 for i in range(n)]
# 		for j in range(n):
# 			if i == 0 and j == 0:
# 				# do something
# 				temp[i] = 1
# 			if j == 0:
# 				temp[j] = dp[j]
# 			else:
# 				temp[j] = dp[j] + temp[j - 1]
# 		dp = temp
# 	return dp[-1]

def striver_space_optimized(m, n):
	prev = [0] * n

	for i in range(m):
		cur = [0] * n
		for j in range(n):
			if i == 0 and j == 0:
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



m = 3; n = 3;
print(f"f: {f(m - 1, n - 1)}")
print(f"fm: {fm(m, n)}")
print(f"Iterative: {fiterative(m, n)}")
# print(f"Space optimized: {f_space_optimized(m, n)}")
print(f"Striver space optimized: {striver_space_optimized(m, n)}")