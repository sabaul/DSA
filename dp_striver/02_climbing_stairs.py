"""
You can jump 1 or 2 stairs at a time.
Find the number of ways you can go from the bottom
to the top of the stairs.
"""

def recursion(n):
	if n == 0 or n == 1:
		return n
	return recursion(n - 1) + recursion(n - 2)


def helper(n, arr):
	if n == 0 or n == 1:
		return n
	if arr[n] != -1:
		return arr[n]
	arr[n] = helper(n - 1, arr) + helper(n - 2, arr)
	return arr[n]

def recursion_memoized(n):
	arr = [-1] * (n + 1)
	arr[0] = 0
	arr[1] = 1
	return helper(n, arr)


# print(recursion(10))
print(recursion_memoized(10))