"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



min in rotated sorted array with unique elements

arr = [4, 5, 6, 7, 0, 1, 2]
idx =  0  1  2  3  4  5  6

brute force -> linear search while keeping track of the smallest number

optimized -> binary search
* we need to somehow eliminate the search space

lo = 0, hi = 6, mid = (0+6)//2 = 3
	* arr[mid] = 7

left space -> sorted -> arr[lo] <= arr[mid] -> 4 <= 7
	* the smallest element in the sorted section might be our answer
		* update ans = min(ans, arr[lo])
	* eliminate the left half
		* lo = mid + 1




"""

def brute_force(arr):
	min_num = float('inf')
	for num in arr:
		if num < min_num:
			min_num = num
	return min_num


def bs(arr):
	lo = 0
	hi = len(arr) - 1
	ans = float('inf')

	while lo <= hi:
		mid = (lo+hi)//2
		if arr[lo] <= arr[mid]:
			# left half is sorted
			# update answer and eliminate the left search space
			ans = min(ans, arr[lo])
			lo = mid + 1
		else:
			# right half is sorted
			# update answer and eliminate the right search space
			ans = min(ans, arr[mid])
			hi = mid - 1
	return ans




arr = [4,5,6,7,0,1,2]
print(brute_force(arr))
print(bs(arr))


arr = [4, 5, 1, 2, 3]
print(brute_force(arr))
print(bs(arr))


arr = [2, 1]
print(brute_force(arr))
print(bs(arr))


arr = [7, 8, 1, 2, 3, 4, 5, 6]
print(brute_force(arr))
print(bs(arr))