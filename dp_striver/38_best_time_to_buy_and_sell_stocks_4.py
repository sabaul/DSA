"""
BEST TIME TO BUY AND SELL STOCKS 4
----------------------------------
	* Allowed to take at most K transactions
	* Stock 3 allowed us at most 2 transactions


prices = [3, 2, 6, 5, 0, 3]
k = 2

"""

def recursion(prices, k):
	n = len(prices)

	def f(idx, tranNo):
		# base cases
		if idx == n or tranNo == 2*k:
			return 0

		# explore possibilities
		if tranNo % 2 == 0:			# buy
			return max(-prices[idx] + f(idx+1, tranNo+1),
						0 + f(idx+1, tranNo))
		else:						# sell
			return max(prices[idx] + f(idx+1, tranNo+1),
						0 + f(idx+1, tranNo))

	return f(0, 0)


def memoization(prices, k):
	n = len(prices)
	dp = [[-1 for i in range(2*k)] for j in range(n)]

	def f(idx, tranNo):
		# base case
		if idx == n or tranNo == 2*k:
			return 0

		if dp[idx][tranNo] != -1:
			return dp[idx][tranNo]

		# explore possibilities
		if tranNo % 2 == 0:
			dp[idx][tranNo] = max(-prices[idx] + f(idx+1, tranNo+1),
								  0 + f(idx+1, tranNo))
		else:
			dp[idx][tranNo] = max(prices[idx] + f(idx+1, tranNo+1),
								  0 + f(idx+1, tranNo))
		return dp[idx][tranNo]

	return f(0, 0)


def tabulation(prices, k):
	n = len(prices)
	dp = [[0 for i in range(2*k+1)] for j in range(n+1)]

	for idx in range(n-1, -1, -1):
		for tranNo in range(2*k-1, -1, -1):
			if tranNo % 2 == 0:
				dp[idx][tranNo] = max(-prices[idx] + dp[idx+1][tranNo+1],
									  dp[idx+1][tranNo])
			else:
				dp[idx][tranNo] = max(prices[idx] + dp[idx+1][tranNo+1],
									  dp[idx+1][tranNo])
	return dp[0][0]


def spaceOptimization(prices, k):
	n = len(prices)
	after = [0 for i in range(2*k+1)]
	cur = [0 for i in range(2*k+1)]

	for idx in range(n-1, -1, -1):
		for tranNo in range(2*k-1, -1, -1):
			if tranNo % 2 == 0:
				cur[tranNo] = max(-prices[idx] + after[tranNo+1],
								  after[tranNo])
			else:
				cur[tranNo] = max(prices[idx] + after[tranNo+1],
								  after[tranNo])
		after = cur[:]
	return after[0]



prices = [3, 2, 6, 5, 0, 3]
k = 2

print(recursion(prices, k))
print(memoization(prices, k))
print(tabulation(prices, k))
print(spaceOptimization(prices, k))