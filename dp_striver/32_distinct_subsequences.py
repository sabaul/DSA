"""
DISTINCT SUBSEQUENCES
---------------------
Given 2 strings s1 and s2, count how many times string 2 appears in string 1

e.g.
====
s1 = "babgbag"
s2 = "bag"


s2 appears like:
    -> baxg
    -> baxxxxg
    -> b****ag
    -> xxxxbag
    -> xxbxxag
=> s2 appears 5 times


-> WE NEED ALL POSSIBLE POSSIBILITIES
-> RECURSION is what we need


How to approach recursion:
1. Express problem in terms of indices
    -> we need count, base case will return 1 or 0
    -> how to write recurrence:-->
        -> f(i, j)
        -> i represents s1 and j represents s2
        -> f(i, j) -> no. of distinct subsequences of string 
                      s2[0...j] from string s1[0....i]
                      
2. Explore all possibilities on that index
    -> take the character
    -> not take the character
    
3. Return the count
    ->


"""


def recursion(s, t):
    n, m = len(s), len(t)

    def f(i, j):
        # base case
        if j < 0:
            return 1
        if i < 0:
            return 0

        # explore all possibilities
        # take and not take 
        # when character matches
        #     -> take or notTake
        # when character doesn't matches
        #     -> don't take
        if s[i] == t[j]:
            notTake = f(i-1, j)
            take = f(i-1, j-1)
            return take+notTake
        else:
            notTake = f(i-1, j)
            return notTake
    return f(n-1, m-1)


def memoization(s, t):
    n, m = len(s), len(t)
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]
    
    def f(i, j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i-1] == t[j-1]:
            notTake = f(i-1, j)
            take = f(i-1, j-1)
            dp[i][j] = take+notTake
            return dp[i][j]
        else:
            notTake = f(i-1, j)
            dp[i][j] = notTake
            return dp[i][j]
    
    return f(n, m)


def tabulation(s, t):
    n, m = len(s), len(t)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

def spaceOptimization(s, t):
    n, m = len(s), len(t)
    prev = [0 for i in range(m+1)]
    cur = [0 for i in range(m+1)]
    cur[0] = prev[0] = 1

    for i in range(1, n+1):
        for j in range(m+1):
            if s[i-1] == t[j-1]:
                cur[j] = prev[j] + prev[j-1]
            else:
                cur[j] = prev[j]
        prev = cur[:]
    return prev[-1]

def betterSpaceOptimization(s, t):
    n, m = len(s), len(t)
    prev = [0 for i in range(m+1)]
    prev[0] = 1

    for i in range(1, n+1):
        for j in range(m, 0, -1):
            if s[i-1] == t[j-1]:
                prev[j] = prev[j] + prev[j-1]
            else:
                prev[j] = prev[j]
    return prev[-1]

s1 = "babgbag"
s2 = "bag"

print(recursion(s1, s2))
print(memoization(s1, s2))
print(tabulation(s1, s2))
print(spaceOptimization(s1, s2))
print(betterSpaceOptimization(s1, s2))
