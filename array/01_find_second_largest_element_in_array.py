"""
FIND LARGEST ELEMENT IN ARRAY

brute -> sort + return last element
	  -> TC: O(nlogn)
	  -> SC: O(1)

optimal -> linear search + keep track of largest element
		-> TC: O(n)
		-> SC: O(1)
"""

def largest_element_in_array(arr):
	largest = float('-inf')
	for num in arr:
		if num > largest:
			largest = num
	return largest


arr = [3, 2, 1, 5, 2]
print(f"input array: {arr}")
print(f"largest_element_in_array: {largest_element_in_array(arr)}")


"""
FIND SECOND LARGEST ELEMENT IN ARRAY

brute -> sort + return second last element
	  -> to find second largest element:
	  		store largest ( the last element in the array )
	  		then iterate from the n-2 element and compare with largest, if it's not equal to largest, it's the second largest
	  -> TC: O(nlogn)
	  -> SC: O(1)


better -> linear search + keep track of largest element
			-> first pass -> find the largest element
			-> second pass -> look for largest again, but not equal to the largest we found in the first pass
		-> TC: O(n)
		-> SC: O(1)


optimal -> linear search in one pass
			-> largest = arr[0] -> treat this as largest for index 0
			-> s_largest = -1

			-> iterate over the array starting second element
				-> if an element is greater than the largest
					-> update largest, and second_largest will be now take largest value
				-> if something is not larger than largest
					-> check if it's larger than second largest
					-> if it is, update second largest
"""

def find_second_largest_brute(arr):
	arr.sort()
	n = len(arr)
	largest = arr[-1]
	for i in range(n-2, -1, -1):
		if arr[i] != largest:
			return arr[i]
	return -1

def find_second_largest_better(arr):
	arr.sort()
	n = len(arr)

	# first pass
	largest = float('-inf')
	for num in arr:
		if num > largest:
			largest = num

	# second pass
	second_largest = float('-inf')
	for num in arr:
		if num > second_largest and num != largest:
			second_largest = num
	return second_largest


def find_second_largest_optimal(arr):
	largest = arr[0]
	slargest = -1

	for i in range(1, len(arr)):
		if arr[i] > largest:
			slargest = largest
			largest = arr[i]
		elif arr[i] > slargest and arr[i] < largest:
			slargest = arr[i]
	return slargest





arr = [1, 2, 4, 7, 7, 5]
print(f"input array: {arr}")
print(f"find_second_largest_brute : {find_second_largest_brute(arr)}")
print(f"find_second_largest_better : {find_second_largest_better(arr)}")
print(f"find_second_largest_optimal : {find_second_largest_optimal(arr)}")

arr = [7, 7, 7, 7, 7]
print(f"input array: {arr}")
print(f"find_second_largest_brute : {find_second_largest_brute(arr)}")
print(f"find_second_largest_better : {find_second_largest_better(arr)}")
print(f"find_second_largest_optimal : {find_second_largest_optimal(arr)}")



def secondlargest(arr, n):
	largest = arr[0]
	slargest = -1

	for i in range(1, len(arr)):
		if arr[i] > largest:
			slargest = largest
			largest = arr[i]
		elif arr[i] > largest and arr[i] > slargest:
			slargest = arr[i]
	return slargest

def secondsmallest(arr, n):
	smallest = arr[0]
	ssmallest = float('inf')

	for i in range(1, n):
		if arr[i] < smallest:
			ssmallest = smallest
			smallest = arr[i]
		elif arr[i] < ssmallest and arr[i] != smallest:
			ssmallest = arr[i]
	return ssmallest

def find_second_largest_and_second_smallest_element(arr, n):
	slargest = secondlargest(arr, n)
	ssmallest = secondsmallest(arr, n)
	return [slargest, ssmallest]




"""
###########################################
# CHECK IF THE ARRAY IS SORTED
ARRAY IN NON-DESCENDING ORDER
###########################################
"""
def check_if_sorted(arr, n):
	for i in range(1, n):
		if arr[i] >= arr[i-1]:
			continue
		else:
			return False
	return True


"""
REMOVE DUPLICATES IN-PLACE FROM THE SORTED ARRAY
	- modify the array in place and return the number of unique elements in array

arr = [1, 1, 2, 2, 2, 3, 3]


Brute Force:
	- declare a set, add elements
	- it will only have unique elements, count the length
	- then replace values in the original array
	- return


Optimization:
	- 2 pointer approach
	- update the left index when any value is different than the left index

"""

def brute(arr, n):
	set_arr = set(arr)
	for i, num in enumerate(set_arr):
		arr[i] = num
	print(arr)
	return arr

arr = [1, 1, 2, 2, 2, 3, 3]
n = len(arr)
res = brute(arr, n)



def optimize(arr, n):
	i = 0
	for j in range(1, n):
		if arr[j] != arr[i]:
			arr[i+1] = arr[j]
			i += 1
	return arr, i



def removeDuplicates(self, nums: List[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i += 1
    return i+1


print(f"input array: {arr}")
arr, count = optimize(arr, n)
print(f"output array: {arr}")
print(f"unique element count: {count}")