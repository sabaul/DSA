"""
PARTITION A SET INTO SUBSETS SUCH THAT THE DIFFERENCE OF SUBSET SUMS IS MINIMUM
-------------------------------------------------------------------------------

Given an array containing N non-negative integers. Your task is to
partition this array into two subsets such that the absolute difference
between subset sums is minimum.


You just need to find the minimum absolute difference considering any
valid division of the array elements.


e.g.
arr = [1, 2, 3, 4]
s1 = [1, 2], s2 = [3, 4] ---> abs(7 - 3) = 4
s1 = [1, 3], s2 = [2, 4] ---> abs(6 - 4) = 2
s1 = [1, 4], s2 = [2, 3] ---> abs(5 - 5) = 0 --> minimal difference -> ans



SOLUTION APPROACH
-----------------

The problem 14 -> subset sum to target
Generate the tabulation 2d DP array

Check the last row, it represents the targets which are possibly True
on the last row. Check which 2 gives the minimum difference.
Return answer
"""

def subsetSumTabulation(n, target, arr):
	dp = [[False for i in range(target + 1)] for j in range(n)]

	for i in range(n):
		dp[i][0] = True
	if arr[0] <= target:
		dp[0][arr[0]] = True

	for i in range(1, n):
		for j in range(1, target+1):
			not_take = dp[i-1][j]
			take = False
			if arr[i] <= j:
				take = dp[i-1][j-arr[i]]
			dp[i][j] = take or not_take

	return dp[-1]


def subsetSumSpaceOptimized(n, target, arr):
	prev = [False for i in range(target+1)]
	cur = [False for i in range(target+1)]

	prev[0] = cur[0] = True
	prev[arr[0]] = True

	for i in range(1, n):
		for j in range(1, target+1):
			not_take = prev[j]
			take = False
			if arr[i] <= j:
				take = prev[j - arr[i]]
			cur[j] = take or not_take
		prev = cur
	return prev



def minSubsetSumDifference(arr, n):
	totalSum = sum(arr)

	# last_row = subsetSumTabulation(n, totalSum, arr)
	last_row = subsetSumSpaceOptimized(n, totalSum, arr)
	print(last_row)
	res = float('inf')
	for s1 in range(0, totalSum//2 + 1):
		if last_row[s1]:
			res = min(res, abs((totalSum - s1) - s1))
	return res



# arr = [1, 2, 3, 4]
arr = [1, 2, 4]
n = len(arr)
print(minSubsetSumDifference(arr, n))