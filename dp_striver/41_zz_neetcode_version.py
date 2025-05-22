"""
BRUTE FORCE - DFS
-----------------

arr = [0, 1, 0, 3, 2, 3]


DFS WITH CACHE
--------------

arr = [1, 2, 4, 3]
"""



def solution(arr):
	n = len(arr)
	LIS = [1] * n

	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			if arr[i] < arr[j]:
				LIS[i] = max(LIS[i], 1 + LIS[j])
	return max(LIS)


def self1(arr):
	n = len(arr)
	lis = [1] * n

	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			if arr[i] < arr[j]:
				lis[i] = max(lis[i], 1 + lis[j])
	return max(lis)



def lis(arr):
	n = len(arr)
	res = [1] * n

	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			if arr[i] < arr[j]:
				res[i] = max(res[i], 1 + res[j])
	return max(res)



arr = [0, 1, 0, 3, 2, 3]
# print(solution(arr))
# print(self1(arr))
print(lis(arr))

print('-'*3)

arr = [1, 2, 4, 3]
# print(solution(arr))
# print(self1(arr))
print(lis(arr))