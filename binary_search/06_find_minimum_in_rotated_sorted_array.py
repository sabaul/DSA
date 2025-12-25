"""
####################################
FIND MINIMUM IN ROTATED SORTED ARRAY [ONLY UNIQUE ELEMENT PRESENT IN ARRAY]
####################################


arr = [4, 5, 6, 7, 0, 1, 2]
idx =  0, 1, 2  3  4  5  6


to find the minimum:
    * we need to eliminate either the left/right side
        * identify the sorted half
        * in the given case, lo = 0, hi = 6, mid = 3
            * the left half is sorted
            * the right half is not sorted
        * why is the right half not sorted?
            * Because the point of rotation lies in that portion
            * so it's not sorted
            * THE RORATING POINT WILL ALWAYS HAVE THE MINIMUM ELEMENT

        * So the sorted section won't have the minimum element
        * We will ALWAYS find the minimum element in the un-sorted portion


* Checking the condition of minimum present in the un-sorted portion

arr = [7, 8, 1, 2, 3, 4, 5, 6]
idx =  0  1  2  3  4  5  6  7

lo = 0, hi = 7, mid = (0+7)//2 = 3

* left half is not sorted
* right half is sorted
    * the minimum element is in the LEFT UN-SORTED PORTION  - left portion


example:
arr = [4, 5, 1, 2, 3]
idx =  0  1  2  3  4

lo = 0, hi = 4, mid = (0+4)//2 = 2

* left half is not sorted
* right half is sorted -> CONTAINS THE MINIMUM
    * CONFLICTS WITH OUR SOLUTION APPROACH


example:
arr = [1, 2]
idx =  0  1

lo = 0, hi = 1, mid = 0

* left half is sorted
    * and it contains the minimum element
    * CONFLICTS WITH OUR SOLUTION APPROACH

* THE SORTED PORTION MAY OR MAY NOT HAVE THE SOLUTION
* PICK THE MINIMUM FROM THE SORTED HALF AND ELIMINATE THE REST
    * BECAUSE THE LEFT-MOST ELEMENT OF THE SORTED ELEMENT IS THE MINIMUM


arr = [4, 5, 6, 7, 0, 1, 2]
idx =  0  1  2  3  4  5  6

ans = INT_MAX/FLOAT_MAX

lo = 0, hi = 6, mid = 3
* left portion is sorted
    * update answer to the minimum value: the element at index "lo"
        * ans = arr[lo]
    * now this sorted portion is of no use to us, as we've picked up the minimum element from this
    * so eliminate this left portion
    * now lo = mid + 1

* lo = 4, hi = 6, mid = (4+6)//2 = 5
* arr[lo] <= arr[mid]
    * left half is sorted
    * pick up the minimum element, the element at index "lo"
    * ans = min(arr[lo], ans)
    * eliminate this sorted portion now
    * lo = mid + 1 = 6

* lo = 6, hi = 6, mid = 6
* arr[lo] <= arr[mid]
    * left half is sorted
    * we need the minimum element from this 




Example:
arr = [7, 8, 1, 2, 3, 4, 5, 6]
idx =  0  1  2  3  4  5  6  7

ans = INT_MAX/float('inf')

* lo = 0, hi = 7, mid = (0+7)//2 = 3
    * arr[lo] is not <= arr[mid]
        * left half is not sorted
        * we need to eliminate the right portion, we need to eliminate this
        * since the right portion is sorted
        * pick up the minimum element, i.e. arr[mid]
        * ans = arr[mid] = 2
        * eliminate the sorted section
            * hi = mid - 1
            * hi = 2

* lo = 0, hi = 2, mid = 1
    * arr[lo] <= arr[mid]
        * this left half is sorted
        * update answer with the minimum value
            * ans = min(arr[lo], ans)
            * ans = 2 only
        * eliminate the left half
        * move lo 
        * lo = mid + 1
        * lo = 2

* lo = 2, hi = 2, mid = 2
    * arr[lo] <= arr[mid]
        * left half is sorted
        * pick up the minimum from this sorted and update ans
        * ans = min(ans, arr[lo])
            * ans = min(2, 1) = 1
            * ans = 1
        * eliminate the left half
        * lo = mid + 1 = 3
    
    * the while lo <= hi in binary search condition fails
    * so we return the answer as 1



* Example
arr = [4, 5, 1, 2, 3]
idx =  0  1  2  3  4

ans = INT_MAX/float('inf')


lo = 0, hi = 4, mid = 2
    * arr[lo] <= arr[mid]
    * left half is not sorted
    * pick up the smallest element of the right sorted portion
        * ans = min(ans, arr[mid])
        * ans = min(INT_MAX, arr[2]=1)
        * ans = 1
    * eliminate the right portion
    * hi = mid - 1
    * hi = 1

lo = 0, hi = 1, mid = 0
    * arr[lo] <= arr[mid]
    * left half is sorted
        * compare ans with the smallest element of this sorted array
        * ans = min(arr[lo], ans)
        * ans = 1
    * eliminate the left half
    * lo = mid + 1
    * lo = 1

lo = 1, hi = 1, mid = 1
    * arr[lo] <= arr[mid]
    * left half is sorted
        * compare ans
        * ans = min(ans, arr[lo])
        * ans = min(1, 5)
        * ans = 1
    * eliminate the left half
    * lo = mid + 1
    * lo = 2

now lo is not <= hi
    * break out of the while loop 
    * return answer


# PSEUDO CODE
def f(arr, n):
    lo, hi = 0, n-1
    ans = float('inf')

    while lo <= hi:
        mid = (lo+hi)//2

        # If the search space is already sorted
        # then we will have this condition: arr[lo] <= arr[mid] <= arr[hi]
        # or we can say that: arr[lo] <= arr[hi]
        # this means the entire array right now is sorted
        # so return the minimum value
        if arr[lo] <= arr[hi]:
            ans = min(ans, arr[lo])
            break or return ans

        # eliminate the left/right half
        if arr[lo] <= arr[mid]:
            # this means left half is sorted
            # update answer with the lowest possible element in the sorted section
            ans = min(ans, arr[lo])

            # eliminate the left half
            lo = mid + 1
        else:
            # now this means, right half is sorted
            # update answer with the smallest possible element in the sorted section
            ans = min(ans, arr[mid])

            # eliminate the right half
            hi = mid - 1

    return ans
"""
