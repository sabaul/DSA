"""
LONGEST BITONIC SUBSEQUENCES
----------------------------

bitonic -> strictly increasing order - strictly decreasing order
		     1, 2, 3, 4, 5,          6, 5, 4, 3, 2, 1

		-> It can also be strictly increasing --> Longest Increasing Subsequences
		-> It can also be strictly decreasing --> Longest Decreasing Subsequences

Solution approach:
	1. Run LIS in a forward pass
	2. Run LIS in a backward pass
	3. create a bitonic array -> bitonic = forward[i] + backward[i] - 1
		* -1 will be there since one element (the biggest one) will be counted twice
"""

def longestBitonicSubsequences(n, nums):
	dp1 = [1] * n
	dp2 = [1] * n

	for i in range(n):
		for j in range(i):
			if arr[i] > arr[j] and 1 + dp1[j] > dp1[i]:
				dp1[i] = 1 + dp1[j]

	for i in range(n-1, -1, -1):
		for j in range(n-1, i, -1):
			if arr[i] > arr[j] and 1 + dp2[j] > dp2[i]:
				dp2[i] = 1 + dp2[j]

	bitonic = [-1] * n
	res = 1
	for i in range(n):
		bitonic[i] += dp1[i] + dp2[i]
		res = max(res, bitonic[i])
	return res

arr = [1, 2, 1, 3, 4]
print(longestBitonicSubsequences(len(arr), arr))