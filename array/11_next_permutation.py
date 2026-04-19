"""
NEXT PERMUTATION
----------------
* Given the array of integers
* Find the next permutation of this array

arr = [3, 1, 2]


Q > What is permutation?
A >
	* Given an array
	* we can have following permutations:
		[1, 2, 3]
		[1, 3, 2]
		[2, 1, 3]
		[2, 3, 1]
		[3, 1, 2]
		[3, 2, 1]
	* How many possible permutations are possible = 3 factorial
												  = 3!
												  = 3 * 2 * 1
												  = 6 possible ways

	* What is next permutation?
		* All the possible permutations needs to be written in sorted order
		* Write them in dictionary order
		* 123 < 132 < 213 < 231 ... and so on

	* What if the input order of array was [3, 2, 1]
	* If we look at all the permutations
		* 123 < 132 < 213 < 231 < 312 < 321
		* Nothing comes after this
	* So we will fall back to the first possible arrangement
		* So answer = [1, 2, 3]


--------------------
BRUTE FORCE SOLUTION
--------------------
1. Generate all the permutations in sorted order
	* time complexity = N! * N
	* there will be N! permutations
	* and all of them are of size N
		* e.g. 
			5! = 120
			15! ~ 10^12
		* So this is extremely expensive operation time wise
2. linear search to find where 312 lies
3. Next index permutation will be the answer


How to generate all the permutations -> RECURSION

	* WE WILL NOT BE USING THIS APPROACH



-------------------------------
we don't have a better solution
-------------------------------
we will directly go to the OPTIMAL SOLUTION
-------------------------------


arr = [2, 1, 5, 4, 3, 0, 0]
	   0  1  2  3  4  5  6
           |
         step 1 -> i = 1


Approach Algorithm Steps:
-------------------------
1. Find longest prefix match, and stop when you find 
	arr[i] < arr[i+1]
	* If there is no dip, it's the largest possible permutation
	* so we need to sort the entire array
	* e.g.
		[5, 4, 3, 2, 1]
		* next permutation will be [1, 2, 3, 4, 5]
	* Instead of sorting, we can reverse the array

2. Find anything longer than the element at arr[i], but take the smallest one, so that you stay close

3. Try to place the remaining elements in sorted order



Dry Run:
--------
arr = [2, 1, 5, 4, 3, 0, 0]
	   0  1  2  3  4  5  6
           |
         step 1 -> i = 1

Step 1: Find longest prefix match
---------------------------------
	* arr[1] < arr[2]
	* we found the point of change index = 1


Step 1 Code:
------------
idx = -1
for i in range(n-2, -1, -1):
	if arr[i] < arr[i+1]:
		idx = i
		break

if we don't find the idx, and idx is still -1
We just need to directly reverse the entire array
That will be the answer



Step 2: Find the smallest element greater than arr[i]
		swap that element with arr[i]
-----------------------------------------------------

Step 2 Code:
------------

for i in range(n-1, idx, -1):
	if arr[i] > arr[idx]:
		swap(arr[i], arr[idx])


Array becomes: [2, 3, 5, 4, 1, 0, 0]
				0  1  2  3  4  5  6
                   |        |


Step 3: we knew that the array from last was already in increasing order from the end to the left
	* from index 6, 5, 4, 3, 2 -> increasing order
	* so instead of sorting it, we can reverse it


Step 3 code:
------------
reverse(arr, idx+1, n-1)




COMPLETE CODE:

def next_permutation(arr):
	n = len(arr)
	idx = -1

	# Step 1: find the arr[i] < arr[i+1]
	for i in range(n-2, -1, -1):
		if arr[i] < arr[i+1]:
			idx = i
			break

	if idx == -1:
		return arr[::-1]

	# Step 2: Find element from idx to n-1
	# such that arr[i] > arr[idx]
	# swap it
	for i in range(n-1, idx, -1):
		if arr[i] > arr[idx]:
			# swap(arr, i, idx)
			arr[i], arr[idx] = arr[idx], arr[i]
			break

	# Step 3: Reverse the remaining array from idx+1 to n-1
	return arr[:idx+1] + arr[n-1, idx, -1]

"""

def next_permutation(arr):
	n = len(arr)
	idx = -1

	# Step 1: find the arr[i] < arr[i+1]
	for i in range(n-2, -1, -1):
		if arr[i] < arr[i+1]:
			idx = i
			break

	if idx == -1:
		return arr[::-1]

	# Step 2: Find element from idx to n-1
	# such that arr[i] > arr[idx]
	# swap it
	for i in range(n-1, idx, -1):
		if arr[i] > arr[idx]:
			# swap(arr, i, idx)
			arr[i], arr[idx] = arr[idx], arr[i]
			break

	# Step 3: Reverse the remaining array from idx+1 to n-1
	return arr[:idx+1] + arr[n-1 : idx : -1]


# arr = [2, 1, 5, 4, 3, 0, 0]
# print(next_permutation(arr))

# arr = [5, 4, 3, 2, 1]
# print(next_permutation(arr))


def reverse(arr):
	lo, hi = 2, len(arr)-1
	while lo < hi:
		arr[lo], arr[hi] = arr[hi], arr[lo]
		lo += 1
		hi -= 1
	return arr

arr = [1, 2, 3, 4, 5]
print(reverse(arr))