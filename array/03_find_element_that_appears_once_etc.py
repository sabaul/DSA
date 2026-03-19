"""
PROBLEM 1. FINDING MISSING NUMBER IN AN ARRAY
-------------------------------------
Given n, and an array of (n-1) elements, these (n-1) elements contain number between 1 to n
Find the missing number

arr = [1, 2, 4, 5], N = 5
	- answer = 3 is not present between 1 to 5


BRUTE:
* for all the numbers between 1 to n
* search for the element each time by iterating in the array
* time complexity: O(n^2)


"""
def brute(arr, n):
	n = len(arr)
	for i in range(1, n+1):
		flag = 0
		for j in range(n):
			if arr[j] == i:
				flag = 1
				break
		if flag == 0:
			return i

arr = [1, 2, 4, 5]
n = 5

print(f"[BRUTE] Missing number: {brute(arr, n)}")


"""
BETTER APPROACH: HASHING
------------------------

arr = [1, 2, 4, 5], N = 5
	- answer = 3 is not present between 1 to 5

- create a hash array of size n+1 -> to store everything from 0 to n
- iterate over the array and mark the elements as 1 one by one (mark as 1)
	- reiterate from 1 to n, and look for who is not MARKED (not marked = 0)
	- so whatever is not MARKED, is going to be the answer
"""

def better(arr, n):
	track = [0 for i in range(n+1)]

	for i in range(len(arr)):
		track[arr[i]] = 1

	for i in range(1, n+1):
		if track[i] == 0:
			return i

arr = [1, 2, 4, 5]
n = 5

print(f"[BETTER] Missing number: {better(arr, n)}")

"""
OPTIMAL APPROACH: SUM
---------------------
SUM OF FIRST N NATURAL NUMBERS = N * (N+1) / 2 = 5 * 6 / 2 = 15
SUM OF ELEMENTS IN ARRAY = 1 + 2 + 4 + 5 = 12

MISSING NUMBER = 15 - 12 = 3
"""

def optimal1(arr, n):
	sum_n = n * (n+1) / 2
	sum_arr = 0
	for n in arr:
		sum_arr += n

	return sum_n - sum_arr

arr = [1, 2, 4, 5]
n = 5

print(f"[OPTIMAL 1] Missing number: {better(arr, n)}")



"""
OPTIMAL 2: XOR APPROACH
-----------------------
XOR PROPERTIES
	- XOR of same number numbers together will be zero
		- a XOR a = 0
		- 1 XOR 1 = 0
		- 2 XOR 2 = 0
	- XOR of a number with zero is that number itself
		- 0 XOR 1 = 1
		- 0 XOR 3 = 3

so solution approach for this problem ( ^ means XOR )
calculate:
	xor1 = 1^2^3^4^5
	xor2 = 1^2^4^5

	xor1 ^ xor2 = 3
as
	(1^1) ^ (2^2) ^ (3) ^ (4^4) ^ (5^5)
	= 0 ^ 3
	= 3
		--> this is the missing number
"""

def optimal2(nums, n):
    xor1 = 0
    xor2 = 0

    for i in range(n):
        xor1 ^= (i+1)
        xor2 ^= nums[i]
    return xor1 ^ xor2


arr = [0, 1, 2, 4, 5]
n = 5

print(f"[OPTIMAL 2] Missing number: {optimal2(arr, n)}")



"""
PROBLEM 2: MAXIMUM CONSECUTIVE 1's
----------------------------------

arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
ans = 3


"""

def max_consecutive1(arr):
	res = 0
	count = 0
	for i in range(len(arr)):
		if arr[i] == 1:
			count += 1
			res = max(res, count)
		else:
			count = 0
	return res


arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(f"MAX CONSECUTIVE 1: {max_consecutive1(arr)}")


"""
PROBLEM 3: FIND THE NUMBER THAT APPEARS ONCE, AND THE OTHERS TWICE
------------------------------------------------------------------

arr = [1, 1, 2, 3, 3, 4, 4]


BRUTE APPROACH:
---------------
* take first element
	* now do linear search looking for same number, count how many time that number appears

* time complexity: O(n^2)
* space complexity: O(1)

def brute(arr):
	n = len(arr)
	for i in range(n):
		num = arr[i]
		count = 0
		for j in range(n):
			if arr[j] == num:
				count += 1
		if count == 1:
			return num
	return -1


BETTER SOLUTION:
----------------
* HASHING

* hash array size = max(arr) + 1
	* max value of the array is used to build the hash array storing count of no. of time an element appears in the array
	* +1 is for zero

* time complexity: O(3*n)
* space complexity: O(max(arr))

def better(arr):
	n = len(arr)
	maxi = arr[0]
	for i in range(1, n):
		maxi = max(maxi, arr[i])

	hash = [0 for i in range(maxi+1)]

	for i in range(n):
		hash[arr[i]] += 1

	for i in range(n):
		if hash[arr[i]] == 1:
			return arr[i]



OPTIMAL APPROACH: XOR PROPERTY
------------------------------
 The problem can be efficiently solved using the properties of the XOR bitwise operator. The key properties of XOR are:

    a^a = 0 (XOR of any number with itself is 0).
    a^0 = a (XOR of any number with 0 is the number itself).
    XOR is both commutative and associative, meaning the order in which you apply XOR does not matter.


Using these properties, calculating XOR all the numbers in the array, the pairs of identical numbers will cancel each other out (because a ^ a = 0), and the result will be the number that appears only once. 

Approach:
    * Start with a variable initialized to 0. This variable will be used to store the cumulative XOR of all numbers in the array.
    * Loop through each element in the array. For each element, update the cumulative XOR by applying the XOR operation between the current cumulative XOR value and the current array element.
    * After iterating through all the elements, the cumulative XOR will hold the value of the integer that appears only once in the array.



def optimal(self, nums):
    res = 0
    for n in nums:
        res ^= n
    return res

"""

