"""
BEST TIME TO BUY AND SELL STOCKS 3
==================================
Maximize the profit by doing at max 2 transactions.


prices = [3, 3, 5, 0, 0, 3, 1, 4]



SIMILAR TO BUY AND SELL STOCKS 2 BUT WITH ONE MORE CONDITION
That will be the number of transactions.

def recursion(prices):
	n = len(prices)

	def f(idx, buy, cap):
		# base cases
		if cap == 0:
			# can't buy/sell anymore
			# can't make any more transactions
			return 0

		if idx == n:
			# exhausted all the days
			return 0

		# explore all possibilities
		profit = 0
		if buy:
			profit = max(-prices[idx] + f(idx+1, 0, cap), 		# I buy, so now idx = idx+1, buy = 1 and in order to complete a transaction, it should be sold as well, so cap=cap
						 0 + f(idx+1, 1, cap)) 					# I do not buy, idx=idx+1, since not buy, buy=1, and as transaction not completed, cap=cap 
		else:
			profit = max(+prices[idx] + f(idx+1, 1, cap-1), 	# sold, now idx=idx+1, buy=1 as we just sold so now we can buy and since a transaction is complete cap=cap-1
						 0 + f(idx+1, 0, cap)) 					# not sold, now idx=idx+1, since not sold, so cant buy buy=0, an transaction not complete, so cap=cap
		return profit

	return f(0, 1, 2)
	# initial idx = 0
	# initial buy = 1, you can buy
	# initial cap = 2, capacity of buying the number of times

"""


def recursion(prices):
	n = len(prices)

	def f(idx, buy, cap):
		# base cases
		if cap == 0:
			# can't do any more transactions
			return 0

		if idx == n:
			# exhausted all the days
			return 0

		# explore all possibilities
		if buy:
			profit = max(-prices[idx] + f(idx+1, 0, cap),
						 0 + f(idx+1, 1, cap))
		else:
			profit = max(prices[idx] + f(idx+1, 1, cap-1),
						 0 + f(idx+1, 0, cap))
		return profit

	return f(0, 1, 2)



def memoization(prices):
	"""
	the dp array will be 3D, as the variables that are changing are:
		1. index -> len(prices) --> n
		2. buy -> 0/1 --> 2
		3. capacity -> 0/1/2 (max limit of transactions allowed)

	dp array size = [n] * [2] * [3]
	"""
	n = len(prices)
	dp = [[[-1 for k in range(3)] for j in range(2)] for i in range(n)]

	def f(idx, buy, cap):
		# base cases
		if cap == 0:
			return 0
		if idx == n:
			return 0

		if dp[idx][buy][cap] != -1:
			return dp[idx][buy][cap]

		if buy:
			profit = max(-prices[idx] + f(idx+1, 0, cap),
						 0 + f(idx+1, 1, cap))
		else:
			profit = max(prices[idx] + f(idx+1, 1, cap-1),
						 0 + f(idx+1, 0, cap))
		dp[idx][buy][cap] = profit
		return dp[idx][buy][cap]
	return f(0, 1, 2)


def tabulation(prices):
	"""
	the dp array will be 3D, as the variables that are changing are:
		1. index -> len(prices) --> n
		2. buy -> 0/1 --> 2
		3. capacity -> 0/1/2 (max limit of transactions allowed)

	dp array size = [n] * [2] * [3]

	# base cases
	1. if cap == 0: return 0
		-> if cap = 0, idx and buy can be anything, so make them zero
	2. if idx == n: return 0
		-> if idx = n, buy and cap can be anything, so make them zero
	"""

	n = len(prices)
	dp = [[[0 for k in range(3)] for j in range(2)] for i in range(n+1)]

	# # base case 1
	# for idx in range(n):
	# 	for buy in range(2):
	# 		dp[idx][buy][0] = 0

	# # base case 2
	# for buy in range(2):
	# 	for cap in range(3):
	# 		dp[n][buy][cap] = 0

	for idx in range(n-1, -1, -1):
		for buy in range(2):
			for cap in range(1, 3):
				if buy:
					profit = max(-prices[idx] + dp[idx+1][0][cap],
								 0 + dp[idx+1][1][cap])
				else:
					profit = max(prices[idx] + dp[idx+1][1][cap-1],
								 0 + dp[idx+1][0][cap])
				dp[idx][buy][cap] = profit
	return dp[0][1][2]


def spaceOptimization(prices):
	"""
	From 3D to 3D array.
	n will not be used anymore in 3D array
	we will keep 2 2D array of size 2x3,
	one for after state and one for current state
	"""
	n = len(prices)
	after = [[0 for i in range(3)] for j in range(2)]
	cur = [[0 for i in range(3)] for j in range(2)]

	for idx in range(n-1, -1, -1):
		for buy in range(2):
			for cap in range(1, 3):
				if buy:
					profit = max(-prices[idx] + after[0][cap],
								 0 + after[1][cap])
				else:
					profit = max(prices[idx] + after[1][cap-1],
								 0 + after[0][cap])
				cur[buy][cap] = profit
		after = cur[:]
	return after[1][2]


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(recursion(prices))
print(memoization(prices))
print(tabulation(prices))
print(spaceOptimization(prices))