"""
FIND OUT HOW MANY TIMES HAS AN ARRAY BEEN ROTATED




Given array:
    arr = [3, 4, 5, 1, 2], answer = 3
    idx =  0, 1  2  3  4

* ideally the sorted array should have been this: [1, 2, 3, 4, 5]
* but we have 2 sections in the array: [3, 4, 5] and [1, 2]
* it has been rotated 3 times 


* FIND THE MINIMUM ELEMENT IN THE ROTATED SORTED ARRAY
* THAT INDEX WILL GIVE US THE NUMBER OF TIMES THE ARRAY IS ROTATED

* it's at index 3 -> so the array has been rotated 3 times


* another example
    arr = [1, 2, 5, 7, 8, 9]

    * how many times the array has been rotated
        * minimum element index = 0
        * zero times the array has been rotated


"""


def find_num_rotations(arr):
    n = len(arr)
    lo, hi = 0, n-1
    ans = float('inf')
    index = -1

    while lo <= hi:
        mid = (lo+hi)//2

        # search space is already sorted
        # then always arr[lo] willl be smaller
        # in that search space
        if arr[lo] <= arr[hi]:
            if arr[lo] < ans:
                index = lo
                ans = arr[lo]


        if arr[lo] <= arr[mid]:
            if arr[lo] < ans:
                index = lo
                ans = arr[lo]
            lo = mid + 1
        else:
            hi = mid - 1
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid

    return index

arr = [3, 4, 5, 1, 2]
print(find_num_rotations(arr))


arr = [1, 2, 5, 7, 8, 9]
print(find_num_rotations(arr))
