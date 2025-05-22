"""
--------------------------------------------------------
Problem 1 on Partition DP -> Matrix Chain Multiplication
--------------------------------------------------------

#################################### PREREQUISITES START ####################################

Given 3 matrices: A, B, C
	* Multiply A, B and C and tell me the minimum cost in multiplication to make a single matrix
	* cost = no. of multiplication operations
	Dimension A -> 10 * 30
	Dimension B -> 30 * 5
	Dimension C -> 5 * 60

Star (*) operation = multiplication operator

A * B -> possible as (number of columns in first matrix (A) = number of rows in second matrix (B))
	* No. of multiplication operations required = 10 * 30 * 5 = 1500

#################################### PREREQUISITES ENDS ####################################


Q. Given 3 matrices: A, B and C.
   Return the minimum cost (cost = no. of operations) to multiply the 3 matrices
   to make a single matrix
	* Dimension A -> 10 * 30
	* Dimension B -> 30 * 5
	* Dimension C -> 5 * 60

-----------------
Solution Approach
-----------------
	1. (A * B) * C -> First multipl A and B, and then multiply result with C

		* Operation A * B
		* no. of multiplications = A * B = 10 * 30 * 5
		* resultant of A * B = (10 * 30) * (30 * 5) dimensions
							 = 10 * 5 dimension resultant matrix

		* Operation resultant * B
		* no. of multiplications = resultant * C = 10 * 5 * 60
		* resultant * C = (10 * 5)  * (5 * 60) dimensions
						= 10 * 60 dimension resultant matrix

		* Total no. of multiplications = (10 * 30 * 5) + (10 * 5 * 60)
									   = 1500 + 3000
									   = 4500 total multiplication operations

	2. A * (B * C) -> First multiply B and C, then multiply result with A

		* Operation B * C
		* no. of multiplications = B * C = 30 * 5 * 60 = 9000
		* resultant of B * C = (30 * 5) * (5 * 60)
							 = 30 * 60 dimension matrix

		* Operation A * resultant
		* no. of multiplication = A * resultant matrix
								= 10 * 30 * 60 = 18000
		* A * resultant dimention = (10 * 30) * (30 * 60)
								  = 10 * 60 dimension final matrix

		* Total no. of multiplications = 9000 + 18000
									   = 27000 operations

=========================================================================

Q. Given matrices A, B, C and D. Multiply them into a single matrix and
   and return the minimum cost

A. How can we multiply
	1. A(B(CD))
	2. (AB)(CD)
	3. (A(BC))D


Given an array of size n, containing dimensions of (n-1) matrices:
	* arr = [10, 20, 30, 40, 50]
		* n = 5
		* arr contains dimensions of (n-1) matrices
	* Dimension of A = 10 * 20
		* A[0] * A[1]
	* Dimension of B = 20 * 30
		* A[1] * A[2]
	* Dimension of C = 30 * 40
		* A[2] * A[3]
	* Dimension of D = 40 * 50
		* A[3] * A[4]

	* Dimension of i'th matrix -> A[i-1] * A[i]


----------------------------------------------
How Do You Solve This Problem --> PARTITION DP
----------------------------------------------

Rules:
1. Start with entire block/array 
	* Always represent them with (i, j)
	* f(i, j)

					ABCD
					i  j
			/		  |			\
	(AB)(CD)       (A)(BCD)      (ABC)(D)
	 ij  ij        ij  i j        i j  ij

	 i -> start point
	 j -> end point


2. Try all partitions 
	* Run a loop to try all partitions

3. Return the best possible 2 partitions

================================================




arr = [10, 20, 30, 40, 50]
		0   1   2   3   4
		    A   B   C   D
		    i           j
		    1           (n-1) = 4


Rules:
======

Step 1: start with f(i, j)
	* f(1, n-1)
	* f(1, 4)
		* returns the min. multiplications to multiply matrix 1 to matrix 4
	
	* Base case
		* i and j will shrink at each partition
		* the minimum that i and j can shrink is when it's at same matrix
			i.e. no. of operations in single matrix = 0 
		* Base case is i == j
		* if i == j: return 0

Step 2: Try all partitions
                     0   1   2   3   4
	* Given array: [10, 20, 30, 40, 50]
						 A   B   C   D
						 i           j

	APPROACH 1
	----------
	* Run a loop k = i to j-1
				 k -> ranges from 1 to 3

	* partitions: f(i, k),  f(k+1, j)

	* k = 1
		* 1st partition: f(1, 1), f(2, 4)
	* k = 2
		* 2nd partition: f(1, 2), f(3, 4)
	* k = 3
		* 3rd partition: f(1, 3), f(4, 4)


	APPROACH 2
	----------
	* Run a loop k = i+1 to j
				 k -> ranges from 2 to 4

	* partitions: f(i, k-1),  f(k, j)

	* k = 2
		* 1st partition: f(1, 1), f(2, 4)
	* k = 3
		* 2nd partition: f(1, 2), f(3, 4)
	* k = 4
		* 3rd partition: f(1, 3), f(4, 4)


	* Both approach 1 and approach 2 yields the same result

 
	# Calculate no. of steps for k = 1
	* dimensions: A (10, 20), B (20, 30), C (30, 40), D (40, 50)
	* k = 1
		* 1st partition: f(1, 1), f(2, 4)
							|        |
						A (10,20)   BCD (20,50)
									  * no matter how we multiply BCD, resultant matrix will be of dimension (20, 50)
		
		              k
		              i           j
		* arr = [10, 20, 30, 40, 50]
		* no. of steps = 10 * 20 * 50
		* 10 is on the left of i --> (i-1) -> arr[i-1]
		* 20 is at k -> arr[k]
		* 50 is at j -> arr[j]



# CODE

def f(i, j):
	if i == j:
		return 0

	mini = float('inf')
	for k in range(i, j-1):
		# count no. of steps if we partition at k

		steps = ((arr[i-1] * arr[k] * arr[j]) # check line 182 to 196
					 + f(i, k) + f(k+1, j))    # give me result from here

		mini = min(mini, steps)

	# return min(all steps)
	return mini
"""



