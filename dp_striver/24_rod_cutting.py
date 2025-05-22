"""
ROD CUTTING PROBLEM --> LAST PROBLEM IN DP ON SUBSEQUENCES
----------------------------------------------------------

Given rod length N, cut it into pieces, the prices are given below for
the corresponding length. Find the maximum price you can get by cutting
the rod into pieces.


N = 5
rod length =  1  2  3  4   5
price arr  = [2, 5, 7, 8, 10]

e.g. rod length 1 + 1 + 1 + 1 + 1 = (2 * 5)   = 10
	 rod length 1 + 2 + 2         = (2 + 2*5) = 12
	 ---> maximize this cost you can achieve


--> THIS IS NOTHING BUT UNBOUNDED KNAPSACK
--> TRY TO PICK LENGTHS (FROM LENGTH ARRAY, IN ALL POSSIBLE WAYS --> RECURSION) 
	AND SUM THEM UP TO MAKE N LENGTH ROD.


RECURSION
=========
1. Express in terms of index
	-> f(idx, rod_length)
2. explore all possibilities
	-> take
	-> not take
3. maximize the possibilities
"""

def recursion(n, prices):

	def f(idx, rodLen):
		# base case
		if idx == 0:
			return rodLen * prices[0]

		# explore all possibilities
		notTake = f(idx-1, rodLen)
		take = float('-inf')
		curLen = idx+1
		if curLen <= rodLen:
			take = prices[idx] + f(idx, rodLen - curLen)
		return max(take, notTake)
	return f(n-1, n)



def memoization(n, prices):
	dp = [[-1 for i in range(n+1)] for j in range(n)]

	def f(idx, rodLen):
		if idx == 0:
			return rodLen * prices[0]

		if dp[idx][rodLen] != -1:
			return dp[idx][rodLen]

		# explore all possibilities
		notTake = f(idx-1, rodLen)
		take = float('-inf')
		curLen = idx+1
		if curLen <= rodLen:
			take = prices[idx] + f(idx, rodLen - curLen)
		dp[idx][rodLen] = max(take, notTake)
		return dp[idx][rodLen]
	return f(n-1, n)


def tabulation(n, prices):
	dp = [[0 for i in range(n+1)] for j in range(n)]

	for rodLen in range(n+1):
		dp[0][rodLen] = rodLen * prices[0]

	for idx in range(1, n):
		for rodLen in range(rodLen+1):
			notTake = dp[idx-1][rodLen]
			take = float('-inf')
			curLen = idx+1
			if curLen <= rodLen:
				take = prices[idx] + dp[idx][rodLen-curLen]
			dp[idx][rodLen] = max(take, notTake)
	return dp[n-1][n]


def spaceOptimized(n, prices):
	prev = [0 for i in range(n+1)]
	cur = [0 for i in range(n+1)]

	for rodLen in range(n+1):
		prev[rodLen] = rodLen * prices[0]

	for idx in range(1, n):
		for rodLen in range(n+1):
			notTake = prev[rodLen]
			take = float('-inf')
			curLen = idx+1
			if curLen <= rodLen:
				take = prices[idx] + cur[rodLen - curLen]
			cur[rodLen] = max(take, notTake)
		prev = cur
	return prev[n]


def betterSpaceOptimized(n, prices):
	prev = [0 for i in range(n+1)]

	for rodLen in range(n+1):
		prev[rodLen] = rodLen * prices[0]

	for idx in range(1, n):
		for rodLen in range(n+1):
			notTake = prev[rodLen]
			take = float('-inf')
			curLen = idx+1
			if curLen <= rodLen:
				take = prices[idx] + prev[rodLen - curLen]
			prev[rodLen] = max(take, notTake)
	return prev[n]


prices = [2, 5, 7, 8, 10]
n = len(prices)

print(recursion(n, prices))
print(memoization(n, prices))
print(tabulation(n, prices))
print(spaceOptimized(n, prices))
print(betterSpaceOptimized(n, prices))