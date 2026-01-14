"""
###################################
AGGRESSIVE COWS

	- given an array, which consists of N stalls, you are given the coordinates of each stall
		- coordinates is nothing but indices 
	- TASK: place x no. of cows in such a way that the minimum distance between any of the 2 cows is the maximum

	- minimum distance between any 2 cows is maximum
###################################


arr = [0, 3, 4, 7, 10, 9], cows = 4


CONFIGURATION 1:
----------------
if we sort the input array, and place cows:
	0   3   4   7   9   10
	c1  c2  c3  c4

	- this is one way of placing cows
	- what is the distance b/w any of 2 cows:
		c1-c2 = 3
		c2-c3 = 1
		c3-c4 = 3
		c1-c3 = 4
		c2-c4 = 4
		c1-c4 = 7
	- what is the minimum distance among all the cows
		c2-c3 = 1

		- this minimum distance will always be between consecutive stalls


CONFIGURATION 2:
----------------
If we place it like this:
	0   3   4   7   9   10
	c1      c2      c3  c4

	- distance between any 2 cows:
		c1-c2 = 4
		c1-c3 = 9
		c1-c4 = 10
		c2-c3 = 5
		c2-c4 = 6
		c3-c4 = 1

	- what is the minimum distance among all the cows
		c3-c4 = 1

		- again it's 1


CONFIGURATION 3:
----------------
If we place it like this:
	0   3   4   7   9   10
	c1      c2  c3      c4

	- distance between any 2 cows:
		c1-c2 = 4
		c1-c3 = 7
		c1-c4 = 10
		c2-c3 = 3
		c2-c4 = 6
		c3-c4 = 3

	- what is the minimum distance among all the cows
		3


If we look at all our configurations, 
and the minimum distance among all the cows:

	CONFIGURATION 1: 1
	CONFIGURATION 2: 1
	CONFIGURATION 3: 3

and the requirement is that:
the minimum distance between any of the cows should be maximized

SO WE WILL CHOOSE CONFIGURATION 3: return ans=3



POINTS TO NOTICE:
-------------------------------------------
POINT 1: SINCE WE NEED MINIMUM DISTANCE BETWEEN COWS
-------------------------------------------
* we just need the consecutive distance between cows
* in the configurations 1, 2, and 3 above, we don't need these:
	* c1-c3
	* c1-c4
	* c2-c4

	* so just calculating the consecutive distances will do

-------------------------------------------
POINT 2: THE GIVEN ARRAY IS NON-SORTED ORDER
-------------------------------------------
* sort the input array



#############################
HOW TO SOLVE:
#############################

arr = [0, 3, 4, 7, 10, 9], cows = 4


let's try to keep the distance between any 2 cows at minimum = 1
we can place it like this:
	  0   3   4   7   9   10
	  c1  c2  c3  c4
dist:    3   1   3


let's try to keep the distance between any 2 cows at minimum = 2
we can place it like this:
	  0   3   4   7   9   10
	  c1  c2      c3  c4
dist:    3    4      2

let's try to keep the distance between any 2 cows at minimum = 3
we can place it like this:
	  0   3   4   7   9   10
	  c1  c2      c3      c4
dist:    3    4       3

let's try to keep the distance between any 2 cows at minimum = 4
we can place it like this:
	  0   3   4   7   9   10
	  c1      c2      c3  
dist:     4       5       

	* this won't work (NOT POSSIBLE)
	* as we can't place all the 4 cows


in the problem statement, it's given that we will have a minimum of 2 cows

and the maximum distance between 2 cows can be: max(arr) - min(arr)
e.g: 
we can place it like this:
	  0   3   4   7   9   10
	  c1                  c2 
dist:          10

distance: max(arr) - min(arr) = 10 - 0 = 10

SO THE RANGE BECOMES: [1, max(arr)-min(arr)]


brute force code:
=================
TIME COMPLEXITY: O(max-min) * O(n)
SPACE COMPLEXITY: O(1)

def can_we_place(arr, dist, cows):
	# cow 1 will always be placed at index 0
	# so initially the cow count will be 1, at coordinate = arr[0]

	count_cows = 1
	last_cow_coordinate = arr[0]

	for i in range(1, len(arr)):
		if arr[i] - last_cow_coordinate >= dist:
			# we can place this cow here
			count_cows += 1
			last_cow_coordinate = arr[i]

	# at the end of the day
	# if we're able to place more than the number of cows
	# by maintaining a minimum distance
	# we can return Possible (True)
	# else return Not possible (False) 
	if count_cows >= cows:
		return True
	return False


def bruteforce(arr, num_cows):
	# sort the input arr
	arr.sort()

	for i in range(1, max(arr)-min(arr)+1):
		if can_we_place(arr, i, num_cows):
			continue
		else:
			# return the previous value
			# in the how to solve section, we could'nt place 4 cows at distance of 4
			# so max possible was the previous value, in that case 3
			return (i-1)



-------------------------------------------------
CAN WE APPLY BINARY SEARCH HERE: TO OPTIMIZE: YES
-------------------------------------------------

MAX DISTANCE POSSIBLE:
	1 2 3 4 5 6 7 8 9 10
	o o o x x x x x x  x

	- we have a region where it's possible
	- we have a region where it's not possible

- we're looking for the max possible answer
- we can do:
	lo = 1, first possible answer
	hi = 10, last possible answer

lo=1, hi=10, mid=5
	* arr[mid] = 5, not possible to place 4 cows at distance=5
	* anything on right is also not possible
	* eliminate right search space
	* hi = mid - 1 = 4

lo = 1, hi = 4, mid = 2
	* arr[mid] = 2, possible to place 4 cows at distance=2
	* anything on left also possible, but we're looking for max
	* look right, eliminate left search space
	* lo = mid + 1 = 3

lo = 3, hi = 4, mid = 3
	* arr[mid] = 3, possible to place 4 cows at distance = 3
	* we need max, look right, eliminate left search space
	* lo = mid + 1 = 4

lo = 4, hi = 4, mid = 4
	* arr[mid] = 4, not possible to place 4 cows at distance=4
	* eliminate right search space, look left
	* hi = mid - 1 = 3
		* lo crosses hi
		* stop the while loop
		* return the last answer



"""


