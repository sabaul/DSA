"""
SORT AN ARRAY OF 0's, 1's and 2's
---------------------------------

arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]


BRUTE -> SORT THE ARRAY
-----------------------
- MERGE SORT -> n * log(n) time complexity


BETTER 
------
* since we know that the array only stores 0, 1, 2
* keep a count of 0, 1 and 2
* then add these 0's, 1's and 2's to the input array

time complexity: O(n+n) -> O(2n) -> O(n)
space complexity: constant





"""

def brute(arr):
	n = len(arr)
	res = []
	for i in range(3):
		for j in range(n):
			if arr[j] == i:
				res.append(arr[j])
	return res


def better(arr):
	count = {}
	for n in arr:
		count[n] = 1 + count.get(n, 0)

	idx = 0
	for i in range(3):
		for j in range(count.get(i)):
			arr[idx] = i
			idx += 1
	return arr

arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(brute(arr))
print(better(arr))



"""

OPTIMAL -> DUTCH NATIONAL FLAG ALGORITHM
----------------------------------------

Rules of this algorithm:
	* elements from index [0 ... low-1]  ->  store 0  -> extreme left
	* elements from index [low ... mid-1]  -> store 1
	* elements from index [high+1 ... n-1] -> store 2 -> extreme right


the hypothetical array looks like this:
	
  [ [0  ...  low-1] [low  ...  mid-1] [mid  ...  high] [high+1  ...  n-1] ]
	 ^         ^      ^          ^      ^          ^      ^           ^
	 |         |      |          |      |          |      |           |
	 0 0 0 0 0 0      1 1 1 1 1 1 1     ------------      2 2 2 2 2 2 2
	                                       0/1/2
	                                     {unsorted}
	                                     {portion}
	                                     {of array}

	* The above 3 rules and 3 pointers will be used to solve this problem


Observation:

  [ [0  ...  low-1] [low  ...  mid-1] [mid  ...  high] [high+1  ...  n-1] ]
	 ^         ^      ^          ^      ^          ^      ^           ^
	 |         |      |          |      |          |      |           |
	 0 0 0 0 0 0      1 1 1 1 1 1 1     ------------      2 2 2 2 2 2 2
	 
	 {                            }        0/1/2          {           }
	 {                            }      {unsorted}       {           }
	 -----------------------------       {portion}        -------------
	    {sorted portion}                 {of array}       {sorted portion}


	* array from [0 to low-1] and [low to mid-1] is SORTED
	* array from [high+1 to n-1] is SORTED
	* if we can somehow manage to sort the unsorted portion, then our task will be easy




* Initially we're starting with the entire array
	* mid = 0 and high = n-1
		* as the entire array is unsorted
	* low = 0
		* as that's the starting index
		* and everything from index 0 to low-1 is zero
		* so this is still valid


	  low
	   ^
	   |
arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
       ^								^
       |								|
       mid								high


* arr[mid] can have these values: 0/1/2

	* if arr[mid] == 0

  [ [0  ...  low-1] [low  ...  mid-1] [mid  ...  high] [high+1  ...  n-1] ]
	 ^         ^      ^          ^      ^          ^      ^           ^
	 |         |      |          |      |          |      |           |
	 0 0 0 0 0 0      1 1 1 1 1 1 1     ------------      2 2 2 2 2 2 2
	 
	 {                            }        0/1/2          {           }
	 {                            }      {unsorted}       {           }
	 -----------------------------       {portion}        -------------
	    {sorted portion}                 {of array}       {sorted portion}

		* how to make sure that this zero is in sorted order
		* we know one thing:
			* left portion is sorted
			* so zero has to be on the left
			* zero will be somewhere before index low 
				* (as from low to mid-1 we have stored 1)
				* (as from 0 to low-1 we have stored 0)
			* so if we place this zero at index low, and swap the 1 stored at index low with this index at mid
				* arr[low], arr[mid] = arr[mid], arr[low]
			* the array will still be sorted
			* now the unsorted position becomes from index (mid+1) to high
				* so increment mid to mid+1
				* also increment low to low+1
					* so that 
						* 0 to low-1 is zero -> SORTED
						* low to mid-1 is one -> SORTED
						* mid to high is UNSORTED
		if arr[mid] == 0:
			swap(arr, low, mid) -> arr[low], arr[mid] = arr[mid], arr[low]
			low += 1
			mid ++ 1


	* if arr[mid] = 1

  [ [0  ...  low-1] [low  ...  mid-1] [mid  ...  high] [high+1  ...  n-1] ]
	 ^         ^      ^          ^      ^          ^      ^           ^
	 |         |      |          |      |          |      |           |
	 0 0 0 0 0 0      1 1 1 1 1 1 1     ------------      2 2 2 2 2 2 2
	 
	 {                            }        0/1/2          {           }
	 {                            }      {unsorted}       {           }
	 -----------------------------       {portion}        -------------
	    {sorted portion}                 {of array}       {sorted portion}

		* if it's a 1
			* index 0 to low-1 -> zero -> SORTED
			* index low to mid-1 -> one -> SORTED
			* index mid -> arr[mid] = 1
				* just increment mid value as it's already sorted

		if arr[mid] == 1:
			mid += 1


	* if arr[mid] = 2

  [ [0  ...  low-1] [low  ...  mid-1] [mid  ...  high] [high+1  ...  n-1] ]
	 ^         ^      ^          ^      ^          ^      ^           ^
	 |         |      |          |      |          |      |           |
	 0 0 0 0 0 0      1 1 1 1 1 1 1     ------------      2 2 2 2 2 2 2
	 
	 {                            }        0/1/2          {           }
	 {                            }      {unsorted}       {           }
	 -----------------------------       {portion}        -------------
	    {sorted portion}                 {of array}       {sorted portion}

		* we know:
			* 0 to low-1 -> zero -> sorted
			* low to mid-1 -> one -> sorted
			* high+1 to n-1 -> two -> sorted
			* mid to high -> contains 0/1/2 -> UNSORTED

			* so move swap arr[mid] with arr[high]
				* arr[mid], arr[high] = arr[high], arr[mid]
				* decrement high index by one
			* we can sort one more element
				* so now UNSORTED region becomes: mid to high-1

		if arr[mid] == 2:
			swap(arr[mid], arr[high]) -> arr[mid], arr[high] = arr[high], arr[mid]
			high -= 1

* the algorithm stops when mid crosses high
	* this means the UNSORTED region -> from mid to high-1
		* no longer exists



IN SHORT SUMMARY:
-----------------
	if arr[mid] == 0:
		swap(arr[mid], arr[low])
		low += 1
		mid += 1
	elif arr[mid] == 1:
		mid += 1
	elif arr[mid] == 2:
		swap(arr[mid], arr[high])
		high -= 1
"""


class Solution:
    def brute(self, nums, n):
        return nums.sort()
    
    def better(self, nums, n):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        idx = 0
        for i in range(3):
            for j in range(count.get(i, 0)):
                nums[idx] = i
                idx += 1
        return nums
    
    def optimal(self, nums, n):
        """
        Dutch National flag algorithm. 
        """
        low, mid, high = 0, 0, n-1

        while mid <= high:
            if nums[mid] == 0:
                # swap nums[mid] and nums[low]
                # increment both index
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # increment the mid as it's sorted only
                mid += 1
            else:
                # swap nums[mid] and nums[high]
                # decrement high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
    
    def sortZeroOneTwo(self, nums):
        n = len(nums)
        # res = self.brute(nums, n)
        # res = self.better(nums, n)
        res = self.optimal(nums, n)
        return res