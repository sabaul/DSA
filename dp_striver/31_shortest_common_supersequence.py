"""
Shortest Common Supersequence Length and print String
---------------------------------------------------

=============
SUPERSEQUENCE
=============
* Given string 1 and string 2, make a string such that
  the string s1 and s2 are both in the supersequence.


s1 = "brute"
s2 = "groot"

-> supersequence -> "brutegroot"
	-> len = 10
	-> both "brute" and "groot" are in the supersequence
	-> but we need shortest such super-sequence

-> supersequence -> "bgruoote"
	-> len = 8
	-> brute is here, and groot is also here
	-> this is indeed the shortest supersequence for these 2 strs


s1 = "bleed"
s2 = "blue"

-> super supersequence -> "bleued"
	-> has both s1 and s2

HOW TO GENERATE LENGTH OF SHORTEST SUPERSEQUENCE
------------------------------------------------
short form: LCS: Longest Common Subsequence
------------------------------------------------
Say, s1 = "brute" and s2 = "groot"

* Common guys taken once
	-> Common guys ===> LCS
	-> LCS gives us the longest common guy in both strings
	-> LCS = 2
* Now from s1, we need everyone except the LCS
	-> we need "bue" from s1 as "rt" is in LCS
* Now from s2, we need everyone except the LCS
	-> we need "goo" from s2 as "rt" is in LCS
* And take the LCS only once.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-> FOR THE LENGTH OF THE SHORTEST COMMON SUPERSEQUENCE
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-> WE NOW HAVE 
	-> shortest common supersequence = "BUE" + "rt" + "GOO"
	-> length of shortest common supersequence
		-> n + m - len(LCS)
		-> 5 + 5 - 2 ==> 8

LENGTH OF SHORTEST COMMON SUPERSEQUENCE = n + m - len(lcs)

Intuition:
-> Use the common characters once
-> and the remaining one's are the length
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


+++++++++++++++++++++++++++++++++++++++++++
NOW HOW TO PRINT THE STRING (SUPERSEQUENCE)
+++++++++++++++++++++++++++++++++++++++++++


# NOW HOW TO FIND THE SHORTEST COMMON SUPERSEQUENCE STRING
# SEE THE CODE BELOW

i = n, j = m
while i > 0 and j > 0:
	if s1[i-1] == s2[j-1]:
		ans += s1[i-1]
		i -= 1
		j -= 1
	elif dp[i-1][j] > dp[i][j-1]:
		# up movement
		ans += s1[i-1]
		i -= 1
	else:
		# down movement
		ans += s2[j-1]
		j -= 1


if i > 0 -> something from string 1 is remaining
if j > 0 -> something from string 2 is remaining

while i > 0:
	ans += s1[i-1]
while j > 0:
	ans += s2[i-1]


Reverse the answer and return
"""



"""

# printing the LCS DP MATRIX
s = "brute"
t = "groot"
n, m = len(s), len(t)
dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for row in dp:
	print(row)

res = []
i, j = n, m
while i > 0 and j > 0:
    if s[i-1] == t[j-1]:
        res.append(s[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        # move upward
        res.append(s[i-1])
        i -= 1
    else:
        # move left
        res.append(t[j-1])
        j -= 1

while i > 0:
    res.append(s[i-1])
    i -= 1
while j > 0:
    res.append(t[i-1])
    j -= 1
print(''.join(res[::-1]))


"""



def tabulation(s, t):
    n, m = len(s), len(t)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    res = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            res.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            res.append(s[i-1])
            i -= 1
        else:
            res.append(t[j-1])
            j -= 1

    while i > 0:
        res.append(s[i-1])
        i -= 1
    while j > 0:
        res.append(t[j-1])
        j -= 1
    return ''.join(res[::-1]), len(res)


def shortest_common_supersequence(s, t):
    return tabulation(s, t)

s = "brute"
t = "groot"
print(shortest_common_supersequence(s, t))