def tabulation(n, arr):
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n-1, 0, -1):
        for j in range(i+1, n):
            mini = float('inf')
            for k in range(i, j):
                steps = (arr[i-1] * arr[k] * arr[j]) + dp[i][k] + dp[k+1][j]
                if steps < mini:
                    mini = steps
            dp[i][j] = mini
    return dp[1][n-1]

def memoization(i, j, arr, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    mini = float('inf')
    for k in range(i, j):
        steps = (arr[i-1] * arr[k] * arr[j]) + memoization(i, k, arr, dp) + memoization(k+1, j, arr, dp)
        if steps < mini:
            mini = steps
    dp[i][j] = mini
    return dp[i][j]

def recursion(i, j, arr):
    if i == j:
        return 0
    mini = float('inf')
    for k in range(i, j):
        steps = (arr[i-1] * arr[k] * arr[j]) + recursion(i, k, arr) + recursion(k+1, j, arr)
        if steps < mini:
            mini = steps
    return mini

def mcm(arr):
    n = len(arr)
    res = recursion(1, n-1, arr)
    print(f"Recursion: {res}")

    dp = [[-1 for i in range(n)] for j in range(n)]
    res = memoization(1, n-1, arr, dp)
    print(f"Memoization: {res}")

    res = tabulation(n, arr)
    print(f"Tabulation: {res}")
    return res


arr = [10, 15, 20, 25]
output = 8000
res = mcm(arr)
print(f"Expected Answer: {8000}")

















# FROM CODING NINJAS CODE STUDIO

import sys
from sys import stdin

def tabulation(n, arr):
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n-1, 0, -1):
        for j in range(i+1, n):
            mini = float('inf')
            for k in range(i, j):
                steps = (arr[i-1] * arr[k] * arr[j]) + dp[i][k] + dp[k+1][j]
                if steps < mini:
                    mini = steps
            dp[i][j] = mini
    return dp[1][n-1]

def memoization(i, j, arr, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    mini = float('inf')
    for k in range(i, j):
        steps = (arr[i-1] * arr[k] * arr[j]) + memoization(i, k, arr, dp) + memoization(k+1, j, arr, dp)
        if steps < mini:
            mini = steps
    dp[i][j] = mini
    return dp[i][j]

def recursion(i, j, arr):
    if i == j:
        return 0
    mini = float('inf')
    for k in range(i, j):
        steps = (arr[i-1] * arr[k] * arr[j]) + recursion(i, k, arr) + recursion(k+1, j, arr)
        if steps < mini:
            mini = steps
    return mini

def mcm(p,n):
    n = len(p)
    # res = recursion(1, n-1, p)
    # dp = [[-1 for i in range(n)] for j in range(n)]
    # res = memoization(1, n-1, p, dp)
    res = tabulation(n, p)
    return res




# CODING NINJAS CODE STUDIO SUBMISSION
import sys
from sys import stdin

def tabulation(n, arr):
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n-1, 0, -1):
        for j in range(i+1, n):

            minsteps = float('inf')
            for k in range(i, j):
                steps = ((arr[i-1] * arr[k] * arr[j])
                         + dp[i][k]
                         + dp[k+1][j])
                if steps < minsteps:
                    minsteps = steps
            dp[i][j] = minsteps
    return dp[1][n-1]


def memoization(i, j, arr, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    minsteps = float('inf')
    for k in range(i, j):
        steps = ((arr[i-1] * arr[k] * arr[j])
                 + memoization(i, k, arr, dp)
                 + memoization(k+1, j, arr, dp))
        if steps < minsteps:
            minsteps = steps
    dp[i][j] = minsteps
    return dp[i][j]


def recursion(i, j, arr):
    if i == j:
        return 0
    minsteps = float('inf')
    for k in range(i, j):
        steps = ((arr[i-1] * arr[k] * arr[j]) 
                 + recursion(i, k, arr) 
                 + recursion(k+1, j, arr))
        if steps < minsteps:
            minsteps = steps
    return minsteps


def mcm(p,n):
    n = len(p)
    # res = recursion(1, n-1, p)

    # dp = [[-1 for i in range(n)] for j in range(n)]
    # res = memoization(1, n-1, p, dp)

    res = tabulation(n, p)
    return res













n=int(stdin.readline().strip())
p=[int(i) for i in stdin.readline().strip().split()]
print(mcm(p,n))