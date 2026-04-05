"""
MAXIMUM SUBARRAY SUM - KADANE'S ALGORITHM
-----------------------------------------
* out of all the subarray's give me the maximum sum
* SUBARRAY: contiguous part of the array
	* e.g. from the below array:
		* [-2], [-1, -2], [-2, -3, 4]
		* subarray is contiguous


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
		0   1  2   3   4  5  6   7

	* ans = 7
	* from index 2 to 6 -> [4, -1, -2, 1, 5]


BRUTE
-----
* Try out all the subarrays
* which ever gives the maximum sum is the answer
	* time complexity: O(n^3)
	* space: O(1)

def brute(arr):
	n = len(arr)
	maxsum = float('-inf')
	for i in range(n):
		for j in range(i, n):
			total = 0
			for k in range(i, j):
				total += arr[k]
			maxsum = max(maxsum, total)
	return maxsum


BETTER
------
* instead of iterating in the third array and adding
* we can just keep on adding the elements in the subarray
	* by adding the next value
	* time complexity: O(n^2)
	* space complexity: O(1)

def better(arr):
	n = len(arr)
	maxsum = float('-inf')
	for i in range(n):
		total = 0
		for j in range(i, n):
			sum += arr[j]
		maxsum = max(maxsum, total)
	return maxsum


"""

def brute(arr):
	n = len(arr)
	maxsum = float('-inf')
	for i in range(n):
		for j in range(i, n):
			total = 0
			for k in range(i, j+1):
				total += arr[k]
			maxsum = max(maxsum, total)
	return maxsum


def better(arr):
	n = len(arr)
	maxsum = float('-inf')
	for i in range(n):
		total = 0
		for j in range(i, n):
			total += arr[j]
			maxsum = max(maxsum, total)
	return maxsum


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(f"Brute: {brute(arr)}")
print(f"Better: {better(arr)}")

"""
OPTIMAL -> KADANE'S ALGORITHM
----------------------------

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
		0   1  2   3   4  5  6   7

* set maxi = float('-inf')

* now start from 0 index
	* with sum = 0

	* idx = 0, val = -2, sum = -2
		* compare with maxi, update maxi = max(maxi, sum)
	* idx = 1, val = -3, sum = -5
		* as -5 is smaller than -3 (the value at idx=1)
		* no point in taking -3
		* set sum = 0, maxi = -2 unchanged
			* when sum < 0
				* reset sum = 0

"""


def optimal(arr):
	cursum = 0
	maxi = float('-inf')

	for i in range(len(arr)):
		cursum += arr[i]
		if cursum > maxi:
			maxi = cursum
		if cursum < 0:
			cursum = 0
	if maxi < 0:
		maxi = 0
	return maxi

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(f"OPTIMAL: {optimal(arr)}")




"""
FOLLOW UP: PRINT THE MAXIMUM SUBARRAY (ANY OF IT)
-------------------------------------------------

If we re-observe the kadane's algorithm
	* our sum value is going below 0 (negative)
	* whenever it's going -ve
		* we're resetting cursum = 0
		* basically we're starting our subarray sum from this point
		* so that is our starting point of subarray
	* when we're updating the maxi
		* that's the end of maximum subarray till that point
		* so that is the end of our subarray sum array

"""

def optimal_print(arr):
	cursum = 0
	maxi = float('-inf')
	start = -1
	ansStart = -1
	ansEnd = -1

	for i in range(len(arr)):
		if cursum == 0:
			start = i
		cursum += arr[i]
		if cursum > maxi:
			maxi = cursum
			ansStart = start
			ansEnd = i
		if cursum < 0:
			cursum = 0
	if maxi < 0:
		maxi = 0

	return maxi, arr[ansStart : ansEnd+1]


print(f"Optimal print: {optimal_print(arr)}")
