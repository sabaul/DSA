"""
#############################################
BS 4 - SEARCH ELEMENT IN ROTATED SORTED ARRAY [ ONLY CONTAINS UNIQUE ELEMENTS]
#############################################

Rotated sorted array definition:
    Given a sorted array: arr = [1, 2, 3, 4, 5]
    * Can you rotate it at 4-5
    * The rotated sorted array will look like this:
        rotated array: arr = [4, 5, 1, 2, 3]

Example:
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    target = 1


Solution approach 1: Linear search
    * time complexity: O(n)


But we need to "SEARCH" in "SORTED" [ even though it's rotated array ]
USE BINARY SEARCH


Since the middle can not distribute left and right halfs always into sorted, because if the target was 8
mid = (lo+hi)//2 = (0+8)//2 = 4
so standard binary search would try to eliminate left half, as 8 should be on the right
BUT THAT IS NOT THE CASE AS 8 IS ON THE LEFT

##########################
SO WE NEED TO IDENTIFY THE SORTED HALF -> IF IT'S ON LEFT OR RIGHT

AFTER IDENTIFICATION, WE CAN APPLY BINARY SEARCH
##########################

Given:
arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
idx =  0, 1, 2, 3, 4, 5, 6, 7, 8
target = 1


* lo = 0, hi = 8, mid = (0+8)//2 = 4
    * arr[lo] <= arr[mid] --> if things are sorted
    * but this is not the case as arr[0] = 7 and arr[4] = 2
        * and 7 is not < 2
    * so we know that on the right of mid, things are sorted
    * and 1 cannot be on the right of mid, so eliminate the right half
    * so update hi = mid - 1
    * hi = 3

* lo = 0, hi = 3, mid = (0+3)//2 = 1
    * arr[mid] = arr[1] = 8
    * arr[lo] <= arr[mid] --> this section is sorted, following the sorted property
        * the right half is not following the sorted order
        * so right half is not sorted
    * we check if target is on the left side:
        7 <= 1 <= 8
        * but since 1 is not on this section, we eliminate this section
        * lo = mid + 1
        * lo = 2

* lo = 2, hi = 3, mid = (2+3)//2 = 2
    * arr[mid] = arr[2] = 9
    * the left portion is sorted as:
        arr[lo] <= arr[mid]
    * now check if 1 is present in this section:
        arr[lo] <= target <= arr[mid]
        9 <= 1 <= 9
        * 1 is not in this left partition, so eliminate the left section
        * move to right
    * lo = mid + 1
    * lo = 3

* lo = 3, hi = 3, mid = 3
    * arr[mid] = arr[3] = 1
    * arr[mid] == target, return the index


def f(arr, n, target):
    lo = 0
    hi = n-1

    while lo <= hi:
        mid = (lo+hi)//2

        # check if target found
        if arr[mid] == target:
            return mid
        # identify the sorted half
        # either it should be left sorted or right sorted
        if arr[lo] <= arr[mid]:
            # it should follow this property
            # left half is sorted

            # Now do the elimination
            if arr[lo] <= target and target <= arr[mid]:
                # target lies within the left half
                # eliminate the right half
                hi = mid - 1
            else:
                # target doesn't lie in the left half
                # eliminate the left half and move right
                lo = mid + 1
        else:
            # right half is sorted
            # if target lies in the right half
            # it should satisfy this condition:
            if arr[mid] <= target and target <= arr[hi]:
                # target lies in the right half
                # eliminate the left half
                lo = mid + 1
            else:
                # target lies in the left half
                # eliminate the right half
                hi = mid - 1


    # IF nothing is found
    return -1


"""



def search(arr, n, target):
    lo = 0
    hi = n - 1

    while lo <= hi:
        if arr[mid] == target:
            return mid

        # If left half is sorted
        if arr[lo] <= arr[mid]:
            # Check if target lies in the left half
            if arr[lo] <= target and target <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # If right half is sorted
        else:
            if arr[mid] <= target and target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1






