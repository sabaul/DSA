"""
Same question as lecture 3

But from step i
Frog can jump to i + 1, i + 2, i + 3 ..... i + k steps
"""

def f(idx, arr):
	if idx == 0: return 0
	fs = f(idx - 1) + abs(arr[i] - arr[i - 1])
	if idx > 1:
		ss = f(idx - 2) + abs(arr[i] - arr[i - 2])
	return min(fs, ss)


def fk(idx, arr):
	if idx == 0: return 0

	min_steps = float('inf')

	for j in range(1, k + 1):
		if (idx - j) >= 0:
			jump = fk(idx - j, arr) + abs(arr[idx] - arr[idx - j])
		min_steps = min(min_steps, jump)
	return min_steps

def fk_tabulation(n, arr):
	dp = [-1] * n
	dp[0] = 0
	for i in range(n):
		min_steps = float('inf')
		for j in range(1, k + 1):
			if (i - j) >= 0:
				jump = dp[i - j] + abs(arr[i] - arr[i - j])
			min_steps = min(min_steps, jump)
		dp[i] = min_steps
	return dp[-1]


# def fk_space_optimized(n, arr):