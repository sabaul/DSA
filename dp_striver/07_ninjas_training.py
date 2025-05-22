"""
Ninja is planning his N days long training schedule. Each day, he
can perform any one of these three activities (Run, Fight, Learn new moves).

Each activity has some merit points on each day.
Ninja has to improve all his skills, he can't do the same activity in
two consecutive days.

Help ninja find out the maximum merit points Ninja can earn?

Given 2D array of size N*3 **points** with points corresponding to each day
and activity. Your task is to calculate the maximum number of merit
points that Ninja can earn.
"""

"""
1st, 2nd 3rd --> activities

input:
1st 2nd 3rd
10  50   1   --> day 0
5   100  11  --> day 1

Greedy Fails (if select 50 on day 1 and then 11 on day 2, we miss out on 100)

Try All Possible ways --> RECURSION (top down --> n --> 0)

1. Express problem in indices (days --> 0, 1, 2 ....)
2. Do stuffs on that index
	-> in order to find what to do on day index
	-> we need to know what task we did on previous day
	-> pass one more parameter
3. Find the max

last:
	0 -> task 0
	1 -> task 1
	2 -> task 2
	3 -> no task done previously (at beggening, i.e. at n)


def f(day, last):
	if day == 0:
		maxi = 0
		for i in range(3):
			if i != last:
				maxi = max(maxi, task[day][i])
		return maxi

	maxi = 0
	for i in range(3):
		if i != last:
			points = task[day][i] + f(day - 1, i)
			maxi = max(maxi, points)
	return maxi


t0 t1 t2
 2  1  3  d0
 3  4  6  d1
10  1  6  d2
 8  3  7  d3
"""

def f(day, last, points):
	if day == 0:
		maxi = 0
		for task in range(3):
			if task != last:
				maxi = max(maxi, points[day][task])
		return maxi

	maxi = 0
	for task in range(3):
		if task != last:
			point = points[day][task] + f(day - 1, task, points)
			# print(points, day, task, points)
			maxi = max(maxi, point)
	return maxi

def striver_recursion(points):
	days = len(points)
	num_tasks = len(points[0])
	return f(days - 1, num_tasks, points)


def f2(day, last, scores, dp):

	if dp[day][last] != -1:
		return dp[day][last]

	if day == 0:
		maxi = 0
		for task in range(3):
			if task != last:
				maxi = max(maxi, scores[day][task])
		return maxi

	maxi = 0
	for task in range(3):
		if task != last:
			points = scores[day][task] + f2(day - 1, task, scores, dp)
			maxi = max(maxi, points)
	dp[day][last] = maxi
	return dp[day][last]


def striver_recursion_memoized(scores):
	days = len(scores)
	tasks = len(scores[0])
	dp = [[-1 for i in range(tasks + 1)] for j in range(days)]
	return f2(days - 1, tasks, scores, dp)



def striver_tabulation(scores):
	days = len(scores)
	tasks = len(scores[0])
	dp = [[-1 for i in range(tasks + 1)] for j in range(days)]

	dp[0][0] = max(scores[0][1], scores[0][2])
	dp[0][1] = max(scores[0][0], scores[0][2])
	dp[0][2] = max(scores[0][0], scores[0][1])
	dp[0][3] = max(scores[0][0], scores[0][1], scores[0][2])

	for day in range(1, days):
		for last in range(tasks + 1):
			dp[day][last] = 0
			for task in range(tasks):
				if task != last:
					point = scores[day][task] + dp[day-1][task]
					dp[day][last] = max(dp[day][last], point)

	return dp[days - 1][tasks]


def ninjaTraining(n, points):
    # Initialize a list 'prev' to store the maximum points for each possible last activity on the previous day.
    prev = [0] * 4

    # Initialize 'prev' with the maximum points for the first day's activities.
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        # Initialize a temporary list 'temp' to store the maximum points for each possible last activity on the current day.
        temp = [0] * 4

        for last in range(4):
            # Initialize 'temp' for the current last activity.
            temp[last] = 0

            for task in range(3):
                if task != last:
                    # Calculate the total points for the current day's activity and the previous day's maximum points.
                    activity = points[day][task] + prev[task]
                    # Update 'temp' with the maximum points for the current last activity.
                    temp[last] = max(temp[last], activity)

        # Update 'prev' with 'temp' for the next iteration.
        prev = temp

    # Return the maximum points achievable after the last day with any activity.
    return prev[3]

def main():
    # Define the points matrix for each day.
    points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    n = len(points)  # Get the number of days.
    # Call the ninjaTraining function to find and print the maximum points.
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()



scores = [[2, 1, 3], [3, 4, 6], [10, 1, 6], [8, 3, 7]]
print(striver_recursion(scores))
print(striver_recursion_memoized(scores))
print(striver_tabulation(scores))
print(striver_space_optimized(scores))