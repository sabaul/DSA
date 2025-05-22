"""
PRINTING LONGEST COMMON SUBSEQUENCES
------------------------------------

s1 = "abcde"
s2 = "bdgek"

ANS = "bde"
"""

def printLCS(s1, s2):
	n, m = len(s1), len(s2)
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	for j in range(m+1):
		dp[0][j] = 0
	for i in range(n+1):
		dp[i][0] = 0

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	for row in dp:
		print(row)

	lcs = dp[n][m]
	print(f"LCS: {lcs}")
	s = [''] * lcs
	idx = lcs-1

	i, j = n, m
	while i > 0 and j > 0:
		if s1[i-1] == s2[j-1]:
			s[idx] = s1[i-1]
			idx -= 1
			i -= 1
			j -= 1
		elif dp[i-1][j] > dp[i][j-1]:
			i -= 1
		else:
			j -= 1


	return ''.join(s)


s1 = "abcde"
s2 = "bdgek"
print(printLCS(s1, s2))