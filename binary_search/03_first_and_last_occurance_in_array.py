"""
#################################################
PROBLEM 1: FIND THE FIRST AND LAST OCCURANCE OF X
#################################################

Given a sorted array

arr = [2, 4, 6, 8, 8, 8, 11, 13]
idx =  0  1  2  3  4  5   6   7


for x = 8, return [3, 5]
for x = 10, return [-1, -1]
for x = 11, return [6, 6]

lower bound -> arr[idx] >= x --> this will give us the first occurance
upper bound -> arr[idx] > x
            -> so [idx - 1] --> this will give us the last occurance

e.g. for 8 -> lower bound = first occurance = 3
           -> upper bound - 1 = last occurance = 6 - 1 = 5

**BUT** 
this will not cover all the edge cases
if the element x is not present in the array, this will not work

e.g. for x = 10
    * lower bound = 6, i.e. arr[6] = 11
    * so we need to check if arr[lower_bound] == x or not

e.g. for x = 14
    * lower bound = 8, i.e. length of the array, hypothetical index
    * if lower bound points to n or arr[lower bound] != x
        * return -1 and -1 for first and last occurance

    * so when these 2 edge cases are handled, the answer will be
        [lb, ub - 1]


"""

def brute_force_linear(arr, x):
    n = len(arr)
    first, last = -1, -1

    for i in range(n-1):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
    return first, last



def lower_bound(arr, n, x):
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


def upper_bound(arr, n, x):
    lo, hi = 0, n-1
    ans = n

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] > x:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


def binary_search_first_and_last_occurance(arr, n, k):
    lb = lower_bound(arr, n, k)
    if (lb == n) or (arr[lb] != k): return [-1, -1]
    
    return [lb, upper_bound(arr, n, k)-1]


arr = [2, 4, 6, 8, 8, 8, 11, 13]

print(binary_search_first_and_last_occurance(arr, len(arr), 8))
print(binary_search_first_and_last_occurance(arr, len(arr), 10))
print(binary_search_first_and_last_occurance(arr, len(arr), 11))





"""
Interviewer might ask to not use any lower bound or upper bound concept
So code up a normal simple binary search solution.


arr = [2, 8, 8, 8, 8, 8, 11, 13]
idx =  0, 1, 2, 3, 4, 5,  6,  7

x = 8


We can't find both the first and last occurance in single BS.
So we will handle them one by one

1. First occurance binary search

first = -1
* lo = 0, hi = 7, mid = (0+7)//2 = 3, arr[mid] = arr[3] = 8
    * arr[mid] = x
    * so update first = 3
    * but we are looking for first occurance
    * since we're looking for first occurance, look at the left now
    * reduce the right search space
    * hi = mid - 1 = 2

* lo = 0, hi = 2, mid = (0+2)//2 = 1, arr[mid] = arr[1] = 8
    * arr[mid] = x
    * so update first = 1
    * but again, we're looking for first occurance
    * so look at the left now
    * hi = mid - 1 = 0

* lo = 0, hi = 0, mid = (0+0)//2 = 0, arr[mid] = arr[0] = 2
    * since arr[mid] != x
    * so arr[mid] < 8, so we need to go to right search space
    * lo = mid + 1
    * this causes lo > hi and the while loop won't run anymore as we have
        * while lo <= hi:, so it will break


2. Last occurance binary search
last = -1

* lo = 0, hi = 7, mid = 3, arr[mid] = arr[3] = 8
    * arr[mid] = x
    * update last = mid= 3
    * we need last occurance, it will be on the right side
    * so eliminate the left search space
    * lo = mid + 1 = 4

* lo = 4, hi = 7, mid = (4+7)//2 = 5, arr[mid] = arr[5] = 8
    * arr[mid] = x
    * update last = mid = 5
    * as we need last occurance, it will be on the right side
    * so eliminate the left search space
    * lo = mid + 1 = 6

* lo = 6, hi = 7, mid = (6+7)//2 = 6, arr[mid] = arr[6] = 11
    * arr[mid] != x
    * we have arr[mid] > x, so we need to eliminate the right search space
    * hi = mid - 1 = 5
    * hi crosses lo, so we stop the while loop

* we now have our first and last occurance as 1 and 5

---------------------------------------------------------------------------

arr = [2, 8, 8, 8, 8, 8, 11, 13]
idx =  0, 1, 2, 3, 4, 5,  6,  7

x = 11

1. First occurance
first = -1
* lo = 0, hi = 7, mid = (0+7)//2 = 3,
    * arr[mid] < x
    * so we won't find solution on the left side
    * eliminate the left side
    * lo = mid + 1 = 4

* lo = 4, hi = 7, mid = (4+7)//2 = 5
    * arr[mid] < x
    * we won't find solution on left side
    * eliminate the left side of search space
    * lo = mid + 1 = 6

* lo = 6, hi = 7, mid = (6+7)//2 = 6
    * arr[mid] = x
        * update first = mid = 6
    * since we're looking for first solution, we need to check left
    * eliminate the right search space
    * hi = mid - 1 = 5
    * hi crosses lo, stop the search and we have our first occurance

first = 6

# Pseudo code for first occurance

def first_occurance(arr, n, x):
    lo, hi = 0, n-1
    first = -1

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] == x:
            # we are looking for first occurance
            # go to left, eliminate right search space
            first = mid
            hi = mid - 1
        elif arr[mid] < x:
            # we need to go right
            # eliminate the left search space, go to right
            lo = mid + 1
        else:
            # we need to go left
            # eliminate right search space, go to left
            hi = mid - 1
    return first



2. Last occurance

def last_occurance(arr, n, x):
    lo, hi = 0, n-1
    last = -1

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] == x:
            # we found the x, but we need last occurance
            # eliminate left search space, go to right
            last = mid
            lo = mid + 1
        elif arr[mid] < x:
            # we will only find element on the right
            # go to right
            lo = mid + 1
        else:
            # we will find element on the left
            # go to left, eliminate right search space
            hi = mid - 1
    return last

"""









