"""
#############################
FIND THE Nth root of a given integer M, if you don't get something, return -1
#############################

* N = 3, M = 27, 3rd root of 27 = 3
* N = 4, M = 69, 4TH ROOT OF 69 DOESN'T EXIST, SO RETURN -1


# linear search approach
for 27:
    1x1x1 = 1
    2x2x2 = 8
    3x3x3 = 27 -> got my answer, done, return 3

for 69, 4th root:
    1x1x1x1 = 1
    2x2x2x2 = 16
    3x3x3x3 = 81 -> exceeded 69, we can't find a solution now, return -1

# linear search solution:

* time complexity: m * log(n)
    * we have a for loop m times, and each time we do the log(n) operation for exponential operations

def nthroot(n, m):
    for i in range(m):
        if f(i, n) == m:
            return i
        elif f(i, n) > m:
            return -1


#################################
# BINARY SEARCH ON ANSWERS
#################################
we were asked to find, the 4th root of 69
    * we did this: 1x1x1x1 = 1
        * this is not possible
        * why did we go to next number?
        * why did we not stop?
            * because the value that we got was less than 69
            * so maybe we can slightly increase the number
            * and if I increase the number, I might end up at the target
        * so we increased the number to 2
    * now -> 2 ^ 4 = 16 < 69
    * again -> 3 ^ 4 = 81 > 69
        * now we can't go more than 3, as 3 ^ 4 = 81 >> 69
        * this is not possible, anything beyond this will also not be possible

* so we have a pattern for when to move left and when to move right
* we can use this pattern to solve this by binary search


example for n = 27, let's apply binary search

n = 3, m = 27

lo = 1, hi = 27, mid = (1 + 27)//2 = 14
    * mid ^ n = 14 ^ 3 > 27
    * since mid ^ n > m, anything greater than 14 will never be the answer
    * reduce the search space, eliminate the right side
    * update hi
    * hi = mid - 1

lo = 1, hi = 13, mid = (1 + 13)//2 = 7
    * mid ^ n = 7 ^ 3 > 27
    * again mid ^ n > m, anything on right will also not be a answer
    * eliminate the right search space
    * hi = mid - 1

lo = 1, hi = 6, mid = (1+6)//2 = 3
    * mid ^ n = 3 ^ 3 = 27
    * we found our answer, return 3





another example: N = 4, M = 69

range = 1 to 69
lo = 1, hi = 69, mid = (1+69)//2 = 35
    * 35 ^ 4 > 69
    * eliminate right side, as everything on right will also be > 69
    * hi = mid - 1

lo = 1, hi = 34, mid = (1+34)//2 = 17
    * 17 ^ 4 > 69
    * same as above, eliminate right side
    * hi = mid - 1

lo = 1, hi = 16, mid = (1+16)//2 = 8
    * 8 ^ 4 > 69
    * same as above, eliminate right side
    * hi = mid - 1

lo = 1, hi = 7, mid = (1+7)//2 = 4
    * 4 ^ 4 > 69
    * eliminate right side
    * hi = mid - 1

lo = 1, hi = 3, mid = (1+3)//2 = 2
    * 2 ^ 4 < 69
    * since this is smaller, anything on left and including this one
    * these won't be the solution
    * lo = mid + 1


lo = 3, hi = 3, mid = (3+3)//2 = 3
    * 3 ^ 4 > 69
    * eliminate right side
    * hi = mid - 1 = 2
    * hi crosses left side, the while loop will close
    * return -1
"""


def f_basic(n, m):
    lo = 1
    hi = m

    while lo <= hi:
        mid = (lo+hi)//2

        current_val = mid ** n
        # this might give us over the int limit

        # so use the custom function below, full function is called f_upgraded
        #func(mid, n, m)

        if current_val == m:
            return mid
        elif current_val > m:
            # eliminate the right search space
            hi = mid - 1
        else:
            # eliminate the left search space
            lo = mid + 1
    return -1


def func(mid, n, m):
    """
    return 1 if == m
    return 0 if < m
    return 2 if > m
    """
    ans = 1
    for i in range(n):
        ans = ans * mid
        if ans > m:
            return 2

    if ans == m:
        return 1
    return 0

def f_upgraded(n, m):
    lo = 1
    hi = m

    while lo <= hi:
        mid = (lo+hi)//2

        midN = func(mid, n, m)

        if midN == 1:
            return mid
        elif midN == 0:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print(f_basic(3, 27))
print(f_basic(4, 69))


print(f_basic(100, 2000))
print(f_upgraded(100, 2000))


