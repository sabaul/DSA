"""
LONGEST SUBARRAY WITH GIVEN SUM K (ARRAY HAS ONLY POSITIVES IN THE ARRAY)
-----------------------------------------------------------------------

What is subarray?
- Contiguous part of the array
- Otherwise it's not a subarray
- e.g. -> [1], [1, 1, 1], [4, 2, 3] --> all are subarray


arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3], k = 3
       0  1  2  3  4  5  6  7  8  9

for this problem, the possible subarrays are:
	[1, 2] -> sum = 3, length = 2
	[3] ----> sum = 3, length = 1
	[1, 1, 1] -> sum = 3, length = 3 ---> RETURN LENGTH OF THIS SUBARRAY = 3
	 3  4  5

	[1, 1, 1] -> sum = 3, length = 3 ---> RETURN LENGTH OF THIS SUBARRAY = 3
	 4  5  6


############################################
BRUTE APPROACH -> GENERATE ALL THE SUBARRAYS
############################################

to generate all the subarrays
n = len(arr)
for i in range(n):
	for j in range(i, n):


"""

def brute(arr, target):
	"""
	time complexity: O(n^3)
	space complexity: O(1) -> no/constant extra space
	"""
	n = len(arr)
	res = 0
	for i in range(n):
		for j in range(i, n):
			total = 0
			for k in range(i, j):
				total += arr[k]
			if total == target:
				print(f"j:{j}, arr[j]: {arr[j]}")
				print(f"i:{i}, arr[i]: {arr[i]}")
				print(f"array: {arr[i:j]}, target: {target}")
				print('-'*30)
				res = max(res, j-i+1)
	return res

def brute_optimized(arr, target):
	"""
	time complexity: O(n^2)
	space complexity: O(1)
	"""
	n = len(arr)
	res = 0
	for i in range(n):
		total = 0
		for j in range(i, n):
			total += arr[j]
		if total == target:
			res = max(res, j-i+1)
	return res

arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
#      
k = 3
print(arr)
idx = [i for i in range(len(arr))]
print(idx)
print('-'*30)
# print(f"Brute: {brute(arr, k)}")
# print(f"Brute Optimized: {brute_optimized(arr, k)}")


"""
BETTER APPROACH -> hashmap
--------------------------
* compute prefix sum and store in hashmap
* at any point i:
	current total sum = total
		we need a subarray of sum target
		so if at any point previously in the array, we have (total - target) at index j
		then it means from index j to i, the subarray sum = target
	so keep a track of the largest subarray with res
	and return the maximum value of res finally

[VERY SIMILAR TO 2 SUM PROBLEM BUT WITH SUBARRAY]


* this will work when elements in array have +ve's and zeroes and -ve's
"""

def better(arr, target):
	res = 0
	n = len(arr)
	prefixsum = {}
	total = 0

	for i, n in enumerate(arr):
		total += n
		if total == target:
			prefixsum[target] = i+1

		required_num = total - target
		if required_num in prefixsum:
			curlen = i - prefixsum[required_num]
			res = max(res, curlen)

		if required_num not in prefixsum:
			prefixsum[total] = i
	return res


arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
k = 3
print(f"Better: {better(arr, k)}")




"""
OPTIMAL APPROACH -> greedy 2 pointer approach
----------------
* keep 2 pointers
* start adding up numbers

if the sum of window == target:
	compute and store length
elif sum of window > target:
	remove from left, update current window total
	increment left
else:
	keep adding numbers to the window

"""


class Solution:
    # Function to find the length of longest subarray having sum k
    def longestSubarray(self, nums, k):
        n = len(nums)
        
        # To store the maximum length of the subarray
        maxLen = 0
        
        # Pointers to mark the start and end of window
        left = 0
        right = 0
        
        # To store the sum of elements in the window
        sum = nums[0]
        
        # Traverse all the elements
        while right < n:
            
            # If the sum exceeds K, shrink the window
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            
            # Store the maximum length
            if sum == k:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
            if right < n:
                sum += nums[right]
        
        return maxLen


nums = [10, 5, 2, 7, 1, 9]
k = 15

# Creating an object of Solution class
sol = Solution()

# Function call to find the length
# of longest subarray having sum k
ans = sol.longestSubarray(nums, k)

print(f"The length of longest subarray having sum k is: {ans}")
