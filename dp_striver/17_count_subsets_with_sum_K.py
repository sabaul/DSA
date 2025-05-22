"""
Number of Subsets
-----------------

Given an array (0-based indexing) of positive integers and you have
to tell how many different ways of selecting the elements from the
array are there such that the sum of chosen elements is equal to the
target number "tar".

-------------------------------------
arr = [1, 2, 2, 3], tar = 3
count no. of subsets that sum = tar

subsets = [[1, 2], [1, 2], [3]]
subset count = 3

recurrence:
1. express problem in terms of index
	-> f(idx, target)
	-> f(n-1, target)
		-> it means how many number of subsets which sum up 
		-> to target till the index (n-1)
2. do all possible stuffs on that index
	-> 
3. sum all of the possibility up
"""

def recursion(i, target, arr):
	if target == 0:
		return 1
	if i == 0:
		if arr[i] == target:
			return 1
		else:
			return 0

	# explore all possibilities
	not_pick = recursion(i-1, target, arr)
	pick = 0
	if arr[i] <= target:
		pick = recursion(i-1, target-arr[i], arr)
	return pick + not_pick


def memoization(n, target, arr):
	dp = [[-1 for i in range(target + 1)] for j in range(n)]

	def f(i, target):
		if target == 0:
			return 1
		if i == 0:
			if arr[i] == target:
				return 1
			return 0

		if dp[i][target] != -1:
			return dp[i][target]

		# explore all possibilities
		not_pick = f(i-1, target)
		pick = 0
		if arr[i] <= target:
			pick = f(i-1, target - arr[i])
		dp[i][target] = pick + not_pick
		return dp[i][target]
	return f(n-1, target)


def tabulation(n, target, arr):
	dp = [[0 for i in range(target+1)] for j in range(n)]

	# target = 0 base case
	for i in range(n):
		dp[i][0] = 1
	# i == 0 base case
	if arr[0] <= target:
		dp[0][arr[0]] = 1

	for i in range(1, n):
		for targ in range(target+1):
			not_pick = dp[i-1][targ]
			pick = 0
			if arr[i] <= targ:
				pick = dp[i - 1][targ - arr[i]]
			dp[i][targ] = pick + not_pick
	return dp[n-1][target]


def spaceOptimized(n, target, arr):
	prev = [0 for i in range(target+1)]
	cur = [0 for i in range(target+1)]

	prev[0] = cur[0] = 1
	if arr[0] <= target:
		prev[arr[0]] = 1

	for i in range(1, n):
		for targ in range(1, target+1):
			not_pick = prev[targ]
			pick = 0
			if arr[i] <= targ:
				pick = prev[targ - arr[i]]
			cur[targ] = pick + not_pick
		prev = cur
	return prev[target]


arr = [1, 2, 2, 3]
tar = 3
n = len(arr)
print(recursion(n-1, tar, arr))
print(memoization(n, tar, arr))
print(tabulation(n, tar, arr))
print(spaceOptimized(n, tar, arr))