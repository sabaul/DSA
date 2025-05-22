"""
MINIMUM COST TO CUT THE STICK
-----------------------------

Given an array (arr) and length of stick (n), cut the stick at the portion from the given array such that the cost is minimized.

COST: the length of the stick that we are cutting.

arr = [1, 3, 4, 5] <--------> n = 7


	| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
	0   1   2   3   4   5   6   7	-->	length of array

	# CUT AT 1 (arr[0])								
	# cost = 7 (LENGTH OF PREVIOUS ARRAY)
	# total cost = 7

	| 1 | 	   | 2 | 3 | 4 | 5 | 6 | 7 |
	0   1      1   2   3   4   5   6   7


	# CUT AT 3 (arr[1])								
	# cost = 6 (LENGTH OF second array)
	# total cost = 7 + 6 = 13

	| 1 | 	   | 2 | 3 |     | 4 | 5 | 6 | 7 |
	0   1      1   2   3     3   4   5   6   7


	# CUT AT 4 (arr[2])
	# cost = 4 (LENGTH OF array at the end (idx 3 to 7))
	# total cost = 7 + 6 + 4 = 17

	| 1 | 	   | 2 | 3 |     | 4 |    | 5 | 6 | 7 |
	0   1      1   2   3     3   4    4   5   6   7

	# CUT AT 5 (arr[3])
	# cost = 3 (LENGTH OF array at the end (idx 4 to 7))
	# total cost = 7 + 6 + 4 + 3 = 20

	| 1 | 	   | 2 | 3 |     | 4 |    | 5 |    | 6 | 7 |
	0   1      1   2   3     3   4    4   5    5   6   7

 
	TOTAL COST = 20


=====================================================================

If we cut it in the sequence -> 3, 5, 1, 4

cut at 3 -> we will have -> [0 1 2 3] and [3 4 5 6 7]
			the length --->     3              4
			cost = 7

cut at 5 -> we will have -> [0 1 2 3] and [3 4 5] and [5 6 7]
			the length --->     3            2           2
			cost = 7 + 4


cut at 1 -> we will have -> [0 1] and [1 2 3] and [3 4 5] and [5 6 7]
			the length --->   1          2           2           2
			cost = 7 + 4 + 3


cut at 4 -> we will have -> [0 1] and [1 2 3] and [3 4] and [4 5] and [5 6 7]
			the length --->   1          2          1         1          2
			cost = 7 + 4 + 3 + 2
				 = 16

LOWEST COST = 16


====================================================================
###################### solution approach ###########################
====================================================================

input array:
			[1 3 4 5]
				 x
			   /   \
			[1 3]  [5]

-> if we sort the input array and solve them independently, will it work?
-> YES, because it is sorted.

-> Say we have a cut at 4

	[0 1 2 3 4] and [4 5 6 7]

	-> or even if we have a cut at 5 or 1
	-> it won't matter
	-> as they are not independent
	-> and they are not connected


-> let's say, we have input array as
	[1 3 4 5 2]

	-> now we can't solve them independently

-> so it has to be sorted
-> so that whenever we solve a subproblem
-> they won't be dependent on each other


==================================================================
solution methodology
==================================================================

* append zero (0) at the begenning and length of string(7) at the end of input array arr

		0  1  2  3  4  5
		0 [1  3  4  5] 7
		   i     j

		         ^
		         |
		        idx

		-> say we cut at 4
		-> cost = length of string in which 4 is present
				= cuts[j + 1] - cuts[i-1]
				= 7 - 0
				= 7
				  + f(i, idx - 1) --> we need to solve for left partition
				  + f(idx + 1, j) --> we need to solve for right partition


-> PARTITION DP
-> INITIALLY THE ENTIRE ARRAY IS CONSIDERED
-> f(1, 4)



def f(i, j):
	# if it crosses over, we have nothing to solve
	if i > j:
		return 0

	mini = float('inf')
	for idx in range(i, j):
		cost = ((cuts[j+1] - cuts[i-1])
				+ f(i, idx - 1)			# left subproblem
				+ f(idx + 1, j))		# right subproblem

		mini = min(mini, cost)
	return mini

"""


