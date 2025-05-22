"""
Same as question 5.
--- But it's a circular neighbour.---
--- Last house is the adjacent to the first house. ---
You can't rob 2 adjacent houses, police will be notified.
"""


def striver_constant_space(arr):
	n = len(arr)
	first = 0
	second = arr[0]
	for i in range(1, n):
		pick = arr[i]
		if i > 1:
			pick += first
		not_pick = second
		third = max(pick, not_pick)
		first, second = second, third
	# return max(first, second)
	return second

arr = [2, 3, 2, 5]
ans1 = striver_constant_space(arr[1 : ])
ans2 = striver_constant_space(arr[ : -1])
print(max(ans1, ans2))