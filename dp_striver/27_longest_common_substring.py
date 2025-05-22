"""
LONGEST COMMON SUBSTRING
------------------------

s1 = "abcjklp"
s2 = "acjkp"

longest common substring = cjk
length = 3

========================
subsequence vs substring
----------xxxx----------
substring -> has to be consecutive
subsequence -> can be and can't be consecutive
========================


def longestCommonSubsequence():
	# matching
	dp[i][j] = 1 + dp[i-1][j-1]

	# not matching
	dp[i][j] = max(dp[i-1][j], dp[i][j-1])


----------------------------------------------------------------
THE NOT-MATCHING ALGO FROM LONGESTCOMMONSUBSEQUENCE DOESN'T WORK
----------------------------------------------------------------
WHY???

e.g. acd || axd
	-> it's a subsequence, so it can break and we can omit c & x
	-> and the answer will be 2 -> ad || ad (longest subsequence)

	-> but the same can't be done for SUBSTRING
	-> we can't omit any character in between
----------------------------------------------------------------

the not matching case from longestCommonSubsequence will become:
dp[i][j] = 0
"""


def tabulation(s, t):
	n, m = len(s), len(t)
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	for j in range(m+1):
		dp[0][j] = 0
	for i in range(n+1):
		dp[i][0] = 0

	res = 0
	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = 0
			res = max(res, dp[i][j])
	return res


def spaceOptimization(s, t):
	n, m = len(s), len(t)
	prev = [0 for i in range(m+1)]
	cur = [0 for i in range(m+1)]

	res = 0
	for i in range(1, n+1):
		for j in range(1, m+1):
			if s[i-1] == t[j-1]:
				cur[j] = 1 + prev[j-1]
				res = max(res, cur[j])
			else:
				cur[j] = 0
		prev = cur[:]
	return res


s = "abcjklp"
t = "acjkp"
print(tabulation(s, t))
print(spaceOptimization(s, t))