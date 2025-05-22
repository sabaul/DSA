"""
SAME AS Q. 37
=============

memoization stored in [n]*[4] array
how?
we are allowed 2 transactions:
	* B S B S
	* 0 1 2 3
	* e o e o ---> e = even, o = odd
		* buy on even
		* sell on odd

f(idx, transaction_no)
"""


def recursion(prices):
	n = len(prices)

	def f(idx, transaction):
		if idx == n or transaction == 4:
			return 0

		# explore possibilities
		if transaction % 2 == 0:	# buy
			return max(-prices[idx] + f(idx+1, transaction+1),
						0 + f(idx+1, transaction))
		else:						# sell
			return max(prices[idx] + f(idx+1, transaction+1),
						0 + f(idx+1, transaction))

	return f(0, 0)


def memoization(prices):
	n = len(prices)
	dp = [[-1 for i in range(4)] for j in range(n)]

	def f(idx, transaction):
		if idx == n or transaction == 4:
			return 0

		if dp[idx][transaction] != -1:
			return dp[idx][transaction]

		if transaction % 2 == 0:
			profit = max(-prices[idx] + f(idx+1, transaction+1),
						 0 + f(idx+1, transaction))
		else:
			profit = max(prices[idx] + f(idx+1, transaction+1),
						 0 + f(idx+1, transaction))
		dp[idx][transaction] = profit
		return dp[idx][transaction]

	return f(0, 0)


----------------------
# NOT WORKING PROPERLY
----------------------
# def tabulation(prices):
# 	n = len(prices)
# 	dp = [[0 for i in range(4)] for j in range(n+1)]

# 	# base case 1: idx == n
# 	for transaction in range(4):
# 		dp[n][transaction] = 0

# 	# transaction == 4
# 	for idx in range(n+1):
# 		dp[idx][3] = 0

# 	for idx in range(n-1, -1, -1):
# 		for transaction in range(2, -1, -1):
# 			if transaction % 2 == 0:
# 				profit = max(-prices[idx] + dp[idx+1][transaction+1],
# 							 0 + dp[idx+1][transaction])
# 			else:
# 				profit = max(prices[idx] + dp[idx+1][transaction+1],
# 							 0 + dp[idx+1][transaction])
# 			dp[idx][transaction] = profit
# 	return dp[0][0]


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(recursion(prices))
print(memoization(prices))
# print(tabulation(prices))
# print(spaceOptimization(prices))