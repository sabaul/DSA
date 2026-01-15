"""
#################################
ALLOCATE BOOKS OR BOOL ALLOCATION
#################################

	- given an array with number of pages in n books
	- with some m number of students

	- Allocate books such that:
		1. each student gets at least one book
			- say there are 4 students (example below), everyone of the 4 students must get at least one book
		2. each book should be allocated to only one student
			- one book can only go to one student
			- can't allocate one book to multiple students
		3. book allocation should be in a contiguous manner
			- given books arr = [25, 46, 28, 49, 24]
			- given 4 students -> 1 2 3 4
			- student 1 -> book 25
			- student 2 -> book 46
			- now we can't allocate book 28 to student 1
				- because it's not contiguous 

			- but we can do this:
				- student 1 - give book 25 and 46
				- student 2 - give book 28
				- student 3 - give book 49
				- student 4 - give book 24
			- it's allowed because it's CONTIGUOUS

	Satisfying all the above conditions:
	- Allocate the books to m students such that the maximum number of pages assigned to a student is MINIMUM
	- if allocation not possible return -1

#################################

example:
arr = [25, 46, 28, 49, 24], students = 4

* book allocation strategy 1 (in series 1, 2, 3, 4):
	25 | 46 | 28 | 49, 24 --> max no. of pages = 73 (student 4)


* book allocation strategy 2 (in series 1, 2, 3, 4):
	25 | 46 | 28, 49 | 24 --> max no. of pages = 77 (student 3)


* book allocation strategy 3 (in series 1, 2, 3, 4):
	25 | 46, 28 | 49 | 24 --> max no. of pages = 74 (student 2)


* book allocation strategy 4 (in series 1, 2, 3, 4):
	25, 46 | 28 | 49 | 24 --> max no. of pages = 71 (student 1)


* THE MINIMUM OF MAXIMUM NO. OF PAGES ALLOCATED TO STUDENTS = 71
	* ALLOCATION 4, PAGES = 71



-------------
HOW TO SOLVE:
-------------
* NOT POSSIBLE CONDITION
	* if number of students is greater than the number of books
		* we won't be able to allocate books with this
	* NOT POSSIBLE SCENARIO

* POSSIBLE SCENARIO
	* The minimum of max no. of pages allocated to students can be:
		1, 2, 3, 4 ....
	* the first number that is our answer, we will STOP (as we need minimum)

	* do we need to start from 1: NO
		* if we start from 1, he won't be able to hold the book
		* to hold one book, someone need at least 24 pages (for this example)
			* but if we take 24, the max someone is holding is 24 pages book
			* and they won't be able to hold book with pages 25, 46, 49
			* so we need to start from max no. of pages book

	* start from biggest no in array: max(arr)


example:
arr = [25, 46, 28, 49, 24], students = 4


MAX NO. OF PAGES THAT CAN BE ASSIGNED TO STUDENTS - CAPACITY = 49
* let's start from 49

book allocation strategy:
	* STUDENT 1 -> 25, it can't take 46 as it will exceed the limit 49
	* STUDENT 2 -> 46, it can't take 28 as it will exceed the limit 49
	* STUDENT 3 -> 28, it can't take 49 as it will exceed the limit 49
	* STUDENT 4 -> 49, it can't take 24 as it will exceed the limit 49
	* STUDENT 5 -> 24

		* BUT WE NEEDED TO ALLOCATE BOOKS TO 4 STUDENTS
		* WE EXCEEDED THE NUMBER OF STUDENTS
		* WHICH IS NOT ALLOWED, WE NEED TO FIT THE BOOKS INTO THE M STUDENTS


* we will increase the max. number of pages allocation to the students
* we'll go from 49 -> 50 -> 51 -> ..... -> 70



at 70: book allocation strategy:
	* STUDENT 1 -> 25, it can't take 46, as 71 will exceed the limit 70
	* STUDENT 2 -> 46, it can't take 28, as 74 will exceed the limit 70
	* STUDENT 3 -> 28, it can't take 49, as 77 will exceed the limit 70
	* STUDENT 4 -> 49, it can't take 24, as 73 will exceed the limit 70
	* STUDENT 5 -> 24	

		* BUT WE NEEDED TO ALLOCATE BOOKS TO 4 STUDENTS
		* WE EXCEEDED THE NUMBER OF STUDENTS
		* WHICH IS NOT ALLOWED, WE NEED TO FIT THE BOOKS INTO THE M STUDENTS


at 71: book allocation strategy:
	* STUDENT 1 -> 25+46 = 71, it can take 46, as 25+46=71 is equal to the limit 71
	* STUDENT 2 -> 28, it can't take 49, as 28+49=77 will exceed the limit 71
	* STUDENT 3 -> 49, it can't take 24, as 49+24=73 will exceed the limit 71
	* STUDENT 4 -> 24, allowed, it will not exceed the limit 71

		* WE ARE ABLE TO ALLOCATE ALL THE BOOKS WITHIN 4 STUDENTS
		* THIS IS THE MINIMUM NUMBER: RETURN 71

* what can be the maximum possible number of pages allocation for books
	* it will be the sum(arr)
		* with this we can allocate all the books to one student

	* say we have number of students = 1
		* we will have to allocate all the books to one student
		* so the max limit for no. of pages = sum(arr)

* SO THE RANGE WILL BE: [ max(arr) -> sum(arr) ]

* NOW WE WILL DO THE LINEAR SEARCH BRUTE FORCE CODE
	* time complexity: O(sum(arr) - max(arr) + 1) * O(n)



-------------------------
OPTIMIZE TO BINARY SEARCH
-------------------------
lo = max(arr)
hi = sum(arr)

answer will be from:
	49 ... ...  ...      71                       172
	^                    ^                        ^
	|                    |                        |
	5 students        4 students              1 student


	* at 49 pages -> 5 students (more than 4)
	* at 172 pages -> 1 student (less than 4)
		* answer lies somewhere between
		* apply binary search

lo=49, hi=172, mid=(49+172)//2 = 110
	* at page_limit=110, we can distribute books to 2 students
		1 -> 25, 46, 28
		2 -> 49, 24
	* we need to increase the number of students
		* so decrease the number of pages limit
		* eliminate right side
		* hi = mid - 1 = 109


lo=49, hi=109, mid=(49+109)//2 = 79
	* at page_limit=79, we can distribute books to 3 students
		1 -> 25, 46
		2 -> 28, 49
		3 -> 24
	* we need to increase the number of students
		* so decrease the number of pages limit
		* eliminate right side
		* hi = mid - 1 = 78


lo=49, hi=78, mid=(49+78)//2 = 63
	* at page_limit=63, we can distribute books to 5 students
		1 -> 25
		2 -> 46
		3 -> 28
		4 -> 49
		5 -> 24
	* we need to DECREASE the number of students
		* so increase the number of pages limit
		* eliminate LEFT side
		* lo = mid + 1 = 64


lo=64, hi=78, mid=(64+78)//2 = 71
	* at page_limit=71, we can distribute books to 4 students
		1 -> 25, 46
		2 -> 28
		3 -> 49
		4 -> 24
	* IT MATCHES OUR NEED, we need minimum number of pages 
		* so DECREASE the number of pages limit
		* eliminate RIGHT side
		* hi = mid - 1 = 70

lo = 64, hi = 70, mid = (64+70)//2 = 67
	* at page_limit=67, we can distribute books to 5 students
		1 -> 25
		2 -> 46
		3 -> 28
		4 -> 49
		5 -> 24
	* we need to DECREASE the number of students
		* so increase the number of pages limit
		* eliminate LEFT side
		* lo = mid + 1 = 68

lo = 68, hi = 70, mid = (68+70)//2 = 69
	* at page_limit=69, we can distribute books to 5 students
		1 -> 25
		2 -> 46
		3 -> 28
		4 -> 49
		5 -> 24
	* we need to DECREASE the number of students
		* so increase the number of pages limit
		* eliminate LEFT side
		* lo = mid + 1 = 70

lo = 70, hi = 70, mid = (70+70)//2 = 70
	* at page_limit=70, we can distribute books to 5 students
		1 -> 25
		2 -> 46
		3 -> 28
		4 -> 49
		5 -> 24
	* we need to DECREASE the number of students
		* so increase the number of pages limit
		* eliminate LEFT side
		* lo = mid + 1 = 71

	* lo crosses hi
	* while loop of binary search stops
	* stored ans = 71 is returned
"""

def count_students(arr, pages):
	students = 1
	page_limit = 0

	for num_pages in arr:
		if page_limit + num_pages > pages:
			page_limit = num_pages
			students += 1
		else:
			page_limit += num_pages
	return students

def bruteforce(arr, m):
	# impossible case
	if m > len(arr):
		return -1

	lo = max(arr)
	hi = sum(arr) + 1

	for pages in range(lo, hi):
		num_students = count_students(arr, pages)
		if num_students == m:
			return pages


def binary_search(arr, m):
	# impossible case
	if m > len(arr):
		return -1
	
	lo = max(arr)
	hi = sum(arr)
	ans = -1

	while lo <= hi:
		mid = (lo+hi)//2
		num_students = count_students(arr, mid)

		if num_students == m:
			ans = mid
			# but we need minimum number of pages that satisfies this condition
			hi = mid - 1

		elif num_students > m:
			# we need to decrease the number of students
			# for that, increase the number of pages
			lo = mid + 1

		else:
			# we need to increase the number of students
			# for that, decrease the number of pages
			hi = mid - 1
	return ans




arr = [25, 46, 28, 49, 24]
students = 4
print(bruteforce(arr, students))
print(binary_search(arr, students))