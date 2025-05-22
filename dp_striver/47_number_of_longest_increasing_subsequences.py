"""
NUMBER OF LONGEST INCREASING SUBSEQUENCES
-----------------------------------------

Given an array, find the number of longest increasing subsequences.

arr = [1, 3, 5, 4, 7]

1 -> [1, 3, 4, 7], len=4
2 -> [1, 3, 5, 6], len=4
	* No. of longest increasing subsequences = 2


arr   = [1, 5, 4, 3, 2, 6, 7, 10, 8, 9]
dp    = [1]
count = [1]
"""


def numbersOfLIS(n, arr):
	dp = [1] * n
	count = [1] * n
	lis = 0

	for i in range(n):
		for prev in range(i):
			if arr[i] > arr[prev] and 1 + dp[prev] > dp[i]:
				dp[i] = 1 + dp[prev]
				count[i] = count[prev]
			elif arr[i] > arr[prev] and 1 + dp[prev] == dp[i]:
				count[i] += count[prev]
		lis = max(lis, dp[i])

	nos = 0
	for i in range(n):
		if dp[i] == lis:
			nos += count[i]
	return nos

arr = [1, 3, 5, 4, 7]
print(numbersOfLIS(len(arr), arr))

arr   = [1, 5, 4, 3, 2, 6, 7, 10, 8, 9]
print(numbersOfLIS(len(arr), arr))