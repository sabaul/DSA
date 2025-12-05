"""
######################################################
LOWER BOUND: smallest index such that arr[idx] >= x
######################################################

* Given a sorted array, smallest index such that the number at that index is greater than or equal to the given number.

Example:
    * Given a sorted array "arr" 
    arr = [3, 5, 8, 15, 19], n = 5

    * for x = 8
        * lower bound = 2, as arr[2] = 8 is >= x, which is 8
    * for x = 9
        * lower bound = 3, as arr[3] = 15 is >= x, which is 9
    * for x = 19
        * lower bound = 4, as arr[4] = 19 is >= x, which is 19
    * for x = 20
        * lower bound = 5, i.e. the SIZE OF THE ARRAY
        * Because there is no one >= 20, so it will be the last hypothetical scenario [ which is the size of the array ]

Example 2:
    * Given a sorted array 
    arr = [3, 5, 8, 15, 19, 19, 19], n = 7

    * for x = 19
        * lower bound = 4, as arr[4] = 19 (the first 19) >= x


Example 3:
    * Given a sorted array
    arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11], n = 10
    idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    * for x = 11
        * FIRST APPROACH -> linear search for loop
        * Big O(n) time complexity
        --------------------------------
        * BINARY SEARCH, AS THE INPUT ARRAY IS SORTED

    * for x = 1
        * ans = 10, always equal to array, the hypothetical answer even if there doesn't exist any number greater than or equal to x
            * we will return this if we don't find anything
        * lo = 0, hi = 9, mid = (0+9)//2 = 4, so arr[mid] = 7
            * arr[mid] >= 1, so update ans = mid = 4
            * since now we need the smallest number, eliminate the right search space
            * hi = mid - 1
        * lo = 0, hi = 3, mid = (0+3)//2 = 1, so arr[mid] = 2
            * arr[mid] = 2 >= 1, so update ans = mid = 1
            * we still need smallest number such that it's >= 1, so eliminate the right search space
            * hi = mid - 1
        * lo = 0, hi = 0, mid = (0+0)//2 = 0, so arr[mid] = 1
            * arr[mid] = 1 >= 1, so update ans = mid = 0
            * look for smallest
            * hi = mid - 1
                * but hi is now -1
                * lo <= hi is not satisfied, so return the answer ans = 0


arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11], n = 10

    * for x = 9
        * ans = 10, the hypothetical answer [ default value ]
        * lo = 0, hi = 9, mid = (0+9)//2 = 4, so arr[mid] = 7
            * arr[mid] is not >= 9
            * so we need to go right, eliminate left search space
            * lo = mid + 1
        * lo = 5, hi = 9, mid = (5+9)//2 = 7, so arr[mid] = 9
            * arr[mid] >= 9, udpate ans = mid = 7
            * but we need smallest, emilinate right search space
            * hi = mid - 1 = 6
        * lo = 5, hi = 6, mid = (5+6)//2 = 5, so arr[mid] = 8
            * arr[mid] is not >= 9
            * we need to go right, eliminate left search space
            * lo = mid + 1 = 6
        * lo = 6, hi = 6, mid = (6+6)//2 = 6, so arr[mid] = 8
            * arr[mid] = arr[6] = 8
                * but arr[mid] is not >= 9
                * if we update lo or hi, we will get out of the while loop

    * so finally, my answer = 7, return 7



# LOWER BOUND CODE IMPLEMENTATION

def f(arr, target, n):
    lo, hi = 0, n-1
    ans = n

    while lo <= hi:
        mid = (lo + hi)//2

        if arr[mid] >= target:
            # this may be an answer, update the answer
            # reduce right search space, eliminate things from right side
            ans = mid
            hi = mid - 1
        else:
            # this mid can't be an answer
            # reduce left search space, eliminate things from left side
            lo = mid + 1

    return ans
"""

def lower_bound(arr, n, x):
    lo, hi = 0, n-1
    ans = n

    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] >= x:
            # may be an answer
            # look for more small index on the left
            ans = mid
            hi = mid - 1
        else:
            # cannot be answer
            # move left point, to the right of mid
            lo = mid + 1
    return ans






"""
######################################################
UPPER BOUND: smallest index such that arr[idx] > x
######################################################

Example 1:
    arr = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12], n = 9
    idx =  0, 1, 2, 3, 4, 5,  6,  7,  8,  9

    for x = 6, upper bound = 3, as arr[3] > x, i.e. 7 > 6
    for x = 11, upper bound = 9, as arr[9] > x, i.e. 12 > 11
    for x = 12, upper bound = 10, HYPOTHETICAL SCENARIO N -> length of array
    for x = 13, upper bound = 10, HYPOTHETICAL SCENARIO N -> length of array
    for x = 0, upper bound = 0, as arr[0] = 2 > 0


* It is similar to lower bound, just remove the = sign from the >= sign

* this is what we had for lower bound:
def lb():
    if arr[mid] >= x:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

* this is what we will need for upper bound:
def ub():
    if arr[mid] > x:
        ans = mid
        mid = hi - 1
    else:
        lo = mid + 1
"""

def upper_bound(arr, x, n):
    lo, hi = 0, n-1
    ans = n
    while lo <= hi:
        if arr[mid] > x:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans






"""
#############################################################
SEARCH INSERT POSITION

Given a sorted array "arr" of distinct values and a target value "m".
Search for the index of the target value in the array.

If the value is present in the array, then return the index.
If the value is not present, determine the index where it would be inserted in
the array while maintaining the sorted order.
#############################################################

Example:
    arr = [1, 2, 4, 7], x = 6, to be inserted in the array
           0  1  2  3

    * 6 will be inserted after 4, i.e. at index 3

    * for x = 2, we will insert 2 at index 1, and then the rest of the array can follow
        * resulting array = [1, 2, 2, 4, 7]

    * this is similar to finding the lower bound
        * smallest index such that arr[index] >= x

    * So this is basically the code for lower bound
"""

def search_insert_position(arr, x):
    n = len(arr)
    lo, hi = 0, n-1
    ans = n

    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] >= x:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans






"""
#############################################################
FLOOR AND CEIL IN SORTED ARRAY

FLOOR - largest number in array <= x
CEIL - smallest number in array >= x
#############################################################

Example:
    arr = [10, 20, 30, 40, 50], x = 25
    for x = 25
        * floor = 20 as floor <= x and 20 <= 25 [ largest number >= x]
        * ceil = 30 as ceil >= x and 30 >= 25 [ smallest number <= x ]


    arr = [10, 20, 25, 30, 40]
    for x = 25
        * floor = 25, as largest number <= 25 --> 25
        * ceil = 25, as smallest number >= 25 --> 25


* How to solve this
    * CEIL: smallest number in array >= x
        * this is LOWER BOUND

    * FLOOR:  just normal bs application


def floor(arr, x):
    ans = -1
    n = len(arr)
    lo, hi = 0, n-1

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] <= x:
            # this might be the largest number <= x
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    if ans != -1:
        return arr[ans]
    return ans


"""






