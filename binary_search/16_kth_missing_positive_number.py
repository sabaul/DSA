"""
###################################
FIND Kth MISSING NUMBER

	- given an array of increasing integers
	- find the kth missing number
###################################

example:


arr = [2, 3, 4, 7, 11], k = 5

* we have, last number is 11
	- write numbers from 1 to 11, and 
	- highlight which numbers are missing and which are present
		- x -> missing
		- o -> present
	- 1 2 3 4 5 6 7 8 9 10 11
	  x o o o x x o x x  x  o
	  1       2 3   4 5  6

	- the 5th missing number is 9
		- RETURN 9



####################
BRUTE FORCE SOLUTION
####################

arr = [2, 3, 4, 7, 11], k = 5

* we get 2, it will take 1 place, now k = 6
* we get 3, it will take 1 place, now k = 7
* we get 4, it will take 1 place, now k = 8
* we get 7, it will take 1 place, now k = 9
* we get 11, it exceeded the k value, we can STOP NOW
	* so the answer to the brute force is 9

==================================================
	* BASICALLY THE NUMBERS THAT ARE LESSER THAN K
	* WILL TAKE IT'S PLACE, SO MOVE NEXT
	* WHERE WE STOP, THAT'S THE ANSWER

---------------------------
---------------------------
BRUTE FORCE EXPLANATION 1:
---------------------------
---------------------------

let have array be [2, 3, 4, ,5] and find 5th missing number


so the concept is

let consider intially that all numbers are missing and if all numbers are missing then our fifth missing number will be x= 5 so now if we iterate over array and we consider 2(0th element of array) so now  2 is not missing anymore so now our 5th missing number will be x= 6 ,again on iterating we get 3 now our 3 is no more missing so now our 5th missing number will be x=7 ...........



and in this process if we find any element of array greater then x(where x is 5th missing number)  it means that 5th missing number which is x till now is lesser then current element of array hence it is our answer





---------------------------
---------------------------
BRUTE FORCE EXPLANATION 2:
---------------------------
---------------------------

 assume you have an empty array and we have some k value, say k = 4the missing number, so in this case the missing value would be 4


Case 1:- where the value at a index in the array < k
now just consider the empty array again and we added a number smaller than k to it, say 2, so now when we again try to find the 4th missing number we would get it as 5 ( as 1 3 4 5 , as 2 already present in the array, hence the missing value shifts by one position ahead and 5 is the 4th missing value), hence whenever we get a number in the array smaller than k, the kth missing value shifts by position ahead


Case2 :- where value at a index in array > k
now consider empty array again and we added a number greater than k, assume k = 4 and we added 7 to it, here the kth missing element will be 4 itself, as even though seven was added - it indicated that the array might or might not contain the first 6 numbers and as the k = 4 value is lesser than 7, so this kth value would also come under missing value, and as 7 > k, so no effect on k occur. So k is the missing element



==================================================

#########################
BRUTE FORCE CODE SOLUTION
#########################

def brute_force(arr, k):
	last_integer = max(arr) # in the array

	for i in range(last_integer):
		if arr[i] <= k:
			k += 1
		else:
			break
	return k


#########################
OPTIMIZE THE SOLUTION
	- what's better than O(n)
	- O(log(n))

	- hints:
		- array is sorted
		- we need something better than O(n)
		- BINARY SEARCH
#########################

arr = [2, 3, 4, 7, 11], k = 5
idx =  0  1  2  3   4

for the given inputs:

- can we apply typical binary search?
	- NO, as we are searching for the number, and the required number is not in the array, we can't use the typical binary search

- can we apply binary search on answers?
	- NO, as binary search on answers is only applicable when you're only looking for minimum or maximum
	- and you know that we have a pattern like this:
		x x x x x o o o o o 
		where x -> NOT POSSIBLE
		where o -> POSSIBLE
		i.e. some portion is not possible and other portion is possible

- here it's a different case
	- the answer 9 should have been between 7 and 11
	- so if we can figure out between which two indices our number can lie, OUR PROBLEM IS SOLVED
		- for the given case, it's between index 3 and 4

	- so how to apply binary search in this question
	- We're sure the answer will lie between 2 and 11 for k = 5
	- Also for this k = 5, the answer is 9, which lies between 7 and 11
	- for k = 3, the answer is 6, which lies between 4 and 7
	- Now, for binary search, we take the entire range in the array, for this case, it's from 2 to 11
		- if somehow, we can figure out the smaller range, like 7 and 11 here
		- so if we figure out the 2 nearby indices, PROBLEM SOLVED


- SO NOW OUR PROBLEM BECOMES: FIND TWO NEARBY INDICES

arr = [2, 3, 4, 7, 11], k = 5
idx =  0  1  2  3   4

ideally, the numbers should have been this:
ideal_arr = [1, 2, 3, 4, 5]
given_arr = [2, 3, 4, 7,11], k = 5
array_idx =  0  1  2  3  4

at the place of 7, we should have had 4
the integers, should have been:
	1 2 3 4 5 6 7 8 9 10 11
	x       x x   x x  x

		here x -> missing number

	in given array, at index 3, number of missing numbers => 7 - 4 = 3
	in given array, at index 4, number of missing numbers => 11 - 5 = 6

- at index 3 we have 3 missing numbers
- at index 4 we have 6 missing numbers

- we are looking for 5th missing number, it will lie between index 3 and 4

ideal_arr = [1, 2, 3, 4, 5]
given_arr = [2, 3, 4, 7,11], k = 5
array_idx =  0  1  2  3  4

misin_arr =  1  1  1  3  6

so we can do binary search on the misin_array (it has the count of number of missing numbers till that point)

lo = 0, hi = 4, mid = (0+4)//2 = 2
	- arr[mid] = 2
	- here, number of missing numbers = 1
	- we're looking for 5th missing, so we can eliminate this one
	- eliminate left portion, look into the right portion
	- lo = mid + 1 = 3

lo = 3, hi = 4, mid = (3+4)//2 = 3
	- arr[mid] = 7
	- here, number of missing numbers = 7 - (mid+1) = 3
	- we're looking for 5th missing, so we can eliminate this one
	- eliminate left portion, look into the right portion
	- lo = mid + 1 = 4

lo = 4, hi = 4, mid = (4+4)//2 = 4
	- arr[mid] = 11
	- here, number of missing numbers = 11 - (mid+1) = 6
	- we're looking for 5th missing, so we can eliminate this one
	- eliminate right portion, look into the left portion
	- hi = mid - 1 = 3

BUT HERE LO AND HI HAVE CROSSED EACH OTHER
- lo > hi, the while loop will stop, and what we have is:
	- lo = 4
	- hi = 3

- POINT TO NOTICE:
	- lo is at an index which is greater than k
	- hi is at an index which is smaller than k

INITIALLY:
	- lo was smaller than k (at 1, in the misin_arr)
	- hi was greater than k (at 6, in the misin_arr)

EVENTUALLY:
	- we are ending at 2 nearby indices, lo and hi


NOW WE NEED TO FIND THE 5TH NUMBER


arr[hi] = 7, numbers missing = 3, we need 2 more, as we need 5th missing no.
so increment arr[hi] 2 times, we get 9, that is the answer
	- arr[hi] + how_many_more_we_need

- BUT, we can't use the arr[hi] here
- example array: [4, 7, 9], k = 3

- hi will point to index before 4
- hi will get to -1, and lo will be at 0
	- this is where the third missing number will be
	- although python will work with this, but it will give incorrect answers
	- DON'T USE HI


- in our original problem: arr = [2, 3, 4, 7, 11], k = 5
- after binary search ends:
	- hi = 3
	- lo = 4
- arr[hi] = 7, missing_numbers = 3, more_nums_required = 2

Formula for missing numbers:
	arr[hi] - (hi+1)

How many more do we need:
	= arr[hi] + more
	= arr[hi] + (k - missing) {as more = k - missing}
	= arr[hi] + k - (arr[hi] - (hi+1))
	= arr[hi] + k - arr[hi] + hi + 1
	= k + hi + 1
	= low + k {as lo = hi + 1}


the binary search code:

def bs(arr, k):
	lo = 0
	hi = len(arr)-1

	while lo <= hi:
		mid = (lo+hi)//2

		missing = arr[mid] - (mid+1)
		if missing < k:
			# eliminate the left half
			lo = mid + 1
		else:
			# eliminate the right half
			hi = mid - 1

	return lo + k

"""

def brute_force(arr, k):
	for i in range(len(arr)):
		if arr[i] <= k:
			k += 1
		else:
			break
	return k


def binary_search(arr, k):
	lo = 0
	hi = len(arr)-1

	while lo <= hi:
		mid = (lo+hi)//2
		missing_numbers = arr[mid] - (mid+1)
		if missing_numbers < k:
			# eliminate left search space
			lo = mid + 1
		else:
			# eliminate right search space
			hi = mid - 1
	return lo+k


arr = [2, 3, 4, 7, 11]
k = 5
print(brute_force(arr, k))
print(binary_search(arr, k))

arr = [4, 7, 9]
k = 3
print(brute_force(arr, k))
print(binary_search(arr, k))