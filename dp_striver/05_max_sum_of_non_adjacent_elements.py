"""
Given an array of N integers. You are supposed to return the max sum
of the subsequence with the constraint that no two elements are
adjacent in the given arraylist.
"""

def striver_recursion(n, arr):

	def f(i):
		if i == 0: return arr[i]
		if i < 0: return 0

		# take the i'th element
		pick = arr[i] + f(i - 2)

		# don't take the i'th element
		not_pick = f(i - 1)

		return max(pick, not_pick)

	return f(n - 1)


def striver_memoized_recursion(n, arr):
	dp = [-1] * n

	def f(i):
		if i == 0:
			return arr[i]
		if i < 0:
			return 0

		if dp[i] != -1:
			return dp[i]

		# take the i'th element
		pick = arr[i] + f(i - 2)

		# don't take the i'th element
		not_pick = f(i - 1)

		dp[i] = max(pick, not_pick)
		return dp[i]

	return f(n - 1)



def striver_tabulation(n, arr):
	dp = [-1] * n
	dp[0] = arr[0]

	for i in range(1, n):
		pick = float('-inf')
		if i - 2 >= 0:
			pick = arr[i] + dp[i - 2]
		not_pick = dp[i - 1]
		dp[i] = max(pick, not_pick)

	return dp[-1]

def striver_tabulation_v2(n, arr):
	dp = [-1] * n
	dp[0] = arr[0]

	for i in range(1, n):
		pick = arr[i]
		if i > 1:
			pick += dp[i - 2]

		not_pick = dp[i - 1]
		dp[i] = max(pick, not_pick)
	return dp[-1]


def striver_constant_space(n, arr):
	first = arr[0]
	second = max(arr[0], arr[1])
	for i in range(2, n):
		pick = arr[i] + first
		not_pick = second
		third = max(pick, not_pick)
		first, second = second, third
	# return max(first, second)
	return second


def striver_cs(n, arr):
	first = 0
	second = arr[0]
	for i in range(1, n):
		take = arr[i]
		if i > 1:
			take += first
		not_take = second
		third = max(take, not_take)
		first, second = second, third
	return second





arr = [2, 1, 4, 9]
# print(striver_recursion(len(arr), arr))
# print(striver_memoized_recursion(len(arr), arr))
# print(striver_tabulation(len(arr), arr))
# print(striver_tabulation_v2(len(arr), arr))
# print(striver_constant_space(len(arr), arr))
# print(striver_cs(len(arr), arr))

print('-'*10)

arr = [1, 8, 9]
# print(striver_recursion(len(arr), arr))
# print(striver_memoized_recursion(len(arr), arr))
# print(striver_tabulation(len(arr), arr))
# print(striver_tabulation_v2(len(arr), arr))
# print(striver_constant_space(len(arr), arr))
# print(striver_cs(len(arr), arr))



arr = [1,3,1]