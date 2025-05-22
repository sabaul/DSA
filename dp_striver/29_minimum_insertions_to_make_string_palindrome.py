"""
----------------------------------------------
MINIMUM INSERTIONS TO MAKE A STRING PALINDROME
----------------------------------------------
	-> you can insert any character anywhere

s = "abcaa"
s_reverse = "aacba"

new_s = s + s_reverse
	-> new_s is a PALINDROME
	-> no. of insertions to make it a palindrome = len(s)
	-> this is the MAXIMUM no. of insertions
	-> but we need MIN. no. of insertions

* to find min. no. of insertions:
	-> new_s = "aabcbaa"
	-> 2 insertions

=================================
HOW DO YOU APPROACH THIS PROBLEM?
=================================

s = "abcaa"

WAY 1
-----
* Keep the longest palindrome portion intact
	* e.g. keep "aaa" intact
	* we have "bc" left
	* add reverse of "bc" to make it palindrome
	* abcacba --> to make it a palindrome

WAY 2
-----
* Keep the longest palindrome portion intact
	* e.g. keep "aca" intact
	* we have "b", "a" left
	* add reverse of "ba" to make it palindrome
	* abacaba --> to make it a palindrome


SOLUTION WILL BE
----------------

answer = (length of string - longest palindromic subsequence)

"""


def recursion(s, t):
	n, m = len(s), len(t)

	def f(i, j):
		if i < 0 or j < 0:
			return 0

		# explore possibilities
		if s[i] == t[j]:
			return 1 + f(i-1, j-1)
		else:
			return max(f(i-1, j), f(i, j-1))
	return f(n-1, m-1)

def memoization(s, t):
	n, m = len(s), len(t)
	dp = [[-1 for i in range(m+1)] for j in range(n+1)]

	def f(i, j):
		if i == 0 or j == 0:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]

		if s[i] == t[j]:
			dp[i][j] = 1 + f(i-1, j-1)
			return dp[i][j]
		else:
			dp[i][j] = max(f(i-1, j), f(i, j-1))
			return dp[i][j]
	return f(n-1, m-1)


def tabulation(s, t):
	n, m = len(s), len(t)
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[n][m]


def spaceOptimization(s, t):
	n, m = len(s), len(t)
	prev = [0 for i in range(m+1)]
	cur = [0 for i in range(m+1)]

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				cur[j] = 1 + prev[j-1]
			else:
				cur[j] = max(prev[j], cur[j-1])
		prev = cur[:]
	return prev[m]

def solution(s):
	t = s[::-1]
	n = len(s)
	# lcs = recursion(s, t)
	lcs = memoization(s, t)
	# lcs = tabulation(s, t)
	# lcs = spaceOptimization(s, t)
	return n - lcs


s = "abcaa"
print(solution(s))