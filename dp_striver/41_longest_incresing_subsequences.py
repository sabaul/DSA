"""
LONGEST INCREASING SUBSEQUENCES
-------------------------------
Given the array, find the longest increasing subsequences.

	- subsequences: contiguous or non-contiguous elements of array
					that follows the order of occurance in array.


arr = [10, 9, 2, 5, 3, 7, 101, 18]

possible solution:
	* [2, 5] = len = 2
	* [2, 3, 7] = len = 3
	* [2, 3, 7, 18] = len = 4


arr = [8, 8, 8]
	* [8] = len = 1
	* as duplicate elements won't be increasing
	* we need increasing subsequences

------------------
solution approach:
------------------
	* For subsequences
		* pick or not pick
		* take or not take

BRUTE FORCE
-----------
* try out various subsequences
	* print all subsequences
		1. power set
		2. recursion
	* check for increase
		* store the longest

Trying all ways:
	* Recursion

How to write recurence:
-----------------------
1. express everything in terms of index
	* f(idx, prev_idx)
		* prev tells me if I can use the element at index idx or not
		* we need to check if current element is greater than the prev or not
		* f(0, -1) -> start recursion with this
			* give me the LIS starting from index 0, with no previous element
		* f(3, 0)
			* give me LIS starting from 3rd index, whose previous index is 0

2. explore all possibilities
	* take/notTake

3. take max length of (notTake, take)

4. write base case



def f(idx, prev_idx):
	# base cases
	if idx == n:
		return 0

	# explore possibilities
	notPick = 0 + f(idx+1, prev_idx)
	take = 0
	if prev_idx == -1 or arr[idx] > arr[prev_idx]:
		pick = 1 + f(idx+1, idx)

	maxLen = max(notPick, pick)
	return maxLen

"""


def recursion(arr):
	n = len(arr)

	def f(idx, prev_idx):
		# base case
		if idx == n:
			return 0

		# explore possibilities
		# pick/notPick
		notPick = f(idx+1, prev_idx)
		pick = float('-inf')
		if prev_idx == -1 or arr[idx] > arr[prev_idx]:
			pick = 1 + f(idx+1, idx)
		maxLen = max(pick, notPick)
		return maxLen

	return f(0, -1)


def memoization(arr):
	"""
	idx changes from 0 to n-1
		* use a N size array

	prev_idx changes from -1 to n-1
		* -1, 0, 1, 2, ......  n-1
		* co-ordinate changed -->
		* 0, 1, 2, 3, .......  n
		* need a (n+1) size array

	dp = [n] * [n+1]
	"""
	n = len(arr)
	dp = [[-1 for i in range(n+1)] for j in range(n)]

	def f(idx, prev_idx):
		# base case
		if idx == n:
			return 0

		if dp[idx][prev_idx+1] != -1:
			return dp[idx][prev_idx+1]

		# explore possibilities
		# pick/notPick
		notPick = f(idx+1, prev_idx)
		pick = float('-inf')
		if prev_idx == -1 or arr[idx] > arr[prev_idx]:
			pick = 1 + f(idx+1, idx)

		maxLen = max(pick, notPick)
		dp[idx][prev_idx+1] = maxLen
		return dp[idx][prev_idx+1]

	return f(0, -1)


def tabulation(arr):
	n = len(arr)
	dp = [[0 for i in range(n+1)] for j in range(n+1)]

	for i in range(n-1, -1, -1):
		for prev_idx in range(n):
			notPick = dp[i+1][prev_idx]
			pick = float('-inf')
			if arr[i] > arr[prev_idx]:
				pick = 1 + dp[i+1][i]

			dp[i][prev_idx] = max(pick, notPick)
	return dp[0][0]


arr = [10, 9, 2, 5, 3, 7, 101, 18]

print(recursion(arr))
print(memoization(arr))
print(tabulation(arr))