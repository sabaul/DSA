"""
########################################
FIND PEAK ELEMENT

Definition of peak element, any element at index i: 
    arr[i-1] < arr[i] > arr[i+1]

* array can have multiple peaks
* take -inf on left and right of the array
########################################

e.g.:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1] -> ans = 8
    arr = [1, 2, 1, 3, 5, 6, 4] -> ans = 2 or 6, return any one
    arr = -inf [1, 2, 3, 4, 5] -inf -> ans = 5, as 4 < 5  and 5 > -inf
    arr = -inf [5, 4, 3, 2, 1] -inf -> ans = 5, as -inf < 5  and 5 > 4


########################################
BRUTE FORCE SOLUTION: LINEAR SEARCH -> O(n) time
########################################
"""
def brute_force(arr):
    n = len(arr)
    for i in range(n):
        if (i == 0 or arr[i-1] < arr[i]) and (i == n-1 or arr[i] > arr[i+1]):
            return arr[i]


"""
######################################
OPTIMIZED - BINARY SEARCH OPTIMIZATION
######################################

arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
idx =  0  1  2  3  4  5  6  7  8  9

* assume array has only 1 peak


* if array has one element: arr = [2], return 0 (as array has -inf on left and right)
* if array has more than one element

3 things can happen:
    for a given mid, peak can lie on the right
    for a given mid, peak can lie on the left
    for a given mid, peak can lie on the same index



lo = 0, hi = 9, mid = (0+9)//2 = 4
    * arr[mid] = 5
    * is this a peak element: it's greater than 4 (left) but not greater than 6 (right)
    * check if peak lies on left or right
    * since 5 is greater than the element on the left
        * it's in the linearly increasing portion of the array
        * if mid is on the increasing curve, peak lies on the right
        * we will never have peak on the left, so eliminate the left portion
        * update lo = mid + 1

lo = 5, hi = 9, mid = (5+9)//2 = 7
    * arr[mid] = 8
    * is this a peak element: YES
    * return mid or arr[mid]

-------------------------------------------------------------------------------
another example:

arr = [1, 10, 13, 7, 6, 5, 4, 2, 1, 0]
idx =  0   1   2  3  4  5  6  7  8  9


lo = 0, hi = 9, mid = (0+9)//2 = 4
    * arr[mid] = 6
    * is this a peak: smaller than left element, greater than right element
    * NOT A PEAK
    * this is on the decreasing portion of the array
        * peak will be on left
        * eliminate the right half
        * update hi = mid - 1


lo = 0, hi = 3, mid = (0+3)//2 = 1
    * arr[mid] = 10
    * is this the peak: greater than left element, smaller than right element
    * NOT A PEAK
    * this mid lies on increasing portion of the array
        * peak will be on the right
        * eliminate the left half
        * update lo = mid + 1

lo = 2, hi = 3, mid = (2+3)//2 = 2
    * arr[mid] = 13
    * is this the peak: YES
    * return the index mid or the value arr[mid]



-------------------------------------------------------------------------------
another example, peak at index 0 or the last index:

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx =  0  1  2  3  4  5  6  7  8  9


* since we always need to check:
    arr[mid - 1] < arr[mid] > arr[mid + 1]

    * so mid should not be index 0 and index (n-1)
    * as this will throw runtime error -> out of bounds error

* before starting the WHILE loop:
    * check if zero-th element can be a peak
        * on left we have -inf, so we just need to compare it with the element at index 1
    * check if n-th element can be a peak
        * on right we have -inf, so we just need to compare it with the element at index (n-2)

* CHECK ABOVE CONDITION:
    * is arr[0] > arr[1] -> NO, SO NOT PEAK
        * 1 > 2 --> NO, NOT PEAK
    * is arr[n-1] > arr[n-2] -> YES, THIS IS THE PEAK ELEMENT
        * 10 > 9
            * return 10
        * NO NEED TO PERFORM BINARY SEARCH


* SO ALWAYS CHECK FOR THE FIRST AND THE LAST ELEMENT WHILE CODING IT UP
* BINARY SEARCH WILL START FROM LO = 1 AND HI = N-2
    * ignoring the first and the last element from the search
    * as we already wrote the conditions for these 2 situation
"""

def f(arr, n):
    # Separate peak conditions
    if n == 1: return 0
    if arr[0] > arr[1]: return 0
    if arr[n-1] > arr[n-2]: return n-1

    lo = 1
    hi = n-2

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            # mid lies on increasing curve, greater than left element
            # peak lies on right
            # eliminate left half
            lo = mid + 1
        else:
            # mid lies on decreasing curve, greater than right element
            # peak lies on left
            # eliminate right half
            hi = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f(arr, len(arr)))
