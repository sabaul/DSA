"""
arr = [1, 3, 2]
Subsequences --> contiguous/non-contiguous part of the array
	e.g. -> [1, 2] is a subsequence --> follows order
			[2, 1] is not a subsequence --> doesn't follow order
			[3, 2] is subsequence/subarray --> follow orders

subsets --> doesn't necessaryly needs to be in order


------------------------------------
CODE STUDIO -> SUBSET SUM EQUAL TO K
------------------------------------

Given an array of 'N' positive integers and an integer K.
Your task is to check if there exists a subset in 'ARR' with a sum
equal to 'K'.

NOTE:
=====
Return True if there exists a subset with sum equal to 'K'.
Otherwise return False

e.g. arr = [1, 2, 3, 4], K = 4
	-> True, subsequences = [[1, 3], [4]]



Solution approach:
==================
-> Generate all subsequences and check if any of those gives sum
   equal to K.
-> it can be done by using -> ***POWER SET*** OR ***RECURSION***

============
-> RECURSION
============
1. Express everything is in terms of index
	-> f(idx, target)
2. Explore all possibilities on that index
	-> two choices:
	-> 1. arr[idx] is part of the subsequence
	-> 2. arr[idx] is not part of the subsequence
3. return True/False

============================
RECURSION = f(n-1, target)
----------------------------
-> in the entire array, till the index (n-1)
-> does there exist a target
e.g. arr = [1, 2, 3, 4], target = 4

-> f(3, 4) 
-> till index 3 (entire array) 
-> does there exist a target 4
============================
"""

def recursion(idx, nums, target):

	# 1. base conditions
	# target satisfied
	if target == 0:
		return True

	# out of bounds boundary condition
	if idx == 0:
		return target == nums[idx]

	# 2. explore all possibilities at the index idx
	# don't take the idx element
	not_take = recursion(idx-1, nums, target)
	# take the idx element
	take = False
	if nums[idx] <= target:
		take = recursion(idx-1, nums, target-nums[idx])

	return take or not_take


def memoized(nums, target):
	dp = [[-1 for i in range(target+1)] for j in range(len(nums)+1)]

	def f(i, target):
		if target == 0:
			return True
		if i == 0:
			return target == nums[i]

		if dp[i][target] != -1:
			return dp[i][target]

		not_take = f(i-1, target)
		take = False
		if nums[i] <= target:
			take = f(i-1, target-nums[i])
		return take or not_take

	return f(len(nums)-1, target)


def tabulation(nums, target):
	dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]

	# Base cases
	for i in range(len(nums)):
		dp[i][0] = True

	dp[0][nums[0]] = True

	# form the nested loops
	for i in range(1, len(nums)):
		for j in range(1, target+1):
			not_take = dp[i-1][j]
			take = False
			if nums[i] <= j:
				take = dp[i-1][j-nums[i]]

			dp[i][j] = take or not_take

	return dp[len(nums)-1][target]


def spaceOptimized(nums, target):
	"""
	Take care of the base cases here
	* the first element of all the rows will be True -> base case 1
	* the nums[0] element in prev will be True -> base case 2
	"""
	prev = [False for i in range(target+1)]
	cur = [False for i in range(target+1)]
	prev[0], cur[0] = True, True
	prev[nums[0]] = True

	for i in range(1, len(nums)):
		for j in range(1, target+1):
			not_take = prev[j]
			take = False
			if nums[i] <= j:
				take = prev[j-nums[i]]
			cur[j] = take or not_take
		prev = cur
	return prev[target]



arr = [1, 2, 3, 4]
target = 4

print(recursion(len(arr)-1, arr, target))
print(memoized(arr, target))
print(tabulation(arr, target))
print(spaceOptimized(arr, target))