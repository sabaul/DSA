"""
PROBLEM: SEARCH IN ROTATED SORTED ARRAY 2 
         [ BUT THIS TIME THE ARRAY MIGHT HAVE DUPLICATES ]


arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], target = 3

In the previous problem, without duplicate approach will not work.

Here, we do not need to return the index as there can be duplicates.
Here, we need to only tell if the target exists or not.


Why previous solution doesn' work.
What were we doing previously:
    1. identifing the sorted half (left or right sorted)
        * because if we do not know which part is sorted, how can we eliminate
        * how can we check in that part

Example: arr = [6, 7, 1, 2, 3, 4, 4, 5]
         idx =  0, 1, 2, 3, 4, 5, 6, 7

    * lo = 0, hi = 7, mid = (0+7)//2 = 3
        * we can say that the right section -> the array [2, 3, 4, 4, 5]
            * is sorted, as arr[mid] <= arr[hi]
                * also arr[lo] is not <= arr[mid]

Another example: arr = [4, 5, 1, 2, 3, 3, 4, 4]
                 idx =  0, 1, 2, 3, 4, 5, 6, 7

    * lo = 0, hi = 7, mid = (0+7)//2 = 3
        * again left portion is not sorted
            * as arr[lo] is not <= arr[mid]
        * right portion is sorted
            * as arr[mid] <= arr[hi]


Another example: arr = [3, 1, 2, 3, 3, 3, 3]
                 idx =  0, 1, 2, 3, 4, 5, 6

    * lo = 0, hi = 6, mid = (0+6)//2 = 3
        * here both the portion will be sorted
            * as arr[lo] <= arr[mid]
            * and arr[mid] <= arr[hi]
                * as all the lo, mid, hi indices point to the number 3
############################################################
                * so arr[lo] == arr[mid] == arr[hi]
############################################################

            * IT'S NOT POSSIBLE THAT BOTH THE SECTION ARE NOT SORTED
                * AS WE CAN SEE LEFT HALF IS NOT SORTED
                * WHEREAS RIGHT PORTION IS SORTED

    * SO WE CAN'T DECIDE WHICH SIDE IS SORTED JUST BY USING THE 3 ELEMENTS
    * THE lo, mid, hi


############################################################
* SO WE NEED TO TRIM DOWN THESE CONDITIONS
* The problem is:
    arr[lo] == arr[mid] == arr[hi]
* So we need to handle this condition somehow
# And reduce our search space
############################################################

if arr[lo] == arr[mid] == arr[hi]:
    # check if it's equal to the target [since all of them are the same]
    if arr[mid] == target:
        return mid
    else:
        # move lo to lo + 1
        # move hi to hi - 1
        # as all of them are equal, keeping mid same, we can move lo and hi
        # as all of them are equal and not equal to the target
        lo += 1
        hi -= 1
        # doing this will reduce our search space



def f(arr, n, target):
    lo, hi = 0, n-1

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] == target:
            return mid

        # HANDLE THE CONDITION WHERE
        # arr[lo] == arr[mid] == arr[hi]
        if arr[lo] == arr[mid] and arr[mid] == arr[hi]:
            # Reduce the search space from left and right
            lo += 1
            hi -= 1
            continue


        # Left sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target and target <= arr[mid]:
                # Element lies in the left section
                # eliminate the right side
                hi = mid - 1
            else:
                # Element lies in the right section
                # eliminate the left side
                lo = mid + 1

        # Right sorted
        else:
            if arr[mid] <= target and target <= arr[hi]:
                # Element lies in the right section
                # eliminate the left section
                lo = mid + 1
            else:
                # Element lies in the left section
                # eliminate the right section
                hi = mid - 1

    # If nothing found
    return -1

"""
