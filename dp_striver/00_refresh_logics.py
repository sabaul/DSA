def memoization(n, coins, amount):
	dp = [[-1 for i in range(amount+1)] for j in range(n)]

	def f(i, target):
		if i == 0:
			if target % coins[0] == 0:
				return target // coins[0]
			return float('inf')

		if dp[i][target] != -1:
			return dp[i][target]

		nottake = f(i-1, target)
		take = float('inf')
		if coins[i] <= target:
			take = 1 + f(i, target-coins[i])
		dp[i][target] = min(take, nottake)
		return dp[i][target]
	return f(n-1, amount)


def recursion(n, coins, amount):
	def f(i, target):
		if i == 0:
			if target % coins[0] == 0:
				return amount // coins[0]
			return float('inf')

		nottake = f(i-1, target)
		take = float('inf')
		if coins[i] <= target:
			take = 1 + f(i, target-coins[i])
		return min(take, nottake)
	return f(n-1, amount)


def coinChange(coins, amount):
	n = len(coins)

	res = recursion(n, coins, amount)
	return res if res != float('inf') else -1