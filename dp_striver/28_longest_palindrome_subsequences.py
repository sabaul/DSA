"""
LONGEST PALINDROME SUBSEQUENCE
------------------------------

s = "bbbab"

subsequences -> b, ab, bb, bbb, bbbb, bab
longest -> bbbb --> ans = 4 (length = 4)

approach 1: 
	-> generate all subsequences
	-> find the longest palindrome

approach 2: using longest common subsequence

e.g. s1 = "bbabcbcab"
		    ----- --
	-> longest palindrome subsequence = "babcbab"
	-> answer len = 7
	-> it matches from the front and back

	-> write s1 in reverse order
	s2 = "bacbcbabb"
		  -- -----

	-> the LCS of s1 and s2 will be the answer
	-> the longest common sequence will be the longest palindrome subsequence
	-> YOU GOT YOUR ANSWER
"""


def recursion(s, t):

	def f(i, j):
		if i < 0 or j < 0:
			return 0

		# explore all possibilities
		if s[i] == t[j]:
			return 1 + f(i-1, j-1)
		else:
			return max(f(i-1, j), f(i, j-1))
	return f(len(s)-1, len(t)-1)


def memoization(s, t):
	n, m = len(s), len(t)
	dp = [[-1 for i in range(m+1)] for j in range(n+1)]

	def f(i, j):
		if i < 0 or j < 0:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]

		# explore all possibilities
		if s[i-1] == t[j-1]:
			dp[i][j] = 1 + f(i-1, j-1)
			return dp[i][j]
		else:
			dp[i][j] = max(f(i-1, j), f(i, j-1))
			return dp[i][j]

	return f(n-1, m-1)


def tabulation(s, t):
	n, m = len(s), len(t)
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	for j in range(m+1):
		dp[0][j] = 0
	for i in range(n+1):
		dp[i][0] = 0

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	# return dp[-1][-1]
	return dp[n][m]


def spaceOptimized(s, t):
	n, m = len(s), len(t)
	prev = [0 for i in range(m+1)]
	cur = [0 for i in range(m+1)]

	for j in range(m+1):
		prev[j] = 0

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				cur[j] = 1 + prev[j-1]
			else:
				cur[j] = max(prev[j], cur[j-1])
		prev = cur[:]
	return prev[m]




s1 = "bbabcbcab"
s2 = s1[::-1]

print(recursion(s1, s2))
print(memoization(s1, s2))
print(tabulation(s1, s2))
print(spaceOptimized(s1, s2))
# print(betterSpaceOptimized(s1, s2))

# print('='*10)

# s1 = "bbbab"
# s2 = s1[::-1]

# print(recursion(s1, s2))
# print(memoization(s1, s2))
# print(tabulation(s1, s2))
# print(spaceOptimized(s1, s2))