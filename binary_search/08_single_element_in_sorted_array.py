"""
##################################
SINGLE ELEMENT IN SORTED ARRAY
##################################
* Given array of integers, all but one will be appearing twice
* only one number will appear once, find that number that appears once

* Guaranteed that the number appearing once will be ONE only
* All other numbers will appear twice and will be together
    * as the input array is SORTED
##################################

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]


##################################
* Brute force solution
##################################
    * linear search
    * for element at index i, (i-1) or (i+1) will be the same element
    * Time complexity: O(n)

def brute_force(arr):
    n = len(arr)

    # For array of size 1
    if n == 1:
        return arr[0]

    for i in range(n):
        if i == 0:
            # first element
            if arr[i] != arr[i+1]:
                return arr[i]
        elif i == n-1:
            # last element
            if arr[i] != arr[i-1]:
                return arr[i]
        else:
            if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
                return arr[i]


##################################
* Binary Search Solution
##################################

* we are looking for a single element in sorted array
* whenever sorted array -> we can think of binary search
* in order to use binary search
    * we need to think of elimination
    * at each iteration, we trim the search space in half
    * we have to find the property of the single element that helps us eliminate the search space


arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
idx =  0  1  2  3  4  5  6  7  8  9  10


single element at index 6 --> 4

we have pairs of elements and their indices are like this:
    1, 1 -> even, odd
    2, 2 -> even, odd
    3, 3 -> even, odd

    5, 5 -> odd, even
    6, 6 -> odd, even

* if we are standing at the even index, and at the right if at the right
    * we have the same element
    * then we are on the left half of the array

* if we are standing at the odd index, and at the right if at the right
    * we have the same element
    * then we are on the right half of the array

* SUMMARIZATION OF ABOVE INTUITION:
    * (even, odd) -> we are in left half -> element in the right half -> eliminate left half
    * (odd, even) -> we are in right half -> element in the left half -> eliminate right half


arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
idx =  0  1  2  3  4  5  6  7  8  9  10

* lo = 1, hi = 9, mid = (1+9)//2 = 5
    * arr[mid] = 3
    * is this the single element: the left and right should not be equal to 3
        * the element at left is the same element
        * it's not the search element
    * so we have to eliminate the left half or the right half, where the single element is not present
    * we are standing at an odd index, the previous index has the same number itself
        * so the single element is in right half
        * so we eliminate the left half
        * update lo = mid + 1

* lo = 6, hi = 9, mid = (6+9)//2 = 7
    * arr[7] = 5
    * is this the single element: the left and right element should not be equal to 5
        * the element at right is the same
        * this is not the single element
    * now, to eliminate the left or the right half
    * we are at odd index, the next element on the right has the same element
        * the single element lies in the left half
        * so we eliminate the right half
        * update hi = mid - 1

* lo = 6, hi = 6, mid = (6+6)//2 = 6
    * arr[6] = 4
    * is this the single element: the left and right element should not be equal to 4
        * and they are not equal to 4
        * this is the single element
        * return it


"""

# * SUMMARIZATION OF ABOVE INTUITION:
#     * (even, odd) -> we are in left half -> single element in the right half -> eliminate left half
#     * (odd, even) -> we are in right half -> single element in the left half -> eliminate right half

def f(arr, n):
    if n == 1:
        return arr[0]

    # TO AVOID WRITING A LOT OF EDGE CASES IF WE TAKE LO = 0 AND HI = n-1
    # WE REDUCE SEARCH SPACE TO LO = 1 AND HI = n-2
    # THIS WILL HELP US AVOID A LOT OF EDGE CASES

    if arr[0] != arr[1]: return arr[0]
    if arr[n-1] != arr[n-2]: return arr[n-1]

    lo = 1
    hi = n-2

    while lo <= hi:
        mid = (lo+hi)//2

        # is this the single element
        if arr[mid-1] != arr[mid] and arr[mid+1] != arr[mid]:
            return arr[mid]

        # if not we need to check which part we need to eliminate
        if mid % 2:
            # if mid is odd
            if arr[mid-1] == arr[mid]:
                # is the left element same
                # then single element in the right half, eliminate left half
                lo = mid + 1
            elif arr[mid] == arr[mid+1]:
                # is the right element same
                # then single element in the lfet half, eliminate right half
                hi = mid - 1
        else:
            # if mid is even
            if arr[mid-1] == arr[mid]:
                # is the left element same
                # then single element is in left half, eliminate right half
                hi = mid - 1
            elif arr[mid] == arr[mid+1]:
                # is the right element same
                # then single element is in right half, eliminate left half
                lo = mid + 1
    return -1


def f_striver_self(arr, n):
    if n == 1:
        return arr[0]

    # TO AVOID WRITING A LOT OF EDGE CASES IF WE TAKE LO = 0 AND HI = n-1
    # WE REDUCE SEARCH SPACE TO LO = 1 AND HI = n-2
    # THIS WILL HELP US AVOID A LOT OF EDGE CASES

    # * SUMMARIZATION OF INTUITION:
    #     * (even, odd) -> we are in left half -> single element in the right half -> eliminate left half
    #     * (odd, even) -> we are in right half -> single element in the left half -> eliminate right half

    if arr[0] != arr[1]: return arr[0]
    if arr[n-1] != arr[n-2]: return arr[n-1]

    lo = 1
    hi = n-2

    while lo <= hi:
        mid = (lo+hi)//2

        # is this the single element
        if arr[mid-1] != arr[mid] and arr[mid+1] != arr[mid]:
            return arr[mid]

        # if not we need to check which part we need to eliminate
        if (mid % 2 == 1 and arr[mid-1] == arr[mid]) or (mid % 2 == 0 and arr[mid+1] == arr[mid]):
            # eliminate the left half
            lo = mid + 1
        elif (mid % 2 == 1 and arr[mid+1] == arr[mid]) or (mid % 2 == 0 and arr[mid-1] == arr[mid]):
            # eliminate the right half
            hi = mid - 1
    return -1


def f_striver_full(arr, n):
    if n == 1:
        return arr[0]

    # TO AVOID WRITING A LOT OF EDGE CASES IF WE TAKE LO = 0 AND HI = n-1
    # WE REDUCE SEARCH SPACE TO LO = 1 AND HI = n-2
    # THIS WILL HELP US AVOID A LOT OF EDGE CASES

    # * SUMMARIZATION OF INTUITION:
    #     * (even, odd) -> we are in left half -> single element in the right half -> eliminate left half
    #     * (odd, even) -> we are in right half -> single element in the left half -> eliminate right half

    if arr[0] != arr[1]: return arr[0]
    if arr[n-1] != arr[n-2]: return arr[n-1]

    lo = 1
    hi = n-2

    while lo <= hi:
        mid = (lo+hi)//2

        # is this the single element
        if arr[mid-1] != arr[mid] and arr[mid+1] != arr[mid]:
            return arr[mid]

        # if not we need to check which part we need to eliminate
        if (mid % 2 == 1 and arr[mid-1] == arr[mid]) or (mid % 2 == 0 and arr[mid+1] == arr[mid]):
            # eliminate the left half
            lo = mid + 1
        else:
            # eliminate the right half
            hi = mid - 1
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
n = len(arr)
print(f(arr, n))
print(f_striver_self(arr, n))
print(f_striver_full(arr, n))
