"""
PARTITION DP INTRODUCTION
-------------------------
MATRIX CHAIN MULTIPLICATION * [[Partition DP]]
---------------------------   ================

* Solve a problem in a pattern ( a particular way )
	* pattern = mathematical calculation
		* e.g. (1 + 2 + 3 ) * 5 and (1 + 2) + (3 * 5) are different
		* solve problem in a particular way, you get a different answer
		* the answer depends on the way you solve a particular problem

* Rules for Partition DP
	1. Given an array
		* arr = []
		* Solve for one portion first and then second portion
			* e.g. arr[0, i] first and then arr[i, n-1]

		* in other words:
		* Given an array arr (start point = i and end point = j)
			* and a partition is present at k
			* solve for arr[i, k] and arr[k, j]
				* f(i, k) and then f(k+1, j)
					* return min/max/optimal response


#################################### PREREQUISITES START ####################################

Given 3 matrices: A, B, C
	* Multiply A, B and C and tell me the minimum cost in multiplication
	* cost = no. of multiplication operations
	Dimension A -> 10 * 30
	Dimension B -> 30 * 5
	Dimension C -> 5 * 60

Star (*) operation = multiplication operator

A * B -> possible as (number of columns in first matrix (A) = number of rows in second matrix (B))
	* No. of multiplication operations required = 10 * 30 * 5 = 1500

#################################### PREREQUISITES ENDS ####################################

"""