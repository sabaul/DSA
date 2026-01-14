"""
#############################################
LEAST CAPACITY TO SHIP PACKAGES WITHIN D DAYS

	- have 1 ship
	- have n items/products of certain weight W
	- have limited number of days d

	- MAKE SURE ALL THESE ITEMS ARE SHIPPED WITHIN d DAYS
	- FIND THE MINIMUM WEIGHT CAPACITY OF SHIP TO DO THIS
#############################################

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5




capacity = 100
	- load items 1, 2, 3, 4, .... 10
	- total weight = 55
	- as capacity = 100 and total weight is 55
	- we can do this in one day
	- but we need to find the least capacity

say,
capacity = 10
	day 1, load items 1, 2, 3, 4 
	- total weight =10, is equal to capacity
		- so on first day, we can send products 1, 2, 3, 4
		
	day 2, load item 5
	- total weight = 5 ( as if we load the 6th item, it will go over capacity )
		- so second day, we can send only product 5

	day 3, load item 6
	- total weight = 6
		- third day, we can only send product 6

	day 4, load item 7
	- total weight = 7
		- fourth day, we can only send product 7

	day 5, load item 8, weight 8
	- total weight = 8
		- fifth day, we can only send product 8

	day 6, product item 9, weight 9
	- total weight = 9
		- sixth day, we can only send product 9

	day 7, product item 10, weight 10
	- total weight = 10
		- seventh day, we can only send product 10

	* we had to do this in 5 days
	* it took us 7 days to complete this
	* CAPACITY = 10, NOT POSSIBLE


say now,
capacity = 15
	day 1, add items 1, 2, 3, 4, 5
	- total weight = 15, allowed

	day 2, add items 6, 7
	- total weight = 13, allowed

	day 3, add items 8
	- total weight = 8, allowed

	day 4, add items 9
	- total weight = 9, allowed

	day 5, add item 10
	- total weight = 10, allowed


	WE WERE ABLE TO DO THIS IN 5 DAYS, WITH CAPACITY 15


capacity range
	- minimum -> max value in the array
		- in the above example, if we take anything less than 10
		- we won't be able to do this
		- so minimum weight should be 10
	- maximum -> sum of all the weights in array
		- that way, we can do all this in one day

	- capacir range -> max(arr) and sum(arr)


"""


def fn(weights, capacity):
	days = 1
	load = 0

	for i in range(len(weights)):
		if load + weights[i] > capacity:
			days += 1
			load = weights[i]
		else:
			load += weights[i]
	return days


def brute_force(weights, days):
	for capacity in range(max(weights), sum(weights)+1):
		days_required = fn(weights, capacity)
		if days_required <= days:
			return capacity


def optimized_binary_search(weights, days):
	lo = max(weights)
	hi = sum(weights)
	ans = -1

	while lo <= hi:
		mid = (lo+hi)//2

		days_required = fn(weights, mid)
		if days_required <= days:
			ans = mid
			hi = mid - 1
		else:
			lo = mid + 1
	return ans



weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

print(brute_force(weights, days))
print(optimized_binary_search(weights, days))