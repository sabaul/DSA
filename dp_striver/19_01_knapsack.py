"""
-----------------
PROBLEM STATEMENT
-----------------
The problem statement is, we have a thief, he steals from houses

in a house, there are **n** items, each item has weight and value

theif has a bag where he keeps the stolen goods.
There is a limit on the weight the bag can carry.
The bag_limit = X

OBJECTIVE --> Maximize the value given the bag limit.

e.g. n = 3
weight = [ 3,  4,  5]
value =  [30, 50, 60]
bag_limit = 8 (can't carry more than 8kg)

approach 1: steals item 0 and 2 --> weight = (3+5=8) and value = (30+60=90)
approach 2: steals item 0 and 1 --> weight = (3+4=7) and value = (30+50=80)

approach 2 -> not the best option
so we go with **approach 1**


GREEDY WON'T WORK --> NO UNIFORMITY (WE MIGHT MISS OUT ON BETTER OPPORTUNITY)

============================================================
== TRY OUT ALL COMBINATIONS and pick the best combination ==
============================================================
					RECURSION
					=========

solution approach to maximize value:
------------------------------------
1. Express in terms of indices
	-> f(idx, weight)
2. Explore all possibilities
	-> pick/not_pick
3. Max of all possibilities


-----------------
make initial call to f(n-1, W)
-----------------
	-> till index (n-1) what max value you will get with 
	-> bag weight capacity of W?
"""


def recursion(n, W, value, weight):

	def f(idx, W):
		if idx == 0:
			if weight[idx] <= W:
				return value[idx]
			else:
				return 0

		notTake = f(idx-1, W)
		take = float('-inf')
		if weight[idx] <= W:
			take = value[idx] + f(idx-1, W-weight[idx])
		return max(take, notTake)

	return f(n-1, W)


def memoization(n, W, value, weight):
	dp = [[-1 for i in range(W + 1)] for j in range(n)]

	def f1(idx, W):
		if idx == 0:
			if weight[idx] <= W:
				return value[idx]
			else:
				return 0

		if dp[idx][W] != -1:
			return dp[idx][W]

		not_take = f1(idx-1, W)
		take = float('-inf')
		if weight[idx] <= W:
			take = value[idx] + f1(idx-1, W-weight[idx])

		dp[idx][W] = max(take, not_take)
		return dp[idx][W]

	return f1(n-1, W)


def tabulation(n, W, value, weight):
	dp = [[0 for i in range(W+1)] for j in range(n)]

	for wei in range(weight[0], W+1):
		dp[0][wei] = value[0]

	for i in range(1, n):
		for wei in range(W+1):
			not_take = dp[i-1][wei]
			take = float('-inf')
			if weight[i] <= wei:
				take = value[i] + dp[i-1][wei-weight[i]]

			dp[i][wei] = max(take, not_take)
	return dp[n-1][W]



def spaceOptimized(n, W, value, weight):
	prev = [0 for i in range(W+1)]
	cur = [0 for i in range(W+1)]

	for wei in range(weight[0], W+1):
		prev[wei] = value[0]

	for i in range(1, n):
		for wei in range(W+1):
			not_take = prev[wei]
			take = float('-inf')
			if weight[i] <= wei:
				take = value[i] + prev[wei-weight[i]]

			cur[wei] = max(take, not_take)
		prev = cur
	return prev[W]



def singleArraySpaceOptimized(n, W, value, weight):
	prev = [0 for i in range(W+1)]

	for wei in range(weight[0], W+1):
		prev[wei] = value[0]

	for i in range(1, n):
		for wei in range(W, -1, -1):
			notTake = prev[wei]
			take = float('-inf')
			if weight[i] <= wei:
				take = value[i] + prev[W - weight[i]]

			prev[wei] = max(take, notTake)
	return prev[W]




weight = [ 3,  2,  5]
value =  [30, 50, 60]
bag_limit = 6
n = len(weight)
print(recursion(n, bag_limit, value, weight))
print(memoization(n, bag_limit, value, weight))
print(tabulation(n, bag_limit, value, weight))
print(spaceOptimized(n, bag_limit, value, weight))
print(singleArraySpaceOptimized(n, bag_limit, value, weight))


# weight = [ 3,  4,  5]
# value =  [30, 50, 60]
# bag_limit = 8
# n = len(weight)
# print(recursion(n, bag_limit, value, weight))
# print(memoization(n, bag_limit, value, weight))
# print(tabulation(n, bag_limit, value, weight))
# print(spaceOptimized(n, bag_limit, value, weight))