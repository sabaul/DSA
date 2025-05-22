"""
WILDCARD MATCHING
=================
Given 2 strings which could consist of "?" and "*" characters, where
    -> ? --> matches with a single character
    -> * --> matches with a sequence of length zero or more
Return True if s1 matches with s2 else False


s1 = "?ay"
s2 = "ray"

-> s1 matches with s2
-> because ? and r (both first character of s1 and s2 are same)
-> return True as the final answer

s1 = "ab*cd"
s2 = "abdefcd"

-> * matches with "def"
-> s1 and s2 are same (* matches)
-> return True

s1 = "**abcd"
s2 = "abcd"

-> return True
-> as * could be None too.
-> * matches with length zero (both * characters)

s1 = "ab?d"
s2 = "abcc"

-> return False
-> as (? = c), but (d != c)
-> so s1 and s2 doesn't match

----------------
Let's understand the * character
----------------

s1 = "ab*cd"
s2 = "abdefcd"

-> starting from right end
-> d == d, and c == c

-> * could match with:
    -> "" (empty string), f, e, d, b, a, ef, def, bdef, abdef, ......many more
    -> without trying we can't tell what it will match with
    -> so we need to check all possible ways
        -> RECURSION
            -> STRING MATCHING RECURSION


RULES TO WRITE RECURSION
------------------------
1. express problem in terms of indices
    -> f(i, j)
    -> What does this f(i, j) means:
        e.g. f(n-1, m-1)
        -> when s = "ab*cd" and t = "abdefed"
        -> n = 5, m = 7 (n-1 = 4 and m-1 = 6)
        -> f(4, 6)
            -> in string t[0:6], and string s[0:4]
            -> are they matching?
        -> it will return True/False

2. explore comparisons

3. out of all comparisons, 
   if anyone can match, return True else return False


----------------------------

In string matching problems, we have 2 options:
1. String match
2. String doesn't match

-> For string matching, we have 2 option:
    -> both the characters match, move indices on both the strings
    -> if s[i] == t[j] or s[i] == '?'
        return f(i-1, j-1)

-> * --> means nothing or anything that it could match too

"""

def recursion(s, t):
    n, m = len(s), len(t)

    def f(i, j):
        # base case
        # return True or False
        # True -> if comparisons have been done
        
        # if s gets exhausted
        # i < 0, s has no more characters to match
        # in order to match with t, t should also not have anything to match
        # basecally both s and t should be exhausted at once, then return True
        if i < 0 and j < 0:
            return True

        # it means that s is exhausted, but t has some characters left
        # but s can't match to t, as it doesn't have any more characters left
        # s doesn't have any characters to match to t (which has some characters left)
        if i < 0 and j >= 0:
            return False

        # if t gets exhausted
        # j < 0 --> but s has some characters left
        # when can s (not an empty string) match with an empty string???
        # only if s has all * characters (one or more)
        # as * are the only characters which can match an empty string (or empty character)
        if j < 0 and i >= 0:
            for idx in range(i+1):
                if s[idx] != '*':
                    return False
            return True

        # explore all possibilities
        if s[i] == t[j] or s[i] == '?':
            return f(i-1, j-1)
        
        if s[i] == '*':
            # star means nothing (empty string),
            # or star means the last character of t, and so on recursively
            # put it in recursion steps
            # star means string of length 1, 2, ..... n
            
            # dont_take_star_as_last_char_of_t = f(i-1, j)
            # take_star_as_last_char_of_t = f(i, j-1)
            # return (dont_take_star_as_last_char_of_t
            #        or take_star_as_last_char_of_t)
            return f(i-1, j) or f(i, j-1)
        return False
    return f(n-1, m-1)


def memoization(s, t):
    n, m = len(s), len(t)
    dp = [[-1 for i in range(m)] for j in range(n)]
    
    def f(i, j):
        if i < 0 and j < 0:
            return True
        if i < 0 and j >= 0:
            return False
        if j < 0 and i >= 0:
            for idx in range(i+1):
                if s[idx] != '*':
                    return False
            return True
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i] == t[j] or s[i] != '?':
            dp[i][j] = f(i-1, j-1)
            return dp[i][j]
        
        if s[i] == '*':
            dp[i][j] = f(i-1, j) or f(i, j-1)
            return dp[i][j]

        dp[i][j] = False
        return dp[i][j]
    
    return f(n-1, m-1)

def memoizationOneBased(s, t):
    n, m = len(s), len(t)
    dp = [[False for i in range(m+1)] for j in range(n+1)]
    
    def f(i, j):
        if i == 0 and j == 0:
            return True
        if i == 0 and j > 0:
            return False
        if j == 0 and i > 0:
            for idx in range(1, i+1):
                if s[idx-1] != '*':
                    return False
            return True
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i-1] == t[j-1] or s[i-1] != '?':
            dp[i][j] = f(i-1, j-1)
            return dp[i][j]
        
        if s[i-1] == '*':
            dp[i][j] = f(i-1, j) or f(i, j-1)
            return dp[i][j]

        dp[i][j] = False
        return dp[i][j]
    
    return f(n, m)

def tabulation(s, t):
    n, m = len(s), len(t)
    dp = [[False for i in range(m+1)] for j in range(n+1)]
    dp[0][0] = True
    for j in range(1, m+1):
        dp[0][j] = False

    for i in range(1, n+1):
        flag = True
        for ii in range(1, i+1):
            if s[ii-1] != '*':
                #dp[i][0] = False
                flag = False
                break
        dp[i][0] = flag

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1] or s[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif s[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = False
    return dp[n][m]
                

    

s1 = ["?ay", "ab*cd", "**abcd", "ab?d"]
s2 = ["ray", "abdefcd", "abcd", "abcc"]

for s, t in zip(s1, s2):
    print(f"s: {s} || t: {t},\n{recursion(s, t)}, {memoization(s, t)}, {memoizationOneBased(s, t)}, {tabulation(s, t)}")
    print('='*30)
