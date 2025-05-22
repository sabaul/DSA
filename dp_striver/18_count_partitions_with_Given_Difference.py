"""
===============================
Partition with Given Difference
===============================
Given an array 'ARR', partition it into two subsets (possibly empty)
such that their union is the original array. Let the sum of
the elements of these two subsets be 'S1' and 'S2'.

given the difference 'D', count the no. of partitions in which
'S1' is greater than or equal to 'S2' and the difference between
'S1' and 'S2' is equal to 'D'. Since the answer may be too
large, return it modulo "10^9 + 7"

Given ----> [arr]
			/	\
		[s1]	[s2]

		s1 > s2
and s1 - s2 = D

e.g. [5, 2, 6, 4], D = 3
[6, 4] and [5, 2] --> (10 - 7 = 3) ===> (ans = 1)


Solution Approach
-----------------
how many subsets are there such that (s1 - s2) = d
where s1 > s2

s1 = totalSum - s2
so we have
(totalSum - s2) - s2 = d
totalSum - d = 2*s2
***s2 = (totalSum-d)/2***

we are looking for subsets such that s2 = (totalSum-d)/2

================================================
The question now becomes:
find the count of subsets whose sum is (totalSum - D)/2
================================================

++++++++ THIS IS DP17 WITH A MODIFIED TARGET ++++++++

edge cases:
1. (totalSum - D) >= 0
2. s2 = (sum of subset)
3. (totalSum - D) has to be even
"""


def f(idx, target, arr, dp):
	if idx == 0:
		if target == 0 and arr[0] == 0:
			return 2
		if target == 0 or arr[0] == target:
			return 1
		return 0

	if dp[idx][target] != -1:
		return dp[idx][target]

	notTake = f(idx-1, target, arr, dp)
	take = 0
	if arr[idx] <= target:
		take = f(idx-1, target-arr[idx], arr, dp)

	dp[idx][target] = take + notTake
	return dp[idx][target]


def findWays(arr, target):
	n = len(arr)
	dp = [[-1 for i in range(target+1)] for j in range(n)]
	return f(n-1, target, arr, dp)


def findWaysTabulation(arr, target):
	n = len(arr)
	dp = [[0 for i in range(target+1)] for j in range(n)]

	# base case
	if arr[0] == 0:
		dp[0][0] = 2
	else:
		dp[0][0] = 1

	if arr[0] != 0 and arr[0] <= target:
		dp[0][arr[0]] = 1

	for idx in range(1, n):
		for targ in range(target + 1):
			notTake = dp[idx-1][targ]
			take = 0
			if arr[idx] <= targ:
				take = dp[idx-1][targ - arr[idx]]
			dp[idx][targ] = take + notTake

	return dp[n-1][target]



def countPartitions(n, d, arr):
	totalSum = sum(arr)

	if (totalSum - d < 0) or (totalSum - d) % 2:
		return False

	# return findWays(arr, (totalSum-d)//2)
	return findWaysTabulation(arr, (totalSum-d)//2)




arr = [5, 2, 6, 4]
D = 3
n = len(arr)

print(countPartitions(n, D, arr))