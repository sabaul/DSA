"""
MAJORITY ELEMENTS
	* find the elements that appears more than N/2 times
		* if N = 8 -> appear more than 4 times
		* if N = 9 -> appear more than 4 times -> math.floor(9/2)


arr = [2, 2, 3, 3, 1, 2, 2]
	* N = 7
	* 2 appears 4 times
		* it's greater than N/2 = 3 times




BRUTE
-----
* Go through each number in the array
* then count how many times that number appears
* keep track of the number which can be the majority element
	* time complexity: O(n^2)

def brute(arr):
	n = len(arr)
	for i in range(n):
		count = 0
		for j in range(n):
			if arr[j] == arr[i]:
				count += 1

		if count > math.floor(n/2):
			return arr[j]
	return -1


BETTER -> hashing
-----------------
* keep the {key: value} pair with {element: count}
* iterate over array and get this count
* then iterate over the hashmap and get the majority element

def better(arr):
	n = len(arr)
	majority_limit = math.floor(n/2)
	count = {}
	for n in arr:
		count[n] = 1 + count.get(n, 0)

	for k, v in count.items():
		if v > majority_limit:
			return k
	return -1
"""

import math

def brute(arr):
	n = len(arr)
	for i in range(n):
		count = 0
		for j in range(n):
			if arr[j] == arr[i]:
				count += 1

		if count > math.floor(n/2):
			return arr[j]
	return -1


def better(arr):
	n = len(arr)
	majority_limit = math.floor(n/2)
	count = {}
	for n in arr:
		count[n] = 1 + count.get(n, 0)

	for k, v in count.items():
		if v > majority_limit:
			return k
	return -1

arr = [2, 2, 3, 3, 1, 2, 2]
print(f"Brute: {brute(arr)}")
print(f"Better: {better(arr)}")



"""
OPTIMAL APPROACH -> MOORE'S VOTING ALGORITHM
--------------------------------------------

arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]


DRY RUN FOR THIS ALGORITHM:
---------------------------

Initialize 2 variables:
	* element = None
	* count = 0

Start iterating:

arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5,  7,  7,  5,  5,  5,  5]
       |                 |
       -------------------
idx	   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15


	* element = 7 -> first element -> ASSUME THIS IS THE ANSWER
	* count = 1 -> idx = 0
			  2 -> idx = 1 (increment as arr[2] == 7)
			  1 -> idx = 2 (decrement as arr[2] != 7)
			  2 -> idx = 3 (increment as arr[3] == 7)
			  1 -> idx = 4 (decrement as arr[4] != 7)
			  0 -> idx = 5 (decrement as arr[5] != 7)


	* now that count = 0
		* this means:
			* if we just consider this portion of array {idx 0 to 5}
			* 7 is definitely not our majority element
				* it got incremented 3 times
				* it got decremented 3 times by other elements
					* it got evened out
					* it can't occur more than 6/2

	* reset the element to the next element at index 6
	* reset the count to 1

arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5,  7,  7,  5,  5,  5,  5]
                         |                |
                         ------------------
idx	   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15


	* element = 5 -> element at index 6 -> ASSUME THIS IS THE ANSWER
	* count = 1 -> idx = 6
			  0 -> idx = 7 (decrement as arr[7] != 5)

	
	* now that count = 0
		* 5 can't be our majority element
	* reset the element to the next element at index 8
	* reset the count to 1

arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5,  7,  7,  5,  5,  5,  5]
                               |          |
                               ------------
idx	   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15

	* element = 5 -> element at index 8 -> ASSUME THIS IS THE ANSWER
	* count = 1 -> idx = 8
			  2 -> idx = 9 (increment as arr[9] == 5)
			  1 -> idx =10 (decrement as arr[10] != 5)
			  0 -> idx =11 (decrement as arr[11] != 5)
			  

	* now that count = 0
	* reset the element to the next element at index 12
	* reset the count to 1

arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5,  7,  7,  5,  5,  5,  5]
											  |           |
                                              -------------
idx	   0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15


	* element = 5 -> element at index 12 -> ASSUME THIS IS THE ANSWER
	* count = 1 -> idx = 12
			  2 -> idx = 13 (increment as arr[13] == 5)
			  3 -> idx = 14 (increment as arr[14] == 5)
			  4 -> idx = 15 (increment as arr[15] == 5)


	* WE HAVE ENDED THE ARRAY ITERATION
		* finally we have the element 5
		* because it was the only element which not got cancelled out by others

	* WE NEED TO BE SURE AND VERIFY IF 5 IS THE MAJORITY ELEMENT
	* THE ALGORITHM SAYS:
		* IF WE HAVE A MAJORITY ELEMENT, IT WILL BE THIS ELEMENT 5
		* SO WE NEED TO VERIFY THIS STATEMENT

	* EXAMPLE:
		* assume the last 4 elements were 1
		* so is 1 the majority element?
			* 1 total count in the array = 5
			* array_size = 16
				* 1 doesn't appear more than 16/2 times
				* so 1 is not the majority element
				return -1

	* FOR THE CURRENT SCENARIO
		* element = 5 at the end of array iteration
		* total count of 5 in array = 9
		* array size = 16
			* 5 appears more than 16/2 times
			* so 5 is the majority element


PROCEDURE FOR THIS ALGORITHM
----------------------------
1. Apply MOORE'S VOTING ALGORITHM
2. Verify that the element that we got is the majority element by iterating in the array

"""


def optimal(arr):
	n = len(arr)
	count = 0
	element = None

	for i in range(n):
		if count == 0:
			# reset the element and count
			count = 1
			element = arr[i]
		elif arr[i] == element:
			# increment the count
			count += 1
		else:
			# if it's a different element
			# decrement the count
			count -= 1

	# Verify the element we got at the end
	# If it's the majority element
	counter = 0
	for i in range(n):
		if arr[i] == element:
			counter += 1

	if counter > math.floor(n/2):
		return element
	return -1
