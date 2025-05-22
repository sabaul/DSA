"""
BEST TIME TO BUY AND SELL STOCKS WITH TRANSACTION FEE
-----------------------------------------------------
	* buy and sell can be done unlimited time
	* but a transaction fee is charged for each transaction

APPROACH: VERY SIMILAR TO THE DP ON STOCKS PROBLEM 2
	-> buy and sell allowed unlimited times

prices = [1, 3, 2, 8, 4, 9]
fee = 2
"""

def recursion(prices, fee):
	n = len(prices)

	def f(idx, buy):
		# base case
		if idx == n:
			return 0

		# explore possibilities
		if buy:
			return max(-prices[idx] + f(idx+1, 0),
					   0 + f(idx+1, 1))
		else:
			return max(prices[idx] + f(idx+1, 1) - fee,
					   0 + f(idx+1, 0))

	return f(0, 1)


def memoization(prices, fee):
	n = len(prices)
	dp = [[-1 for i in range(2)] for j in range(n)]

	def f(idx, buy):
		if idx == n:
			return 0

		if dp[idx][buy] != -1:
			return dp[idx][buy]

		if buy:
			dp[idx][buy] = max(-prices[idx] + f(idx+1, 0),
							   0 + f(idx+1, 1))
		else:
			dp[idx][buy] = max(prices[idx] + f(idx+1, 1) -fee,
							   0 + f(idx+1, 0))
		return dp[idx][buy]

	return f(0, 1)

prices = [1, 3, 2, 8, 4, 9]
fee = 2

print(recursion(prices, fee))
print(memoization(prices, fee))