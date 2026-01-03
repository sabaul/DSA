"""
######################################
FIND THE SMALLEST DIVISOR GIVEN A THRESHOLD

    * Given an array of integers and a threshold value
    * find the smallest divisor such that
        * when you divide each individual value with it
        * take the ceil of each value
        * sum them up
            * the sum total should be less than equal to the THRESHOLD VALUE
######################################

e.g.

arr = [1, 2, 5, 9], threshold = 6

    * take divisor = 4
        * 1/4 = 1
        * 2/4 = 1
        * 5/4 = 2
        * 9/4 = 3
            * sum total = 1+1+2+3 = 7 is not <= 6 [threshold]
        * divisor=4, cannot be our answer


    * take divisor = 5
        * 1/5 = 1
        * 2/5 = 1
        * 5/5 = 1
        * 9/5 = 2
            * sum total = 1+1+1+2 = 5 is not <= 6 [threshold]
        * divisor=5, can be our answer

    * divisor = 6 will also be an answer
        * and so on
        * divisor = 7, 8, ..... will also be an answer
        * since we need the smallest
        * divisor = 5 will be our answer


----------------------------------------
BRUTE FORCE
----------------------------------------
* start from 1 and do the division+ceil+summation <= threshold
    * if it satisfies the condition, return
    * if not, increase the value and check till we find the divisor
        * increase from 1 -> 2 -> 3 -> 4

* but what is the range: where to start and stop
    * we can't start with a number smaller than 1
        * we can't divide anything by zero
    * anything greater than max(arr) will still give us the total summation as len(arr)
        * e.g: arr = [1, 2, 5, 9], threshold=6
            * if divisor = 100
            * 1/100 + 2/100 + 5/100 + 9/100 = 1+1+1+1 = 4 = size of array
            * this is the minimum total sum after division
        * so the max value can be the max(arr)

    * so we have the range from 1 to max(arr)
    * RANGE = [1, max(arr)]


* TIME COMPLEXITY: MAX(ARR) * N
* SPACE: O(1)



def brute_force(arr, threshold):
    for divisor in range(1, max(arr)+1):
        summation = 0
        for i in range(len(arr)):
            summation += math.ceil(arr[i]/divisor)
        if summation <= threshold:
            return divisor
    return -1




-----------------------------------------------
OPTIMIZATION
-----------------------------------------------
* we have a range: 1 to max(arr)
* we have a pattern: x x x x x o o o o 
    * where x -> not possible 
    * where o -> possible

    * and we have to search from the range

* WE CAN USE BINARY SEARCH
* just replace the initial linear search in the range with BINARY SEARCH

* time complexity: log(max(arr)) * N
    * where N -> size of array
* space complexity: O(1)


=============================
EDGE CASE
=============================
* if it can't have a divisor
* the minimum sum after division can be n
    * where n - size of the array

* if n > threshold: return -1
    * because it won't be possible to return a divisor that satisfies the condition



"""

import math

def brute_force(arr, threshold):
    for divisor in range(1, max(arr)+1):
        summation = 0
        for i in range(len(arr)):
            summation += math.ceil(arr[i]/divisor)
        if summation <= threshold:
            return divisor
    return -1


def summation(arr, divisor):
    summation = 0
    for i in range(len(arr)):
        summation += math.ceil(arr[i]/divisor)
    return summation


def binary_search(arr, threshold):
    if len(arr) > threshold:
        return -1

    lo = 1
    hi = max(arr)
    ans = float('inf')

    while lo <= hi:
        mid = (lo+hi)//2

        current_summation = summation(arr, mid)
        if current_summation <= threshold:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


arr = [1, 2, 5, 9]
threshold = 6

print(brute_force(arr, threshold))
print(binary_search(arr, threshold))
