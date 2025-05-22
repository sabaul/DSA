"""
LARGEST DIVISIBLE SUBSET
------------------------
	* Given an array of DISTINCT NUMBERS, 
	  print any subset such that given any two elements at i and j

		* arr[i] should be able to divide arr[j]
			OR
		* arr[j] should be able to divide arr[i]

arr = [1, 16, 7, 8, 4]

	* e.g. [16, 8, 4]
		* [16, 8] --> 16 is divisibile by 8
		* [16, 4] --> 16 is divisibile by 4
		* [8, 4]  --> 8 is divisibile by 4

	* Largest divisible subset: [1, 16, 8, 4]
		* all elements can divide all other elements
		* 16/1 possible
		* 8/1 possible
		* 4/1 possible
		* 16/8 possible
		* 16/4 possible
		* 8/4 possible
		* ALL THE PAIRS ARE DIVISIBLE
			* can be a possible answer
			* len(arr) = 4
		* since we need subset, we can use any way to print the subset:
			* [1, 4, 8, 16], [4, 1, 16, 8], [16, 8, 4, 1]


	* if we add a 7 to the above subset, it won't work
		* as 7 is not divisible by 4, 8, 16
		AND
		* 7 can't divide anything else


arr = [1, 16, 7, 8, 4]

Subsequence 
-----------
	* contiguous/non-contiguous elements from array,
	* where the order of elements in the array should be maintained
	* e.g. [1, 16, 8]

Subset
------
	* Order is not important anymore
	* no need to follow order of elements
	* e.g. [1, 8, 16], [1, 16, 8], [1, 7, 16]


Solution approach
-----------------

* Sort the array

arr = [1, 4, 7, 8, 16]

* Print any answer
	* subsequence problem
		* take
		* not take
	* we can sort it and then share the answer
	* as long as the divisibility is not compromized

CODE SOLUTION APPROACH
----------------------

1. sort the input array now
   arr = [1, 3, 7, 8, 16]

2. how to make sure, each pair is divisible?
	* since input is sorted
	* say we select 1
		* we can select 4 as 4/1 is possible
			* can't select 7 as 7/4 is not possible
		* we can select 8 as 8/4 is possible
			* as 4/1 is possible, 8/1 will also be possible
		* we can select 16, as 16/8 is possible
			* as 8/4 is possible, and 4/1 is possible
			* 16/4 and 16/1 is also possible
		* arr = [1, 4, 8, 16]



###################################################################

* longest increasing subsequence (old problem)
* longest divisible subsequence  (new problem) -> current

* after sorting the input array
* [1, 4, 8, 16]
	* 4/1  -true
	* 8/4  -true
	* 16/8 -true
	* earlier we were looking for increasing order of elements
	* now we just need to check for divisibility
		* pick next number if it is divisible with current numbers

###################################################################

CODE FOR LIS

for i in range(n):
	for j in range(i):
		if arr[j] < arr[i] and dp[i] < dp[j] + 1:
			dp[i] = dp[j] + 1
			hash[i] = j


CODE FOR LONGEST DIVISIBLE SUBSEQUENCE (LDS)

for i in range(n):
	for j in range(i):
		if arr[i] % add[j] == 0 and dp[i] < dp[j] + 1:
			dp[i] = dp[j] + 1
			hash[i] = j
"""

# LONGEST INCREASING SUBSEQUENCE WITH SORTED INPUT ARRAY

def finalVersion(n, arr):
	arr.sort()

	dp = [1] * n
	backtrack = [i for i in range(n)]
	maxi = 1
	lastIndex = 0

	for i in range(n):
		for prev in range(i):
			if arr[i] % arr[prev] == 0 and 1 + dp[prev] > dp[i]:
				dp[i] = 1 + dp[prev]
				backtrack[i] = prev
		if dp[i] > maxi:
			maxi = dp[i]
			lastIndex = i

	res = []
	while True:
		res.append(arr[lastIndex])
		lastIndex = backtrack[lastIndex]
		if len(res) == maxi:
			return res




arr = [1, 16, 7, 8, 4]
print(finalVersion(len(arr), arr))