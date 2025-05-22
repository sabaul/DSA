"""
BEST TIME TO BUY AND SELL STOCK
-------------------------------
Given an array of prices of stock on that given day, maximize the profit. You can
only buy and sell the stock once.

arr = [7, 1, 5, 3, 6, 4]

buy @ 1, and sell @ 6, max profit = 5 ----> ANSWER


APPROACH
--------
* buy @ minimum price
* sell @ maximum price
* BUY SHOULD HAPPEN BEFORE SELL
	* if you are selling on i'th day, you buy on the minimum price from
	  1st day to (i-1)th day.

* Keep track of the minimum element
"""



def mySolution(arr):
	n = len(arr)
	if n == 1:
		return 0

	l, r = 0, 1
	maxProfit = profit = 0
	while r < n:
		if arr[r] > arr[l]:
			profit = arr[r] - arr[l]
			maxProfit = max(profit, maxProfit)
		else:
			l = r
		r += 1
	return maxProfit



def striverSolution(arr):
	n = len(arr)
	mini = arr[0]
	maxProfit = 0

	for i in range(1, n):
		cost = arr[i] - mini
		maxProfit = max(maxProfit, cost)
		mini = min(mini, arr[i])
	return maxProfit




arr = [7, 1, 5, 3, 6, 4]
print(mySolution(arr))
print(striverSolution(arr))