"""
########################
BINARY SEARCH ON ANSWERS 1: 

    FIND THE SQRT OF AN INTEGER
        * return the floor value if not a perfect square
        * e.g. for n = 30, sqrt = 5.something = 5
########################

* n = 25, sqrt(25) = 5
* n = 30, sqrt(30) = 5.something = 5
* n = 35, sqrt(35) = 5.something = 5
* n = 36, sqrt(36) = 6

#####################
LINEAR SEARCH WAY:
#####################
1 -> 1x1 = 1
2 -> 2x2 = 4
3 -> 3x3 = 9
4 -> 4x4 = 16
5 -> 5x5 = 25

for n = 28
    1
    2
    3
    4
    5 -> 25
    6 -> 36 > 28, so we can return 5

def linear_search(n):
    ans = -1
    for i in range(n):
        if i*i <= n:
            ans = i
        else:
            break
    return ans

#####################
# BINARY SEARCH SOLUTION
#####################

for n = 28
 1 can be a solution
 2 can be a solution
 3 can be a solution
 4 can be a solution
 5 can be a solution
 6 can't be a solution
 7 can't be a solution
 8 can't be a solution
 9 can't be a solution

since 6 will not be an answer
so anything greater than 6 will never be an answer

and since from 1 to 5 are my possible answers
WE ALWAYS TAKE THE MAXIMUM 5

NOTE: till a certain point, the answers are possible, after that point, the answer can't be found
    * THIS IS A CUE FOR USING BINARY SEARCH


* n = 28
lo = 1 and hi = 28 [nothing bigger than 28 can be our answer]
    * mid = (1+28)//2 = 14.5 = 14
    * 14*14 > 28
    * if 14 is not my answer, anything greater than this won't be the answer 
    * eliminate the right search space
    * hi = mid - 1

lo = 1, hi = 13, mid = (1+13)//2 = 7
    * 7*7 > 28
    * if 7 is not my answer, anything greater also won't be answer
    * eliminate right search space
    * hi = mid - 1


lo = 1, hi = 6, mid = (1+6)//2 = 3
    * 6*6 > 28
    * eliminate right search space
    * hi = mid - 1

lo = 1, hi = 5, mid = (1+5)//2 = 3
    * 3*3 is not greater than 28
    * this might be our answer, but we need to search for maximum
        * update answer = 3
        * going left won't make sense, move right as anything on the left won't be the answer, so we can go right
    * lo = mid + 1


lo = 4, hi = 6, mid = (4+6)//2 = 5
    * 5*5 < 28
    * update answer = 5
        * nothing on left will be the answer now
    * update answer, move right
    * lo = mid + 1

lo = 6, hi = 6, mid = 6
    * 6*6 > 28
    * eliminate right search space
    * hi = mid - 1

    * we have crossed the left, stop the while loop, we return ans

"""

def f(n):
    lo = 1
    hi = n
    ans = 1

    while lo <= hi:
        mid = (lo+hi)//2

        if mid*mid <= n:
            # update answer
            # move right, as anything on left now won't be the answer
            # update lo = mid + 1
            ans = mid
            lo = mid + 1
        else:
            # if it's greater, then anything on right won't be answer
            # eliminate the right search space, look for smaller values
            hi = mid - 1
    return ans