def tabulation(n, c, cuts):
	dp = [[0 for i in range(c+2)] for j in range(c+2)]

	for i in range(c, 0, -1):
		for j in range(1, c+1):
			if i > j:
				continue

			mini = float('inf')
			for idx in range(i, j+1):
				cost = (cuts[j+1] - cuts[i-1] 
						+ dp[i][idx - 1] 
						+ dp[idx + 1][j])
				mini = min(mini, cost)

			dp[i][j] = mini
	return dp[1][c]




def memoization(i, j, cuts, dp):
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    mini = float('inf')
    for idx in range(i, j+1):
        cost = cuts[j+1] - cuts[i-1] + memoization(i, idx-1, cuts, dp) + memoization(idx + 1, j, cuts, dp)
        mini = min(mini, cost)
    dp[i][j] = mini
    return dp[i][j]


def recursion(i, j, cuts):
    if i > j:
        return 0
    
    mini = float('inf')
    for idx in range(i, j+1):
        cost = cuts[j+1] - cuts[i-1] + recursion(i, idx-1, cuts) + recursion(idx+1, j, cuts)
        mini = min(mini, cost)
    return mini


def cost(n: int, c: int, cuts: List[int]) -> int:
    cuts = [0] + cuts + [n]
    cuts.sort()

    # res = recursion(1, c, cuts)

    # dp = [[-1 for i in range(n)] for j in range(n)]
    # res = memoization(1, c, cuts, dp)

    res = tabulation(n, c, cuts)
    return res


def cost(n: int, c: int, cuts: List[int]) -> int:
    cuts = [0] + cuts + [n]
    cuts.sort()
    # res = recursion(1, c, cuts)

    # dp = [[-1 for i in range(n)] for j in range(n)]
    # res = memoization(1, c, cuts, dp)

    res = tabulation(n, c, cuts)
    return res




###############################
# LEETCODE SOLUTION
###############################

class Solution:
    
    def tabulation(self, n, c, cuts):
        dp = [[0 for i in range(c + 2)] for j in range(c + 2)]
        
        for i in range(c, 0, -1):
            for j in range(1, c + 1):
                if i > j:
                    continue
                
                mincost = float('inf')
                for idx in range(i, j + 1):
                    cost = (cuts[j + 1] - cuts[i - 1]
                            + dp[i][idx - 1]
                            + dp[idx + 1][j])
                    mincost = min(mincost, cost)
                dp[i][j] = mincost
        return dp[1][c]
    
    def memoization(self, i, j, cuts, dp):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        mincost = float('inf')
        for idx in range(i, j + 1):
            cost = (cuts[j + 1] - cuts[i - 1]
                    + self.memoization(i, idx - 1, cuts, dp)
                    + self.memoization(idx + 1, j, cuts, dp))
            mincost = min(mincost, cost)
        dp[i][j] = mincost
        return dp[i][j]
    
    def recursion(self, i, j, cuts):
        if i > j:
            return 0
        
        mincost = float('inf')
        for idx in range(i, j + 1):
            cost = (cuts[j + 1] - cuts[i - 1]
                    + self.recursion(i, idx - 1, cuts)
                    + self.recursion(idx + 1, j, cuts))
            mincost = min(mincost, cost)
        return mincost
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        cuts = [0] + cuts + [n]
        cuts.sort()
        
        # res = self.recursion(1, c, cuts)
        
        # i --> 1 to c (c = num cuts)
        # j --> c to 1
        # dp = [[-1 for i in range(c + 2)] for j in range(c + 2)]
        # res = self.memoization(1, c, cuts, dp)
        
        res = self.tabulation(1, c, cuts)
        
        return res