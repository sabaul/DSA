"""
--------------------------
PARTITION EQUAL SUBSET SUM
--------------------------

Given an array 'ARR' of 'N' positive integers. Your task is to find if we
can partition the given array into two subsets such that the sum of 
elements in both subsets is equal.

e.g. Let's say the given array is [2, 3, 3, 3, 4, 5], then the array can be
partitioned as [2, 3, 5] and [3, 3, 4] with equal sum 10.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			[2, 3, 3, 3, 4, 5]
			/				 \
	[2, 3, 5]				  [3, 3, 4]
	 subset 1 					subset 2


Divide them into 2 subsets such that s1 = s2

		S
	  /   \
	 s1   s2

s1 = s2 = s/2 
where s = total sum of elements of input array

if s = odd -> not possible

so if we find s1 (i.e. s1 = s/2)
the remaining elements will form s2 (as s1 == s2)

so the Question converts to ==> DP QUESTION 14

Given an array input, check if we can have a subset sum = s/2 (s = total sum)
"""

def subsetSumSpaceOptimized(n, target, arr):
	prev = [False for i in range(target + 1)]
	cur = [False for i in range(target + 1)]

	prev[0] = cur[0] = True
	prev[arr[0]] = True

	for i in range(1, n):
		for j in range(1, target+1):
			not_take = prev[j]
			take = False
			if arr[i] <= j:
				take = prev[j-arr[i]]
			cur[j] = take or not_take
		prev = cur
	return prev[target]


def subsetSumTabulation(n, target, arr):
	dp = [[False for i in range(target + 1)] for j in range(n)]

	# base cases
	for i in range(target):
		dp[0][i] = True

	if arr[0] <= target:
		dp[0][arr[0]] == True

	# explore all possibilities in the iterative loop
	for i in range(1, n):
		for j in range(target+1):
			not_take = dp[i-1][j]
			take = False
			if arr[i] <= j:
				take = dp[i-1][j-arr[i]]
			dp[i][j] = take or not_take
	return dp[n-1][target]


def subsetSumRecursionMemoized(n, target, arr):
	dp = [[-1 for i in range(target+1)] for j in range(n)]

	def f(i, target):
		if target == 0: return True
		if i == 0: return arr[i] == target

		if dp[i][target] != -1:
			return dp[i][target]

		# explore all cases
		not_take = f(i-1, target)
		take = False
		if arr[i] <= target:
			take = f(i-1, target - arr[i])
		dp[i][target] = take or not_take
		return dp[i][target]
	return f(n-1, target)


def subsetSumRecursion(n, target, arr):
	def f(i, target):
		# base cases
		if target == 0: return True
		if i == 0: return arr[i] == target

		# explore all cases
		not_take = f(i-1, target)
		take = False
		if arr[i] <= target:
			take = f(i-1, target-arr[i])
		return take or not_take
	return f(n-1, target)


def canPartition(arr, n):
	totalSum = sum(arr)
	if totalSum % 2:
		return False

	target = totalSum // 2
	# return subsetSumRecursion(n, target, arr)
	# return subsetSumRecursionMemoized(n, target, arr)
	# return subsetSumTabulation(n, target, arr)
	return subsetSumSpaceOptimized(n, target, arr)





arr = [2, 3, 3, 3, 4, 5]
n = len(arr)
print(canPartition(arr, n))

arr = [2, 3, 3, 3, 4, 5, 1]
n = len(arr)
print(canPartition(arr, n))

arr = [1, 5, 11, 5]
n = len(arr)
print(canPartition(arr, n))