"""
EDIT DISTANCE -> string matching
-------------
Given 2 strings, you can do three operations:
    1. insert any character in s1
    2. remove any character from s1
    3. replace any character in s1, choose any character from s1 and replace it with any character

Given these 3 operations, find min. no. of operations to convert string s1 to s2.


s1 = "horse"
s2 = "ros"
    -> Convert s1 to s2 in min. no. of operations

Is it always possible?
    -> YES, delete all characters from s1 and insert s2
    -> maximum no. of steps = O(n + m)

Approach 2:
    replace h -> r ==> rorse
    remove r  -> rose
    remove e  -> ros
        -> In 3 steps, s1 converted to s2
        -> min. no. of operations = 3


s1 = "intention"
s2 = "execution"

remove t --> inention
replace i -> e ===> enention
replace n -> x ===> exention
replace n -> c ===> exection
insert u       ===> execution
    -> In 5 operations, s1 converted to s2


-> STRING MATCHING
==================
-> Insert of the same character if they are not matching(from s2)
-> Delete and try finding somewhere else
-> Replace and match

WE WILL NEED TO EXPLORE ALL POSSIBLE STUFFS --> RECURSION
-------------------------------------------

How to approach recursion
-------------------------
1. express in terms of indices -> f(i, j)
    -> f(i, j) 
        -> find me the min. operations to convert s1[0...i] to s2[0..j]
2. explore all paths of matching
    -> if they match
    -> if they doesn't match
3. Return minimum (of all paths)
4. base case

"""

def recursion(s, t):
    n, m = len(s), len(t)

    def f(i, j):
        # base case, when it's over
        # if string 1 gets exhausted or string 2 gets exhausted
        # f(-1, 1) 
        # if i < 0 (e.g. -1 and we don't have any characters in s1)
        # we will need to insert the characters to make it to s2
        # so no. of operations required to make it to s2
        # will be equal to the length of string2 from s2[0:j+1]
        if i < 0:
            return j+1

        # when s2 is exhausted
        # s2 < 0 (e.g. -1) and s1 >= 2
        # f(i, j) ==> f(2, -1) -> min. no. of operations to convert
        # s1 (which might be something) to an empty string
        # e.g. >>> "hor" ---> ""
        # we will need to delete all the characters present in s1
        # so no. of operations = (i+1)
        if j < 0:
            return i+1

        # explore possibilities
        if s[i] == t[j]:
            return 0 + f(i-1, j-1)
        else:
            # because we insert a character at the right end
            # 13-14 minute portion of video
            # so a character is inserted in s at the end
            # and i stays at the same place
            # and insert is one operation
            insert = 1 + f(i, j-1)

            # or else we can delete the i'th character
            # and see if (i-1)th character of s1 matches s2
            # i will reduce, j will stay
            delete = 1 + f(i-1, j)

            # replace the i'th character with the s2[j] th character
            # decrease indices for both the strings
            replace = 1 + f(i-1, j-1)
            return min(insert, delete, replace)
    return f(n-1, m-1)

def memoization(s, t):
    n, m = len(s), len(t)
    dp = [[-1 for i in range(m)] for j in range(n)]
    
    def f(i, j):
        if i < 0:
            return j+1
        if j < 0:
            return i+1
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i] == t[j]:
            dp[i][j] = f(i-1, j-1)
            return dp[i][j]
        else:
            insert = 1 + f(i, j-1)
            delete = 1 + f(i-1, j)
            replace = 1 + f(i-1, j-1)
            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
    return f(n-1, m-1)


def memoizationShiftIndex(s, t):
    n, m = len(s), len(t)
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]
    
    def f(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i-1] == t[j-1]:
            dp[i][j] = f(i-1, j-1)
            return dp[i][j]
        else:
            insert = 1 + f(i, j-1)
            delete = 1 + f(i-1, j)
            replace = 1 + f(i-1, j-1)
            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
    return f(n, m)

def tabulation(s, t):
    n, m = len(s), len(t)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    
    for j in range(m+1):
        dp[0][j] = j
    for i in range(n+1):
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                insert = 1 + dp[i][j-1]
                delete = 1 + dp[i-1][j]
                replace= 1 + dp[i-1][j-1]
                dp[i][j] = min(insert, delete, replace)
    return dp[n][m]

def spaceOptimization(s, t):
    n, m = len(s), len(t)
    prev = [0 for i in range(m+1)]
    cur = [0 for i in range(m+1)]
    for j in range(m+1):
        prev[j] = j

    for i in range(1, n+1):
        cur[0] = i
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                cur[j] = prev[j-1]
            else:
                insert = 1 + cur[j-1]
                delete = 1 + prev[j]
                replace= 1 + prev[j-1]
                cur[j] = min(insert, delete, replace)
        prev = cur[:]
    return prev[m]





s1 = "horse"
s2 = "ros"

print(recursion(s1, s2))
print(memoization(s1, s2))
print(memoizationShiftIndex(s1, s2))
print(tabulation(s1, s2))
print(spaceOptimization(s1, s2))
