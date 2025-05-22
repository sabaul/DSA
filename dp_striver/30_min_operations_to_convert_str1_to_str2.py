"""
MIN. OPERATIONS TO CONVERT STRING 1 TO STRING 2
* OPERATIONS
	-> delete any char. in str1
	-> insert anywhere in str1
-----------------------------------------------
str1 = "abcd"
str2 = "anc"


NOTE:
-> it is always possible to convert str1 to str2
-> max no. of operations
	-> delete all characters of str1 -> len(str1)
	-> insert all characters of str2 -> len(str2)
		-> max no. of operations = len(str1) + len(str2)

WHAT CAN I NOT TOUCH??
----------------------
-> abcd to anc conversion is possible with
	-> 2 deletion and 1 insertion

-> the common portion from str1 and str2 is **LONGEST COMMON SUBSEQUENCE**
-> SO I CAN'T TOUCH THE **LONGEST COMMON SUBSEQUENCE**

------------------------------------------
-> NO. OF  DELETION = len(str1) - len(LCS)
-> NO. OF INSERTION = len(str2) - len(LCS)

===================================================================
-> TOTAL NO. OF OPERATIONS = len(str1) + len(str2) - (2 * len(LCS))
===================================================================
------------------------------------------
"""


def spaceOptimization(s, t, n, m):
	prev = [0 for j in range(m+1)]
	cur = [0 for j in range(m+1)]

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				cur[j] = 1 + prev[j-1]
			else:
				cur[j] = max(prev[j], cur[j-1])
		prev = cur
	return prev[m]


def tabulation(s, t, n, m):
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[n][m]


def memoization(s, t, n, m):
	dp = [[-1 for i in range(m+1)] for j in range(n+1)]

	def f(i, j):
		if i < 0 or j < 0:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]

		if s[i-1] == t[j-1]:
			dp[i][j] = 1 + f(i-1, j-1)
			return dp[i][j]
		dp[i][j] = max(f(i-1, j), f(i, j-1))
		return dp[i][j]

	return f(n, m)


def recursion(s, t, n, m):
	def f(i, j):
		# base case
		if i < 0 or j < 0:
			return 0

		# explore all possibilities
		if s[i] == t[j]:
			return 1 + f(i-1, j-1)
		return max(f(i-1, j), f(i, j-1))

	return f(n-1, m-1)




def solve(s, t):
	n, m = len(s), len(t)
	# lcs = recursion(s, t, n, m)
	# lcs = memoization(s, t, n, m)
	# lcs = tabulation(s, t, n, m)
	lcs = spaceOptimization(s, t, n, m)
	operations = n + m - (2 * lcs)
	return operations


s = "abcd"
t = "anc"

print(solve(s, t))