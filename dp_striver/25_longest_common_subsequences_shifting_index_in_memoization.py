"""
STARTING FROM DP ON STRINGS
PROBLEMS ON 
	-> comparison
	-> replacements/edits


---------------------------
LONGEST COMMON SUBSEQUENCES
---------------------------

s1 = "adebc"
s2 = "dcadb"


Q.> what is subsequence?
e.g. abc -> a, b, c, ab, bc, ac, abc, ""
	-> maintaining the order of occurance, but doesn't necessarily
	   needs to be contiguous. It can be contiguous.
	-> no. of subsequences for "abc" = 8
	-> for string of length n, no. of subsequences = 2^n



Longest common subsequence
--------------------------
-> s1 can generate 2^5 subsequences
-> s2 can generate 2^5 subsequences
	-> get the longest common subsequence
	-> ANSWER: "adb" occurs in s1 and s2
			   lcs = 3 (length of adb)


* Brute Force -> Exponential in nature
	-> generate all subsequences, then compare one by one
	-> 2^n

* Generate all subsequences and compare on way -> RECURSION

e.g. s1=acd / s2=ced
	    012      012

Rules to write recurrence
1. Express problem in terms of indices
	-> single string can't express this problem, we need 2 indices
	-> f(idx1, idx2)
		- e.g. f(2, 2) represents lcs of str1(0...2) and str2(0....2)
			   f(2, 5) represents lcs of str1(0...2) and str2(0....5)

2. Explore all possibilities on that index
	-> do comparisons character wise
	-> if both character are matching
		-> if s1[idx1] == s2[idx2]: 
		       return 1 + f(idx1-1, idx2-1)

	-> if characters are not matching
	-> explore both the possibility that
		-> reducing idx1 might give best result
		-> reducing idx2 might give best result
			-> if s1[idx1] != s2[idx2]:
			       return max(f(idx1-1, idx2), f(idx1, idx2-1))



3. Take the best among them
	-> return max of both the possibilities
"""


def recursion(s1, s2):

	def f(idx1, idx2):
		# base case
		if idx1 < 0 or idx2 < 0:
			return 0

		# all possibilities
		# match
		if s1[idx1] == s2[idx2]:
			return 1 + f(idx1-1, idx2-1)
		# doesn't match
		return max(f(idx1-1, idx2), f(idx1, idx2-1))
	return f(len(s1)-1, len(s2)-1)


def memoization(s1, s2):
	n1, n2 = len(s1), len(s2)
	dp = [[-1 for i in range(n2)] for j in range(n1)]

	def f(idx1, idx2):
		if idx1 < 0 or idx2 < 0:
			return 0

		if dp[idx1][idx2] != -1:
			return dp[idx1][idx2]

		if s1[idx1] == s2[idx2]:
			dp[idx1][idx2] = 1 + f(idx1-1, idx2-1)
			return dp[idx1][idx2]

		dp[idx1][idx2] = max(f(idx1-1, idx2), f(idx1, idx2-1))
		return dp[idx1][idx2]

	return f(n1-1, n2-1)


def memoizationShiftingIndex(s1, s2):
	n, m = len(s1), len(s2)
	dp = [[-1 for i in range(m+1)] for j in range(n+1)]

	def f(i, j):
		if i == 0 or j == 0:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]

		if s1[i-1] == s2[j-1]:
			dp[i][j] = 1 + f(i-1, j-1)
			return dp[i][j]

		dp[i][j] = max(f(i-1, j), f(i, j-1))
		return dp[i][j]

	return f(n, m)



def tabulation(s1, s2):
	n, m = len(s1), len(s2)
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	for i in range(n):
		dp[i][0] = 0
	for j in range(m):
		dp[0][j] = 0

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[-1][-1]



def spaceOptimization(s1, s2):
	n, m = len(s1), len(s2)
	prev = [0 for i in range(m+1)]
	cur = [0 for i in range(m+1)]

	for j in range(m):
		prev[j] = 0

	for i in range(1, n+1):
		for j in range(1, m+1):
			if s1[i-1] == s2[j-1]:
				cur[j] = 1 + prev[j-1]
			else:
				cur[j] = max(prev[j], cur[j-1])
		prev = cur[:]
	return prev[m]




s1 = 'acd'
s2 = 'ced'
print(recursion(s1, s2))
print(memoization(s1, s2))
print(memoizationShiftingIndex(s1, s2))
print(tabulation(s1, s2))
print(spaceOptimization(s1, s2))

print('='*5)

s1 = "adebc"
s2 = "dcadb"
print(recursion(s1, s2))
print(memoization(s1, s2))
print(memoizationShiftingIndex(s1, s2))
print(tabulation(s1, s2))
print(spaceOptimization(s1, s2))