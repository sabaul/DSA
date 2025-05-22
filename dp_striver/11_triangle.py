"""
We might have variable starting point and variable enging point
------------------------
CODE STUDIO --> TRIANGLE
========================

Given a array/list "TRIANGLE". Task is to return the minimum
path sum to reach from the top to the bottom row.

The triangle array will have N rows and the i-th row,
where 0 <= i < N will have (i+1) elements.

You can move only to the adjacent number of row below each step.
e.g. -> if you are at index j in row i
	 -> then you can move to i or (i+1) index in row (j+1) in each step

#row
0   -> 1
1   -> 2 3
2   -> 3 6 7
3   -> 8 9 6 10

++++++++++++++++++++++++++++++++++++++++++++++
Try out all the paths => Recursion => min(sum)
++++++++++++++++++++++++++++++++++++++++++++++
1. represent problem in terms of index --> (i, j) -> row, col
	-> f(i, j) --> start from (0, 0) and go to the (n-1)th row
			   --> Min path sum from (0, 0) to (i, j)
2. explore all paths (down/diagonally right)
	-> go down 				 => (i+1, j)
	-> diagonally down right => (i+1, j+1)
3. Min of all paths
++++++++++++++++++++++++++++++++++++++++++++++

start from (0, 0)
m = no. of rows
base case = (n-1)th row
			which ever column you reach, return that j'th value

"""

def f(i, j, n, arr):
	if i == n-1: return arr[n-1][j]

	down = arr[i][j] + f(i+1, j, n, arr)
	diagonal = arr[i][j] + f(i+1, j+1, n, arr)
	return min(down, diagonal)

def f_memoized(i, j, n, arr, dp):
	if i == n-1:
		return arr[n-1][j]
	if dp[i][j] != -1:
		return dp[i][j]

	down = arr[i][j] + f_memoized(i+1, j, n, arr, dp)
	diag = arr[i][j] + f_memoized(i+1, j+1, n, arr, dp)
	
	dp[i][j] = min(down, diag)
	return dp[i][j]

def fm(n, arr):
	dp = [[-1 for i in range(n)] for j in range(n)]
	return f_memoized(0, 0, n, arr, dp)

def f_tabular(n, arr):
	dp = [[-1 for i in range(n)] for j in range(n)]

	# base case
	# last row of arr is the base case
	for j in range(0, n):
		dp[n-1][j] = arr[n-1][j]

	# iterative tabulation loop
	for i in range(n-2, -1, -1):
		for j in range(i, -1, -1):
			down = arr[i][j] + dp[i+1][j]
			diagonal = arr[i][j] + dp[i+1][j+1]
			dp[i][j] = min(down, diagonal)
	return dp[0][0]

def f_spaceOptimized(n, arr):
	# base case
	# last row of arr is the base case
	prev = [-1] * n
	for i in range(n):
		prev[i] = arr[-1][i]

	# Iterative tabulation loop
	for i in range(n-2, -1, -1):
		curr = [-1] * n
		for j in range(i, -1, -1):
			down = arr[i][j] + prev[j]
			diagonal = arr[i][j] + prev[j+1]
			curr[j] = min(down, diagonal)
		prev = curr
	return prev[0]





arr = [[1], 
	   [2, 3], 
	   [3, 6, 7], 
	   [8, 9, 6, 10]]
n = len(arr)


print(f(0, 0, n, arr))
print(fm(n, arr))
print(f_tabular(n, arr))
print(f_spaceOptimized(n, arr))