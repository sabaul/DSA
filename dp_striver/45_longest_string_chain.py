"""
LONGEST STRING CHAIN
--------------------

string chain --> a -> ab -> cab -> dcab -> dczab
	* adding one character at a time

Code Solution
-------------
	-> Longest Increasing Subsequence with compare function
		* compare function compares if the arr[i] and arr[j] 
		  are strings with only one character difference
		* arr[i] should have only one more extra character when
		  compared to arr[j]
"""

def compare(s, t):
	if len(s) != len(t)+1:
		return False

	first, second = 0, 0
	while first < len(s):
		if second < len(t) and s[first] == t[second]:
			first += 1
			second += 1
		else:
			first += 1

	if first == len(s) and second == len(t):
		return True
	return False

def lsc(arr):
	n = len(arr)
	arr.sort(key=len)

	res = 0
	dp = [1] * n

	for i in range(n):
		for prev in range(i):
			if compare(arr[i], arr[prev]) and 1 + dp[prev] > dp[i]:
				dp[i] = 1 + dp[prev]

		if dp[i] > res:
			res = dp[i]
	return res

words = ["a","b","ba","bca","bda","bdca"]
print(lsc(words))