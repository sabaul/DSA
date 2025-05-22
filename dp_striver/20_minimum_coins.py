"""
MINIMUM COINS --> DP ON SUBSEQUENCES
------------------------------------

Given an arr with infinite coin denominations = [1, 2, 3] and a target = 7.
Find the min. no. of coins that sum up to target.
If the answer is not possible, return -1.


solution = [3, 3, 1] --> min. no of coins = 3
		or [2, 2, 2, 1] --> coins = 4
		or [1, 1, 1, 1, 1, 1, 1] --> coins = 7


Greedy -> pick biggest coin -> 7//3 = 2, remaining = 7-6 = 1
	   -> next biggest = 1//2 = 0, can't use 2
	   -> next biggest = 1//1 = 1, can use one coin of denomination 1
	   		-> remaining = 1 - 1 = 0

Greedy works for this case, but it might fail for another test case.
When does Greedy fails?
	-> denominations = [9, 6, 5, 1], target = 11
	Solution:
	-> 11//9 = 1 coin of denomination 9, remaining = 2
	-> 2//1 = 2 coin of denomination 1, remaining = 0
		-> so we have the solution with 3 coins, and sum(those coins) = target
	-> BUT if we had picked [6, 5], with just 2 coins, the target = 11
	-> GREEDY FAILS HERE

-----------------------------------------------
-> GREEDY FAILS AS THERE IS NO UNIFORMITY HERE.
-----------------------------------------------

=========
recursion
=========

SO TRY OUT ALL COMBINATIONS TO FORM THE TARGET --> 0/1 KNAPSACK
-> TAKE THE COMBINATION WHICH HAS MINIMUM COINS


HOW TO WRITE RECURSION HERE
---------------------------
1. express recurrence in terms of index and another thing
	-> f(idx, T)
2. Explore all possibilities at the index 
	-> take the coin
	-> not take the coin
3. Find minimum of all possibilities

f(n-1, T) --> min. no. of coins used till index (n-1) to make target
"""

def recursion(n, T, coins):

	def f(i, T):
		# base case
		# started at (n-1), look at idx 0
		if i == 0:
			if T % coins[0] == 0:
				return T // coins[0]
			return float('inf')

		# explore all possibilities
		notTake = f(i-1, T)
		take = float('inf')
		if coins[i] <= T:
			take = 1 + f(i, T-coins[i])
		return min(notTake, take)

	return f(n-1, T)


def memoization(n, T, coins):
	dp = [[-1 for i in range(T+1)] for j in range(n)]

	def f(i, T):
		if i == 0:
			if T % coins[0] == 0:
				return T // coins[0]
			return float('inf')

		if dp[i][T] != -1:
			return dp[i][T]

		# explore all possibilities
		notTake = f(i-1, T)
		take = float('inf')
		if coins[i] <= T:
			take = 1 + f(i, T-coins[i])
		dp[i][T] = min(take, notTake)
		return dp[i][T]
	return f(n-1, T)


def tabulation(n, T, coins):
	dp = [[0 for i in range(T+1)] for j in range(n)]

	# base case
	for targ in range(T+1):
		if targ % coins[0] == 0:
			dp[0][targ] = targ // coins[0]
		else:
			dp[0][targ] = float('inf')

	# recursion to iterative
	# idx = 1 -> (n-1) (zero, already covered in base case)
	# target = 0 -> target
	for idx in range(1, n):
		for targ in range(T+1):
			notTake = dp[idx-1][targ]
			take = float('inf')
			if coins[idx] <= targ:
				take = 1 + dp[idx][targ-coins[idx]]
			dp[idx][targ] = min(take, notTake)
	return dp[n-1][T]


def spaceOptimized(n, T, coins):
	prev = [0 for i in range(T+1)]
	cur = [0 for i in range(T+1)]

	# base case
	for targ in range(T+1):
		if targ % coins[0] == 0:
			prev[targ] = targ // coins[0]
		else:
			prev[targ] = float('inf')

	# iterative
	for idx in range(1, n):
		for targ in range(T+1):
			notTake = prev[targ]
			take = float('inf')
			if coins[idx] <= targ:
				take = 1 + cur[targ-coins[idx]]
			cur[targ] = min(take, notTake)
		prev = cur
	return prev[-1]



denominations = [1, 2, 3]
target = 7
n = len(denominations)

print(recursion(n, target, denominations))
print(memoization(n, target, denominations))
print(tabulation(n, target, denominations))
print(spaceOptimized(n, target, denominations))