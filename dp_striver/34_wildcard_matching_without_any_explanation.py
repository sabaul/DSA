def recursion(s, t, n, m):
	
	def f(i, j):
		# base cases
		if i < 0 and j < 0:
			return True
		if i < 0 and j >= 0:
			return False
		if j < 0 and i >= 0:
			for ii in range(i+1):
				if s[ii] != '*':
					return False
			return True

		# explore all possibilities
		if (s[i] == t[j]) or (s[i] == '?'):
			return f(i-1, j-1)

		if s[i] == '*':
			return f(i-1, j) or f(i, j-1)

		return False
	return f(n-1, m-1)


def memoization(s, t, n, m):
	dp = [[-1 for i in range(m)] for j in range(n)]

	def f(i, j):
		if i < 0 and j < 0:
			return True
		if i < 0 and j >= 0:
			return False
		if j < 0 and i >= 0:
			for ii in range(i+1):
				if s[ii] != '*':
					return False
			return True

		if dp[i][j] != -1:
			return dp[i][j]

		if (s[i] == t[j]) or (s[i] == '?'):
			dp[i][j] = f(i-1, j-1)
			return dp[i][j]

		if s[i] == '*':
			dp[i][j] = f(i-1, j) or f(i, j-1)
			return dp[i][j]

		dp[i][j] = False
		return dp[i][j]

	return f(n-1, m-1)

def memoizationShiftedIndex(s, t, n, m):
	dp = [[-1 for i in range(m+1)] for j in range(n+1)]

	def f(i, j):
		if i == 0 and j == 0:
			return True
		if i == 0 and j > 0:
			return False
		if j == 0 and i > 0:
			for ii in range(1, i+1):
				if s[ii-1] != '*':
					return False
			return True

		if dp[i][j] != -1:
			return dp[i][j]

		if (s[i-1] == t[j-1]) or (s[i-1] == '?'):
			dp[i][j] = f(i-1, j-1)
			return dp[i][j]

		if s[i-1] == '*':
			dp[i][j] = f(i-1, j) or f(i, j-1)
			return dp[i][j]

		dp[i][j] = False
		return dp[i][j]

	return f(n, m)


def tabulation(s, t, n, m):
	dp = [[False for i in range(m+1)] for j in range(n+1)]

	# Base conditions
	dp[0][0] = True

	for j in range(1, m+1):
		dp[0][j] = False

	for i in range(1, n+1):
		flag = True
		for ii in range(1, i+1):
			if s[ii-1] != '*':
				flag = False
				break
		dp[i][0] = flag


	for i in range(1, n+1):
		for j in range(1, m+1):
			if (s[i-1] == t[j-1]) or (s[i-1] == '?'):
				dp[i][j] = dp[i-1][j-1]
			elif s[i-1] == '*':
				dp[i][j] = dp[i-1][j] or dp[i][j-1]
			else:
				dp[i][j] = False
	return dp[n][m]


def spaceOptimization(s, t, n, m):
	prev = [False for i in range(m+1)]
	cur = [False for i in range(m+1)]

	prev[0] = True

	for j in range(1, m+1):
		prev[j] = False

	for i in range(1, n+1):
		# cur is the current row's column
		# and that cur's 0'th column has to be assigned everytime
		# move the third base case here
		
		flag = True
		for ii in range(1, i+1):
			if s[ii-1] != '*':
				flag = False
				break
		cur[0] = flag

		for j in range(1, m+1):
			if s[i-1] == t[j-1] or s[i-1] == '?':
				cur[j] = prev[j-1]
			elif s[i-1] == '*':
				cur[j] = prev[j] or cur[j-1]
			else:
				cur[j] = False
		prev = cur[:]
	return prev[m]



s1 = ["?ay", "ab*cd", "**abcd", "ab?d"]
s2 = ["ray", "abdefcd", "abcd", "abcc"]

for s, t in zip(s1, s2):
    # print(f"s: {s} || t: {t},\n{recursion(s, t)}, {memoization(s, t)}, {memoizationOneBased(s, t)}, {tabulation(s, t)}")
    n, m = len(s), len(t)
    print(f"s: {s} || t: {t}")
    print(f"Recursion: {recursion(s, t, n, m)}")
    print(f"Memoization: {memoization(s, t, n, m)}")
    print(f"Memo shift: {memoizationShiftedIndex(s, t, n, m)}")
    print(f"Tabulation: {tabulation(s, t, n, m)}")
    print(f"Space Optimization: {spaceOptimization(s, t, n, m)}")
    print('='*30)