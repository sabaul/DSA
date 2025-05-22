"""
BEST TIME TO BUY AND SELL STOCKS WITH COOLDOWN
----------------------------------------------
	* unlimited transactions allowed
	* COOLDOWN --> can't buy right after sell
		* at least one day gap in between sell and another buy

------------------------
previous stock problems:
------------------------
	* stock 1 -> 1 transactions allowed
	* stock 2 -> unlimited transactions
	* stock 3 -> 2 transactions allowed
	* stock 4 -> k transactions allowed
	* stock 5 -> unlimited times with cooldown
		* at least one day gap between sell and another buy
		* follow same as stock 2 solution, just take a 1 day gap after selling

prices = [4, 9, 0, 4, 10]
"""


def recursion(prices):
	n = len(prices)

	def f(idx, buy):
		# base cases
		if idx >= n:
			return 0

		# explore possibilities
		if buy:
			# buy or not buy at index = idx
			return max(-prices[idx] + f(idx+1, 0),
					   0 + f(idx+1, 1))
		else:
			# sell or not sell at index = idx
			return max(+prices[idx] + f(idx+2, 1),
					   0 + f(idx+1, 0))
	return f(0, 1)


def memoization(prices):
	n = len(prices)
	dp = [[-1 for i in range(2)] for j in range(n)]

	def f(idx, buy):
		if idx >= n:
			return 0

		if dp[idx][buy] != -1:
			return dp[idx][buy]

		if buy:
			dp[idx][buy] = max(-prices[idx] + f(idx+1, 0),
							   0 + f(idx+1, 1))
		else:
			dp[idx][buy] = max(prices[idx] + f(idx+2, 1),
							   0 + f(idx+1, 0))
		return dp[idx][buy]
	return f(0, 1)


def tabulation(prices):
	n = len(prices)
	dp = [[0 for i in range(2)] for j in range(n+2)]

	for idx in range(n-1, -1, -1):
		for buy in range(2):
			if buy:
				dp[idx][buy] = max(-prices[idx] + dp[idx+1][0],
								   0 + dp[idx+1][1])
			else:
				dp[idx][buy] = max(prices[idx] + dp[idx+2][1],
								   0 + dp[idx+1][0])
	return dp[0][1]


def tabulationV2(prices):
	n = len(prices)
	dp = [[0 for i in range(2)] for j in range(n+2)]

	for idx in range(n-1, -1, -1):
		dp[idx][1] = max(-prices[idx] + dp[idx+1][0],
						 0 + dp[idx+1][1])
		dp[idx][0] = max(prices[idx] + dp[idx+2][1],
						 0 + dp[idx+1][0])
	return dp[0][1]


def spaceOptimization(prices):
	n = len(prices)

	front2 = [0 for i in range(2)]
	front1 = [0 for i in range(2)]
	cur = [0 for i in range(2)]

	for idx in range(n-1, -1, -1):
		cur[1] = max(-prices[idx] + front1[0],
					 0 + front1[1])
		cur[0] = max(prices[idx] + front2[1],
					 0 + front1[0])

		front2 = front1[:]
		front1 = cur[:]
	return cur[1]



prices = [4, 9, 0, 4, 10]
print(recursion(prices))
print(memoization(prices))
print(tabulation(prices))
print(tabulationV2(prices))
print(spaceOptimization(prices))