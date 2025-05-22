"""
BEST TIME TO BUY AND SELL STOCK 2
---------------------------------
Given prices of stocks on each day, you are allowed to buy and sell stocks. You can 
buy as many times as you want and sell as many times as you want. MAXIMIZE PROFIT.

You have to buy then sell, buy then sell and so on.
You can't do buy buy and sell sell.

Before buying stocks, you should have sold previous bought stocks.


prices = [7, 1, 5, 3, 6, 4]


approaches:
	* [7, 1, 5, 3, 6, 4]
	-     B  S  B  S ----> 4 + 3 = 7
	-     B        S ----> 5
	---> ANSWER = 7


HOW TO SOLVE/APPROACH THE PROBLEM:
-------------------------

7 1 5 3 6 4
^
|

let's say we start at index 0, what all can I do?
	* I can buy or sell
	* There are a lot of ways
	* TRY ALL WAYS
		* RECURSION
	* SELECT BEST AMONG THE ALL WAYS


HOW TO WRITE RECURRENCE IN DP
-----------------------------
1. Express in terms of indices
	* On any index, we have to know if we have previously bought or sold
	* I need to know if I have bought previously or not
	* f(idx, buy)
		* buy = 1 (can buy)
		* buy = 0 (can't buy)

		* e.g. f(0, 1)
			* Starting on 0th day with buy, what is the max profit we can get
			* This is how we will be starting the recursion calls.
				* Starting on first day with buy, what is max profit achievable

2. Explore all possibilities at that index (index=day)
	

3. Take the max of profits made among them

"""



def recursion(prices):
	n = len(prices)

	def f(i, buy):
		# buy = 1 (can buy)
		# buy = 0 (can't buy)
		# base cases
		if i == n:
			# if buy == 0, we are still holding a stock and haven't 
			# sold the last bought stock
			return 0

		# explore all possibilities
		if buy:
			# with buy=1, we can buy or not buy (take or notTake)
			profit_with_buy = -prices[i] + f(i+1, 0)
			profit_with_not_buy = 0 + f(i+1, 1)

			profit = max(profit_with_buy, profit_with_not_buy)
		else:
			# here it's not possible to buy 
			# with buy=0, the only available option is to sell or not sell
			profit_with_sell = prices[i] + f(i+1, 1)
			profit_without_sell = 0 + f(i+1, 0)

			profit = max(profit_with_sell, profit_without_sell)
		return profit

	return f(0, 1)


def memoization(prices):
	n = len(prices)
	# dp array will be of size (n, 2)
	# n because len(prices) == n
	# 2 because the buy can have 2 options, buy or sell
	dp = [[-1 for i in range(2)] for j in range(n)]

	def f(i, buy):
		if i == n:
			return 0

		if dp[i][buy] != -1:
			return dp[i][buy]

		if buy:
			profit_with_buy = -prices[i] + f(i+1, 0)
			profit_without_buy = 0 + f(i+1, 1)

			profit = max(profit_with_buy, profit_without_buy)
			dp[i][buy] = profit
		else:
			profit_with_sell = prices[i] + f(i+1, 1)
			profit_without_sell = f(i+1, 0)

			profit = max(profit_with_sell, profit_without_sell)
			dp[i][buy] = profit
		return dp[i][buy]

	return f(0, 1)


def tabulation(prices):
	n = len(prices)
	dp = [[0 for i in range(2)] for j in range(n+1)]

	# base case
	# for idx == 0, profit = 0
	# recursion started from 0 -> n
	# tabulation stars from n -> 0
	dp[n][0] = dp[n][1] = 0

	for i in range(n-1, -1, -1):
		for buy in range(2):
			if buy:
				profit_with_buy = -prices[i] + dp[i+1][0]
				profit_without_buy = dp[i+1][1]

				profit = max(profit_with_buy, profit_without_buy)
				dp[i][buy] = profit
			else:
				profit_with_sell = prices[i] + dp[i+1][1]
				profit_without_sell = dp[i+1][0]

				profit = max(profit_with_sell, profit_without_sell)
				dp[i][buy] = profit
	return dp[0][1]


def spaceOptimization(prices):
	n = len(prices)
	ahead = [0, 0]
	cur = [0, 0]

	ahead[0] = ahead[1] = 0

	for i in range(n-1, -1, -1):
		for buy in range(2):
			if buy:
				profit_with_buy = -prices[i] + ahead[0]
				profit_without_buy = ahead[1]

				profit = max(profit_with_buy, profit_without_buy)
				ahead[buy] = profit
			else:
				profit_with_sell = prices[i] + ahead[1]
				profit_without_sell = ahead[0]

				profit = max(profit_with_sell, profit_without_sell)
				ahead[buy] = profit
		cur = ahead[:]
	return ahead[1]


def spaceOptimizationAnotherWay(prices):
	n = len(prices)

	aheadNotBuy = aheadBuy = curNotBuy = curBuy = 0

	for i in range(n-1, -1, -1):
		for buy in range(2):
			if buy:
				profit_with_buy = -prices[i] + aheadNotBuy
				profit_without_buy = aheadBuy

				curBuy = max(profit_with_buy, profit_without_buy)
			else:
				profit_with_sell = prices[i] + aheadBuy
				profit_without_sell = aheadNotBuy

				curNotBuy = max(profit_with_sell, profit_without_sell)
		aheadBuy = curBuy
		aheadNotBuy = curNotBuy

	return aheadBuy

def v2(prices):
	n = len(prices)

	aheadNotBuy = aheadBuy = curNotBuy = curBuy = 0

	for i in range(n-1, -1, -1):
		for buy in range(2):
			if buy:
				curBuy = max(-prices[i] + aheadNotBuy, aheadBuy)
			else:
				curNotBuy = max(prices[i] + aheadBuy, aheadNotBuy)
		aheadBuy = curBuy
		aheadNotBuy = curNotBuy
	return aheadBuy



# prices = [7, 1, 5, 3, 6, 4]

prices = [1, 2, 3, 4, 5]

print(recursion(prices))
print(memoization(prices))
print(tabulation(prices))
print(spaceOptimization(prices))
print(spaceOptimizationAnotherWay(prices))
print(v2(prices))