def can_we_place(arr, dist, cows):
	# cow 1 will always be placed at index 0
	# so initially the cow count will be 1, at coordinate = arr[0]

	count_cows = 1
	last_cow_coordinate = arr[0]

	for i in range(1, len(arr)):
		if arr[i] - last_cow_coordinate >= dist:
			# we can place this cow here
			count_cows += 1
			last_cow_coordinate = arr[i]

			if count_cows >= cows:
				return True

	# at the end of the day
	# if we're able to place more than the number of cows
	# by maintaining a minimum distance
	# we can return Possible (True)
	# we can add the True condition inside for loop to optimize it
	# else return Not possible (False) 
	# if count_cows >= cows:
	# 	return True
	return False


def bruteforce(arr, num_cows):
	# sort the input arr
	arr.sort()
	# distance_range = max(arr) - min(arr)
	distance_range = arr[-1] - arr[0]

	for i in range(1, distance_range+1):
		if can_we_place(arr, i, num_cows):
			continue
		else:
			# return the previous value
			# in the how to solve section, we could'nt place 4 cows at distance of 4
			# so max possible was the previous value, in that case 3
			return (i-1)


def binary_search(arr, num_cows):
	arr.sort()
	lo = 1
	# hi = max(arr) - min(arr)
	hi = arr[-1] - arr[0]
	ans = -1

	while lo <= hi:
		mid = (lo+hi)//2

		if can_we_place(arr, mid, num_cows):
			# update answer and eliminate left half
			ans = mid
			lo = mid + 1
		else:
			# not possible, eliminate right half
			hi = mid - 1
	return ans



arr = [0, 3, 4, 7, 10, 9]
cows = 4
print(bruteforce(arr, cows))
print(binary_search(arr, cows))