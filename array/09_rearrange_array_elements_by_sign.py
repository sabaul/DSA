"""
REARRANGE ARRAY ELEMENTS BY SIGN
--------------------------------
* given array of even length
* elements are +ve or -ve
* arrange them such that:
	* first element is positive
	* For all integers with the same sign, the order in which they were present in nums is preserved.
	* Every consecutive pair of integers have opposite signs.


arr = [3, 1, -2, -5, 2, -4]

result arr = [3, -2, 1, -5, 2, -4]



BRUTE:
------
* keep 2 array:
	* positive -> n/2 size
	* negative -> n/2 size
	* result = [iterate and add +ve and -ve elements from positive and negative]

* TC -> O(n) + O(n/2)
* SC -> O(n)


--------------------------------------------------------
-> OPTIMIZE SPACE COMPLEXITY
	-> we can't 
	-> we need to somehow maintain the elements in the required pattern
	-> for that we need extra space

-> we can reduce the 2 pass over array and make it 1 pass
--------------------------------------------------------


OBSERVATION 1:
----------------
* All the positive elements will be at even index
	* result arr = [3, -2, 1, -5, 2, -4]
					0   1  2   3  4   5

		* 1st positive -> 0
		* 2nd positive -> 2
		* 3rd positive -> 4

* All negative elements are at odd index
		* 1st negative -> 1
		* 2nd negative -> 3
		* 3rd negative -> 5



"""


def brute(arr):
	positive = []
	negative = []
	res = []

	for n in arr:
		if n > 0:
			positive.append(n)
		else:
			negative.append(n)

	for i in range(len(positive)):
		res.append(positive[i])
		res.append(negative[i])

	return res



def optimal(arr):
	n = len(arr)
	positive_count = 0
	negative_count = 0
	res = [0 for i in range(n)]

	for n in arr:
		if n > 0:
			positive_count += 1
			idx = 2 * (positive_count - 1)
			res[idx] = n
		else:
			negative_count += 1
			idx = (2 * (negative_count - 1)) + 1
			res[idx] = n
	return res


def optimal_simpler(arr):
	n = len(arr)
	posindex = 0
	negindex = 1
	res = [0 for i in range(n)]

	for n in arr:
		if n > 0:
			res[posindex] = n
			posindex += 2
		else:
			res[negindex] = n
			negindex += 2
	return res


arr = [3, 1, -2, -5, 2, -4]

print(f"Brute: {brute(arr)}")
print(f"Optimal: {optimal(arr)}")
print(f"optimal_simpler: {optimal_simpler(arr)}")



"""
VARIETY 2
---------
* no mention of equal number of positive and negative elements
* if any of the positive and negative numbers are left
	* add them at the end without altering the order


* either:
	* num_positives > num_negatives
	* num_negatives > num_positives



arr = [1, 2, -4, -5, 3, 6]

* num_positives = 4
* num_negatives = 2
	* num_positives > num_negatives


* we've solved for num_positives == num_negatives

* if num_positives != num_negatives
	1. num_positives > num_negatives
	2. num_negatives > num_positives


* WE CAN'T USE OPTIMAL SOLUTION
* FALL BACK TO THE BRUTE FORCE SOLUTION

* pos = [2, 3, 4, 1]
* neg = [-1, -3]
	* len(pos) > len(neg)


"""


def second_variant_brute(arr):
	n = len(arr)
	pos = []
	neg = []
	res = []

	for n in arr:
		if n > 0:
			pos.append(n)
		else:
			neg.append(n)

	poslen = len(pos)
	neglen = len(neg)
	# print(f"poslen: {poslen} -> {pos}")
	# print(f"neglen: {neglen} -> {neg}")
	if poslen > neglen:
		for i in range(neglen):
			# print(i)
			res.append(pos[i])
			res.append(neg[i])

		for i in range(neglen, poslen):
			# print(i, pos[i])
			res.append(pos[i])
	else:
		for i in range(poslen):
			res.append(pos[i])
			res.append(neg[i])

		for i in range(poslen, neglen):
			res.append(neg[i])

	return res


arr = [1, 2, -4, -5, 3, 6]

print(f"SECOND VARIANT: {second_variant_brute(arr)}")