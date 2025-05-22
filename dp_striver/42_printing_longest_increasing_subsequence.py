"""
PRINTING LONGEST INCREASING SUBSEQUENCES
----------------------------------------


"""


def recursion(arr):
	n = len(arr)

	def f(i, prev_idx):
		if i == n:
			return 0

		# explore possibilities
		notTake = f(i+1, prev_idx)
		take = float('-inf')
		if prev_idx == -1 or arr[i] > arr[prev_idx]:
			take = 1 + f(i+1, i)
		maxLen = max(take, notTake)
		return maxLen

	return f(0, -1)

def memoization(arr):
	"""
	i -> 0 to n-1
	  -> 0, 1, 2, .... n-1
	prev_idx -> -1 to n-1
			 -> -1, 0, 1, 2, 3, .... n-1

	dp = [n][n+1]
	"""
	n = len(arr)
	dp = [[-1 for i in range(n+1)] for j in range(n)]

	def f(i, prev_idx):
		if i == n:
			return 0

		if dp[i][prev_idx+1] != -1:
			return dp[i][prev_idx+1]

		notTake = f(i+1, prev_idx)
		take = float('-inf')
		if prev_idx == -1 or arr[i] > arr[prev_idx]:
			take = 1 + f(i+1, i)
		dp[i][prev_idx+1] = max(take, notTake)
		return dp[i][prev_idx+1]
	return f(0, -1)


def tabulation(arr):
	n = len(arr)
	dp = [[0 for i in range(n+1)] for j in range(n+1)]

	for i in range(n-1, -1, -1):
		for prev_idx in range(i-1, -2, -1):
			notTake = dp[i+1][prev_idx+1]
			take = float('-inf')
			if prev_idx == -1 or arr[i] > arr[prev_idx]:
				take = 1 + dp[i+1][i+1]
			dp[i][prev_idx+1] = max(take, notTake)
	return dp[0][-1+1]


def spaceOptimization(arr):
	n = len(arr)

	ahead = [0 for i in range(n+1)]
	cur = [0 for i in range(n+1)]

	for i in range(n-1, -1, -1):
		for prev_idx in range(i-1, -2, -1):
			notTake = ahead[prev_idx+1]
			take = float('-inf')
			if prev_idx == -1 or arr[i] > arr[prev_idx]:
				take = 1 + ahead[i+1]
			cur[prev_idx+1] = max(take, notTake)
		ahead = cur[:]
	return ahead[-1+1]


def anotherApproach(arr):
	n = len(arr)
	dp = [1 for i in range(n)]
	maxi = 1

	for i in range(n):
		for prev in range(i):
			if arr[prev] < arr[i]:
				dp[i] = max(dp[i], 1 + dp[prev])
		maxi = max(maxi, dp[i])
	return maxi



def printLIS(arr):
	n = len(arr)
	dp = [1 for _ in range(n)]
	hashh = [i for i in range(n)]
	maxi = 1
	lastIndex = 0

	for i in range(n):
		for prev in range(i):
			if arr[prev] < arr[i] and 1 + dp[prev] > dp[i]:
				dp[i] = 1 + dp[prev]
				hashh[i] = prev

	# 	if dp[i] > maxi:
	# 		maxi = dp[i]
	# 		lastIndex = i

	# while hashh[lastIndex] != lastIndex:
	# 	lastIndex = hashh[lastIndex]
	# 	lis[ind] = arr[lastIndex]
	idx = dp.index(max(dp))
	res = []
	while idx != 0:
		res.append(arr[idx])
		idx = hashh[idx]
	print(res)




arr = [10, 9, 2, 5, 3, 7, 101, 18]


print(printLIS(arr))

# print(recursion(arr))
# print(memoization(arr))
# print(tabulation(arr))
# print(spaceOptimization(arr))
# print(anotherApproach(arr))

# print('='*10)

# arr = [5, 4, 11, 1, 16, 18]
# print(recursion(arr))
# print(memoization(arr))
# print(tabulation(arr))
# print(spaceOptimization(arr))
# print(anotherApproach(arr))