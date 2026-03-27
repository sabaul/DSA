"""
=========================================================
TWO SUM - VARIANT 1
-------------------
Pick 2 elements from array, that sum up to target, 
return True if possible, return False if not possible

arr = [2, 6, 5, 8, 11], target = 14
ANSWER -> True

=========================================================

TWO SUM - VARIANT 2
-------------------
Pick 2 elements from array, that sum up to target
we are sure that the sum will be able to reach target
return where these 2 elements are present

arr = [2, 6, 5, 8, 11], target = 14
ANSWER -> [1, 3]
	* as arr[1] + arr[3] = 6 + 8 = 14

=========================================================

=========================================================
=========================================================
BRUTE APPROACH
--------------
=========================================================
=========================================================
* pick first element
	* check every other element
* pick second element
	* check every other element
* Time Complexity: O(n^2)


def brute(arr, n):
	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			elif arr[i] + arr[j] == target:
				return True or return [i, j]
	return [-1, -1]

OPTIMIZE THIS BRUTE FORCE SOLUTION
----------------------------------
* when we pick first element
	* we start from next elements
* when we pick second element
	* we don't need to check the elements prior to this element again
	* as they won't work
	* so look for elements from after that element

* Time complexity: O(n^2) still

def brute_optimized(arr, n):
	for i in range(n):
		for j in range(i+1, n):
			if arr[i] + arr[j] == target:
				return True or [i, j]
	return [-1, -1]



=========================================================
=========================================================
BETTER - HASHMAP
=========================================================
=========================================================

def better(arr, n, target):
	track = {}
	for i, num in enumerate(arr):
		required = target - num
		if required in track:
			return [i, track[required]]
		track[num] = i
	return [-1, -1]



=========================================================
=========================================================
OPTIMAL - WITHOUT USING HASHMAP (RESTRICTION)
- 2 pointer approach

- Sort the input array
- then use 2 pointer approach

- Time complexity: O(n * logn)
- But this will only work for variety 1, as we need to return True/False

- when we need indices as well, we need to store the indices in an array as well
- something like this: [2, 6, 5, 8, 11]
	- store it like this: [(2, 0), (6, 1), (5, 2), (8, 3), (11, 4)]
	- now sort it based on first element of tuple
	- then use the algorithm
	- But this is not optimal for SECOND VARIETY
=========================================================
=========================================================

def optimal(arr, n, target):
	arr.sort()
	lo, hi = 0, n-1
	while lo < hi:
		cursum = arr[lo] + arr[hi]
		if cursum == target:
			return True
		elif cursum > target:
			hi -= 1
		else:
			lo += 1
	return False

"""