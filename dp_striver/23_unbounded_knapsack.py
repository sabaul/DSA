"""
UNBOUNDED KNAPSACK
------------------

* In 0/1 knapsack, there will be only one instances of items.
* In unbounded knapsack, there is an infinite supply of items.


WEIGHT = [2,  4, 6]
VALUE  = [5, 11, 13]
BAG_CAPACITY = 10

ways to pick up items:
	* wt-6 + wt-4 = 13 + 11 = 24
	* wt-6 + 2(wt-4) = 13 + 10 = 23
	* 2(wt-4) + wt-2 = 22 + 5 = 27 ---> max possible value (ANSWER)
	* 5(wt-2) = 25


RECURSION
---------
1. express in terms of indices
	-> f(idx, wt)
2. explore all possibilities
3. return max of every possibility


f(n-1, w) --> what is the max value you can generate at index (n-1)
			  and the bag weight capacity w


"""


def recursion(n, weights, values, bag_capacity):

	def f(idx, w):
		# base case
		if idx == 0:
			return (w//weights[0]) * values[0]

		# explore all possibility
		notTake = f(idx-1, w)
		take = 0
		if weights[idx] <= w:
			take = values[idx] + f(idx, w-weights[idx])
		return max(take, notTake)

	return f(n-1, bag_capacity)



def memoization(n, weights, values, bag_capacity):
	dp = [[-1 for i in range(bag_capacity+1)] for j in range(n)]

	def f(idx, w):
		if idx == 0:
			return (w//weights[0])*values[0]

		# check dp
		if dp[idx][w] != -1:
			return dp[idx][w]

		# explore possibilities
		notTake = f(idx-1, w)
		take = 0
		if weights[idx] <= w:
			take = values[idx] + f(idx, w-weights[idx])
		dp[idx][w] = max(take, notTake)
		return dp[idx][w]
	return f(n-1, bag_capacity)


def tabulation(n, weights, values, bag_capacity):
	dp = [[0 for i in range(bag_capacity+1)] for j in range(n)]

	for capacity in range(bag_capacity+1):
		dp[0][capacity] = (capacity // weights[0]) * values[0]

	for i in range(1, n):
		for cap in range(capacity+1):
			notTake = dp[i-1][cap]
			take = 0
			if weights[i] <= cap:
				take = values[i] + dp[i][cap-weights[i]]
			dp[i][cap] = max(take, notTake)
	return dp[n-1][bag_capacity]


def spaceOptimized(n, weights, values, bag_capacity):
	prev = [0 for i in range(bag_capacity+1)]
	cur = [0 for i in range(bag_capacity+1)]

	for cap in range(bag_capacity+1):
		prev[cap] = (cap // weights[0]) * values[0]

	for i in range(1, n):
		for cap in range(bag_capacity+1):
			notTake = prev[cap]
			take = 0
			if weights[i] <= cap:
				take = values[i] + cur[cap-weights[i]]
			cur[cap] = max(take, notTake)
		prev = cur
	return prev[-1]


def betterSpaceOptimized(n, weights, values, bagCapacity):
	""" 2 array to 1 array """
	prev = [0 for i in range(bagCapacity+1)]
	for cap in range(bagCapacity+1):
		prev[cap] = (cap // weights[0]) * values[0]

	for i in range(1, n):
		for cap in range(bagCapacity+1):
			notTake = prev[cap]
			take = 0
			if weights[i] <= cap:
				take = values[i] + prev[cap-weights[i]]
			prev[cap] = max(take, notTake)
	return prev[-1]



weights = [2,  4, 6]
values = [5, 11, 13]
bag_capacity = 10
n = len(weights)

print(recursion(n, weights, values, bag_capacity))
print(memoization(n, weights, values, bag_capacity))
print(tabulation(n, weights, values, bag_capacity))
print(spaceOptimized(n, weights, values, bag_capacity))
print(betterSpaceOptimized(n, weights, values, bag_capacity))