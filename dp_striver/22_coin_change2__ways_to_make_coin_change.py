"""
=============================================
Ways to make coin change - DP ON SUBSEQUENCES
=============================================

Given an array and a target. Form the target. Any element in array can be
used any no. of times.

arr = [1, 2, 3], target = 4

ways to make target = 4 using the array arr:
	[1, 1, 1, 1] = 4
	[1, 1, 2]    = 4
	[2, 2]       = 4
	[1, 3]       = 4

Answer = 4 ways



To find total no. of ways --> TRY OUT ALL WAYS (RECURSION)


How to write recursion function:

1. Express problem in terms of indices
	-> f(idx, target)
	-> f(2, 4)
		-> Till index 2, in how many ways can we form the target 4
2. Do all possible stuff on that index
	-> take and not take
3. Count no. of ways
	-> sum of possibilities
"""


def spaceOptimization(n, target, arr):
	prev = [0 for i in range(target+1)]
	cur = [0 for i in range(target+1)]

	for t in range(target+1):
		if t%arr[0] == 0:
			prev[t] = 1
		else:
			prev[t] = 0

	for idx in range(1, n):
		for t in range(target+1):
			notTake = prev[t]
			take = 0
			if arr[idx] <= t:
				take = cur[t-arr[idx]]

			cur[t] = take + notTake
		prev = cur
	return prev[target]



def tabulation(n, target, arr):
	dp = [[0 for i in range(target+1)] for j in range(n)]

	for t in range(target+1):
		if t%arr[0] == 0:
			dp[0][t] = 1
		else:
			dp[0][t] = 0

	for idx in range(1, n):
		for t in range(target+1):
			notTake = dp[idx-1][t]
			take = 0
			if arr[idx] <= t:
				take = dp[idx][t-arr[idx]]

			dp[idx][t] = take + notTake
	return dp[n-1][target]


def memoization(n, target, arr):
	dp = [[-1 for i in range(target+1)] for j in range(n)]

	def f(idx, t):
		if idx == 0:
			if t % arr[0] == 0:
				return 1
			return 0

		# check dp
		if dp[idx][t] != -1:
			return dp[idx][t]

		# explore possibility
		notTake = f(idx-1, t)
		take = 0
		if arr[idx] <= t:
			take = f(idx, t-arr[idx])
		dp[idx][t] = take + notTake
		return dp[idx][t]
	return f(n-1, target)


def recursion(n, target, arr):

	def f(idx, t):
		# base cases
		if idx == 0:
			if t % arr[0] == 0:
				return 1
			else:
				return 0


		# explore possibilities
		notTake = f(idx-1, t)
		take = 0
		if arr[idx] <= t:
			take = f(idx, t-arr[idx])

		return take + notTake
	return f(n-1, target)



arr = [1, 2, 3]
target = 4
n = len(arr)

print(recursion(n, target, arr))
print(memoization(n, target, arr))
print(tabulation(n, target, arr))
print(spaceOptimization(n, target, arr))