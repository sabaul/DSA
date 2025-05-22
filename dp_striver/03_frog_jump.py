"""
A frog on 1st step of an N stairs long statement.
Frog wants to reach the Nth stair.

Height[i] is the height of (i + 1)th stair.
If frog jumps from ith to jth stair, the energy lost
in the jump is given by Height[i-1] - Height[j-1].

In the Frog is on ith staircase, he can jump either to
(i + 1)th stair or to (i + 2)th stair.

Find the minimum total energy used by the frog to reach
from 1st stair to Nth stair.

e.g.
10, 20, 30, 10
 0   1   2   3
 * > * > * > * --> 10 + 10 + 20 = 40
 * > * > > > * --> 10      + 10 = 20
 * > > > * > * --> 20 + 20      = 40

Answer: 
Min = 20 (path 2)


# Steps for recursion
1. Express the solution in terms of indices.
2. Do all stuffs on that index
3. Take the minimal of all stuffs

Want: 
f(n - 1) -> min Energy required to reach (n - 1) from 0


def f(idx):
	if idx == 0:
		return 0

	one_step = f(idx - 1) + abs(arr[idx] - arr[idx - 1])
	two_step = 0
	if idx > 1:
		two_step = f(idx - 2) + abs(arr[idx] - arr[idx - 2])

	return min(one_step, two_step)

"""



# def recursion(n, arr):
# 	if n == 0:
# 		return 0

# 	one_step = recursion(n - 1, arr) + abs(arr[n] - arr[n - 1])
# 	two_step = float('inf')
# 	if n > 1:
# 		two_step = recursion(n - 2, arr) + abs(arr[n] - arr[n - 2])

# 	return min(one_step, two_step)


# def helper(n, arr, store):
# 	if n == 0:
# 		return 0

# 	if store[n] != -1:
# 		return store[n]

# 	one_step = helper(n - 1, arr, store) + abs(arr[n] - arr[n - 1])
# 	two_step = float('inf')
# 	if n > 1:
# 		two_step = helper(n - 2, arr, store) + abs(arr[n] - arr[n - 2])

# 	arr[n] = min(one_step, two_step)
# 	return arr[n]

# def recursion_memoization(n, arr):
# 	return helper(n, arr, [-1] * (n + 1))



def f(n, arr):
	if n == 0:
		return 0

	oneStep = f(n - 1, arr) + abs(arr[n] - arr[n - 1])
	twoStep = float('inf')
	if n > 1:
		twoStep = f(n - 2, arr) + abs(arr[n] - arr[n - 2])
	return min(oneStep, twoStep)

def striver_recursion(n, arr):
	return f(n - 1, arr)



def f2(n, arr, dp):
	if n == 0: return 0

	if dp[n] != -1:
		return dp[n]

	oneStep = f2(n - 1, arr, dp) + abs(arr[n] - arr[n - 1])
	twoStep = float('inf')
	if n > 1:
		twoStep = f2(n - 2, arr, dp) + abs(arr[n] - arr[n - 2])

	dp[n] = min(oneStep, twoStep)
	return dp[n]

def striver_recursion_memoized(n, arr):
	store = [-1] * (n + 1)
	return f2(n - 1, arr, store)


def striver_tabulation(n, arr):
	dp = [-1] * n
	dp[0] = 0
	# dp[1] = [abs(arr[1] - arr[0])]

	for i in range(1, n):
		oneStep = dp[i - 1] + abs(arr[i] - arr[i - 1])
		twoStep = float('inf')
		if i > 1:
			twoStep = dp[i - 2] + abs(arr[i] - arr[i - 2])
		dp[i] = min(oneStep, twoStep)
	return dp[-1]


def striver_constant_space(n, arr):
	first = 0
	second = abs(arr[1] - arr[0])

	for i in range(2, n):
		oneStep = second + abs(arr[i] - arr[i - 1])
		twoStep = first + abs(arr[i] - arr[i - 2])
		third = min(oneStep, twoStep)
		first, second = second, third
	return min(first, second)




arr = [10, 20, 30, 10]
n = len(arr)
# print(recursion(n, arr))
# print(recursion_memoization(n, arr))

print(striver_recursion(n, arr))
print(striver_recursion_memoized(n, arr))
print(striver_tabulation(n, arr))
print(striver_constant_space(n, arr))