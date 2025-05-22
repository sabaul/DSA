"""
Last problem on DP ON GRIDS ~ 3D DP
===================================

CODE STUDIO -> NINJA AND HIS FRIENDS
++++++++++++++++++++++++++++++++++++
Ninja has a grid of R*C. Each cell of the grid contains some chocolates. 
Ninja has 2 friends Alice and Bob, and he wants to collect as many 
chocolates as possible with help of his friends.

Initially Alice is in top-left position (0, 0) and Bob is in top-right 
position (0, C-1) in the grid. Each of them can move from their current 
cell to the cells just below them. When anyone passes from any cell, he 
will pick all chocolates in it, and then the no. of chocolates in that 
cell will become zero. If both stay in the same cell, only one of them 
will pick the chocolates in it.

If Alice or Bob is at (i, j) then they can move to (i+1, j), (i+1, j-1)
or (i+1, j+1). they will always stay inside the "GRID".

Your task is to find the maximum no. of chocolates Ninja can collect
with the help of his friends by following the above rules.


grid = [[2, 3, 1, 2],
		[3, 4, 2, 2],
		[5, 6, 3, 5]]

alice path = 2 -> 4 -> 6
bob path   = 2 -> 2 -> 5 (right most column)
total chocolates = 12 + 9 = 21 (we need to maximize this) ** OBJECTIVE **


----------------------------------------------
FIXED STARTING POINT (top left and top right) AND VARIABLE ENDING POINT
----------------------------------------------
n = # rows
m = # cols

(0, 0) and (0, m-1)
(All paths by Alice + All paths by Bob) --> Maximize it
		|					|
	Recursion			Recursion


APPROACH
--------
1. Express everything in terms of (i1, j1) for Alice and (i2, j2) for Bob.
2. Explore all the paths (down, down diagonal left and down diagonal right)
3. Max Sum


=========================================
Start recursion from fixed starting point
=========================================

f(0, 0, 0, m-1) --> first 2 args Alice position + last 2 args Bob's position

Base Case can be of 2 types:
1. destination based  --> i == n-1
2. Out of bounds base case -> (j1 < 0 or j1 >= m) or (j2 < 0 or j2 >= m)

----
NOTE ==> ALWAYS WRITE OUT OF BOUNDS BASE CASE FIRST
----

def f(i1, j1, i2, j2, n, m):
	if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
		return float('-inf')
	if i1 == n-1 and i2 == n-1:

--> i1 and i2 will be same
--> As both alice and bob will move together while moving in rows


DP ARRAY FOR MEMOIZATION
========================
in recursion which parameters are changing --> i, j1, j2
--------------------------------------------------------
range of  i -> 0 to n-1 -> size n
range of j1 -> 0 to m-1 -> size m
range of j2 -> 0 to m-1 -> size m

dp array dimention = n * m * m
--------------------------------------------------------

"""

def recursion(i, j1, j2, n, m, matrix):
	# Base cases
	# 1. Out of bound base cases
	if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
		return float('-inf')

	# 2. Destination base case
	if i == n-1:
		if j1 == j2:
			return matrix[i][j1]
		else:
			return matrix[i][j1] + matrix[i][j2]

	# 3. Explore all possible cases for both alice and bob
	# Move alice and bob both at once
	# 3 move possible by alice and bob
	# for each single move by alice, bob moves 3 times
	# so total of 9 combinations
	maxi = 0
	for dj1 in range(-1, 2, 1):
		for dj2 in range(-1, 2, 1):
			possibility = recursion(i+1, j1 + dj1, j2 + dj2, n, m, matrix)
			if j1 == j2:
				maxi = max(maxi, matrix[i][j1] + possibility)
			else:
				maxi = max(maxi, matrix[i][j1] + matrix[i][j2] + possibility)
	return maxi


def memoized(n, m, matrix):
	dp = [[[-1 for i in range(m)] for j in range(m)] for k in range(n)]

	def f(i, j1, j2):
		# 1. out of bounds base case
		if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
			return float('-inf')

		# 2. destination base case
		if i == n-1:
			if j1 == j2:
				return matrix[i][j1]
			else:
				return matrix[i][j1] + matrix[i][j2]

		# 3. Check if dp array at point i, j1, j2 != -1
		if dp[i][j1][j2] != -1:
			return dp[i][j1][j2]

		# 4. Explore all possible cases for both alice and bob
		maxi = 0
		for dj1 in range(-1, 2, 1):
			for dj2 in range(-1, 2, 1):
				possibility = f(i+1, j1+dj1, j2+dj2)
				if j1 == j2:
					maxi = max(maxi, matrix[i][j1] + possibility)
				else:
					maxi = max(maxi, matrix[i][j1] + matrix[i][j2] + possibility)
				dp[i][j1][j2] = maxi
		return dp[i][j1][j2]
	return f(0, 0, m-1)


# def tabulation(n, m, matrix):
# 	dp = [[[0 for i in range(m)] for j in range(m)] for k in range(n)]

# 	for j1 in range(m):
# 		for j2 in range(m):
# 			if j1 == j2:
# 				dp[n-1][j1][j2] = matrix[n-1][j1]
# 			else:
# 				dp[n-1][j1][j2] = matrix[n-1][j1] + matrix[n-1][j2]
# 	for i in range(n-2, -1, -1):
# 		for j1 in range(0, m):
# 			for j2 in range(0, m):

# 				maxi = float('-inf')
# 				for dj1 in range(-1, 2, 1):
# 					for dj2 in range(-1, 2, 1):
# 						if j1 == j2:
# 							value = matrix[i][j1]
# 						else:
# 							value = matrix[i][j1] + matrix[i][j2]

# 						if (j1+dj1 >= 0 and j1+dj1 < m and j2+dj2 >= 0 and j2+dj2 < m):
# 							value += dp[i+1][j1+dj1][j2+dj2]
# 						else:
# 							value += float('-inf')

# 						maxi = max(maxi, value)
# 				dp[i][j1][j2] = maxi
# 		return dp[0][0][m-1]



grid = [[2, 3, 1, 2],
		[3, 4, 2, 2],
		[5, 6, 3, 5]]

n = len(grid)
m = len(grid[0])
print(recursion(0, 0, m-1, n, m, grid))
print(memoized(n, m, grid))
# print(tabulation(n, m, grid))