"""
SAME AS Q17 BUT WITH INCLUDING ZEROES IN THE SUBSET
---------------------------------------------------
no. of subsets sum = k

arr = [0, 0, 1], sum = 1
ans based on the previous code = 1 subset --> [1]
	-> because in constraints, it was written that
	-> arr[i] > 0

but it should be 4 subsets
	-> [1], [0, 1], [0, 1], [0, 0, 1]
	-> now let's change the constraints to be
	-> arr[i] >= 0


compute no. of zeroes = 2
subsets for these 2 zeroes = [], [0, .], [., 0], [0, 0]
add 1 to it --> [1], [0, 1], [1, 0], [0, 0, 1]


how many ways can we represent the 2 zeroes: pow(2, n) * #ans

+++++++++++++++++++power set+++++++++++++++++++


"""


def memoization(n, target, arr):
	dp = [[-1 for i in range(target + 1)] for j in range(n)]

	def f(i, target):
		if i == 0:
			if target == 0 and arr[i] == 0:
				return 2
			if target == 0:
				return 1
			if arr[i] == target:
				return 1
			return 0

		if dp[i][target] != -1:
			return dp[i][target]

		# explore all possibilities
		not_pick = f(i-1, target)
		pick = 0
		if arr[i] <= target:
			pick = f(i-1, target - arr[i])
		dp[i][target] = pick + not_pick
		return dp[i][target]
	return f(n-1, target)