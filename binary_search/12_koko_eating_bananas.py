"""
###################################################
KOKO EATING BANANAS
    * return the minimum integer k such that koko can eat all bananas within h hours
    * k = bananas / hour
###################################################


piles = [3, 6, 7, 11], h = 8

for k = 2
    * no. of hours for pile 1 = 2 hours for 3 bananas
    * ..................... 2 = 3 hours for 6 bananas
    * ..................... 3 = 4 hours for 7 bananas
    * ..................... 4 = 6 hours for 11 bananas
    * total time taken to eat all bananas = 15 hours
    * but we have only 8 max hours
    * so k = 2 won't work, NOT POSSIBLE

for k = 3
    * no. of hours for pile 1 = 1 hours for 3 bananas
    * ..................... 2 = 2 hours for 6 bananas
    * ..................... 3 = 3 hours for 7 bananas
    * ..................... 4 = 4 hours for 11 bananas
    * total time taken to eat all bananas = 10 hours
    * but we have only 8 max hours
    * so k = 3 won't work, NOT POSSIBLE
    
for k = 4
    * no. of hours for pile 1 = 1 hours for 3 bananas
    * ..................... 2 = 2 hours for 6 bananas
    * ..................... 3 = 2 hours for 7 bananas
    * ..................... 4 = 3 hours for 11 bananas
    * total time taken to eat all bananas = 8 hours
    * but we have only 8 max hours
    * so k = 4 works, POSSIBLE ANSWER
        * k = 5 will also work
        * k = 6, 7, 8 all of them will work
        * SINCE we're looking for MINIMUM THE ANSWER is 4


BRUTE FORCE:
    * start with 1 banana/hour
        * calculate total time
        * check with the total time that we have
        * if works, stop, otherwise proceed next number one by one
    
    * repeat till it works as a possible solution

    * what can be the maximum value for this range
        * for n bananas/hr 
        * max bananas in any lot (max of the array)
            * this will determine the max value for the range
            * because the mininum time taken would be the length of array when we take the max value of array
                * as time taken for each bin would be 1
                * so total time = len(array)
                    * for max value eating = max(array)



def func(arr, hourly_rate):
    total_hrs = 0
    for i in range(len(arr)):
      total_hrs += ceil(arr[i]/hourly_rate)
    return total_hrs


def f(array):
    for i in range(1, max(array)):
      req_time = func(arr, i)
      if req_time <= h:
        return i
    return -1

time complexity: O(max(arr) * n)
    * max(arr) because the for loop is running for max(array)
    * n -> as each time we're going across the piles of bananas




#################
PATTERN HERE:
#################
    * WE KNOW THE RANGE
        * RANGE = 1 to max(array)
    * we have a pattern like this, for all the possible answers in number line:
        1 2 3 4 5 6 7 8 9 10 11 12
        x x x o o o o o o o o o o 

        till 3 -> not possible
        after 3 -> possible answers

        pattern: NOT POSSIBLE to POSSIBLE

    * SO WE CAN USE BINARY SEARCH HERE
    * replace LINEAR SEARCH WITH BINARY SEARCH

------------------------------------------------------------------

time complexity: O(log(max(arr)) * n)
"""
import math

def calculate_time(arr, hourly_rate):
    total_time = 0
    for i in range(len(arr)):
        total_time += math.ceil(arr[i]/hourly_rate)
    return total_time

def brute_force(arr, h):
    for hourly_rate in range(1, max(arr)+1):
        time_req = calculate_time(arr, hourly_rate)
        if time_req <= h:
            return hourly_rate
    return -1

def binary_search(arr, h):
    lo, hi = 1, max(arr)
    ans = -1

    while lo <= hi:
        mid = (lo+hi)//2

        time_req = calculate_time(arr, mid)

        if time_req <= h:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


arr = [3, 6, 7, 11]
h = 8

print(f"Brute Force: {brute_force(arr, h)}")
print(f"Binary Search: {binary_search(arr, h)}")
