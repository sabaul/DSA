"""
Recursion   -> n-1 to 0
-----------------------
f(n - 1, 3) -> max merit points from 0 to (n-1)th day when
			-> on day n, task 3 was done
			-> 3 = no task was performed

f(2, 1) -> max merit points from 0 to 2, given that on the
		-> day n you performed task 1
"""

def f(day, last, points):
	if day == 0:
		# do something
		maxi = 0
		for task in range(3):
			if task != last:
				maxi = max(points[day][task], maxi)
		return maxi

	maxi = 0
	for task in range(3):
		if task != last:
			cur_score = points[day][task] + f(day - 1, task, points)
			maxi = max(maxi, cur_score)
	# print(f"maxi: {maxi}")
	return maxi

def f_memoized(points):
	days = len(points)
	tasks = len(points[0])
	dp = [[-1 for i in range(tasks + 1)] for j in range(days)]

	def f1(day, last):

		if dp[day][last] != -1:
			return dp[day][last]

		if day == 0:
			maxi = 0
			for task in range(tasks):
				if task != last:
					maxi = max(maxi, points[day][task])
			return maxi

		maxi = 0
		for task in range(tasks):
			if task != last:
				cur_score = points[day][task] + f1(day - 1, task)
				maxi = max(maxi, cur_score)
		dp[day][last] = maxi
		return dp[day][last]

	return f1(days - 1, 3)



points = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f(len(points) - 1, len(points[0]), points))
print(f_memoized(points))

points = [[2, 1, 3], [3, 4, 6], [10, 1, 6], [8, 3, 7]]
print(f(len(points) - 1, len(points[0]), points))
print(f_memoized(points))