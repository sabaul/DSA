"""
L1 --> Fibonacci
"""

def rec(n):
	if n <= 1:
		return n
	return rec(n - 1) + rec(n - 2)


def helper(n, store):
	if n == 0 or n == 1:
		return n

	if store[n] != -1:
		return store[n]
	store[n] = helper(n - 1, store) + helper(n - 2, store)
	return store[n]

def memo_rec(n):
	return helper(n, [-1] * (n + 1))


def fib_arr(n):
	arr = [-1] * (n + 1)
	arr[0] = 0
	arr[1] = 1

	for i in range(2, n + 1):
		arr[i] = arr[i - 1] + arr[i - 2]
	# print(arr)
	return arr[-1]


def fib_space_optimized(n):
	first = 0
	second = 1
	for i in range(2, n + 1):
		third = first + second
		first, second = second, third
	return third


# print(rec(5))
# print(memo_rec(100))
# print(fib_arr(100))
# print(fib_space_optimized(100))