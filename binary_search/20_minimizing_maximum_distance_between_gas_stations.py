"""
MINIMIZE MAXIMUM DISTANCE TO GAS STATIONS
-----------------------------------------
* given an array of n integers, representing coordinates of gas stations
* all the coordinates will be in sorted order
* task is to place k new gas stations
* place them in such a way that you minimize the maximum distance between any 2 gas stations
* WE CAN PLACE THEM AT DECIMAL COORDINATES AS WELL

-----------------------------------------
example
-----------------------------------------
arr = [1, 2, 3, 4, 5], k = 4
* place 4 gas stations 

way 1 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    * difference between any 2 consecutive gas stations = 1
        * max distance b/w any 2 consecutive gas stations = 1

way 2 -> [1, 1.25, 1.5, 1.75, 2, 3, 4, 4.5, 5,]
              .     .    .              .
    * differences are varied here:
        * min = 0.25
        * also have 0.5
        * max = 1
    * so the max distance = 1


way 3 -> [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
              x       x       x       x
    * differences = 0.5 for all
    * max = 0.5

    * for this use case, we can't do better than this
    * WE MINIMIZED THE MAXIMUM DISTANCE BETWEEN THE GAS STATIONS


    RETURN ANSWER 0.5
    * return 0.5


-----------------------------------------
example 2
-----------------------------------------
arr = [1, 7], k = 2


approach 1:
    [1, 7, 8, 9]
    * max distance = 6
    * are we reducing the max distance by placing the new stations outside the range?
        * NO, IT DOESN'T MAKE SENCE TO ADD THEM OUTSIDE THE EXTREME
        * LEFT OR RIGHT
        * BECAUSE THE MAX DISTANCE WILL STILL BE AT THE SAME 
        * SO PLACE NEW GAS STATIONS IN BETWEEN THE EXISTING ONES

approach 2:
    arr =     [1, 2, 4, 7]
    distances =  1  2   3

    * max distance = 3

approach 3:
    * we have total distance = 6
    * we need to create 3 spaces between 1 and 7
        * so that all the distances are minimized
    * so total_distance / 3 = 6 / 3 = 2

    ###########################
    * EQUAL SECTORS OF LENGTH 2
    ###########################



    arr =     [1, 3, 5, 7]
    distances =  2  2  2 

    * max distance = 2
    * max distance is minimized now, return 2


    
-----------------------------------------
example 3
-----------------------------------------
arr = [1, 13, 17, 23], k = 5

* we can't place anything to the right and left

* we have 3 sectors where have to place 5 new gas stations
* sector 1 -> 1, 13
* sector 2 -> 13, 17
* sector 3 -> 17, 23

sectors:
    |   |   |   |
      0   1   2


###################################
* let's start with 1 new gas station, where will I place that 1 new station
###################################
* sector 1 ->  1-13 -> distance = 12
* sector 2 -> 13-17 -> distance = 4
* sector 3 -> 17-23 -> distance = 6

* sector 1 is the maximum distance between 2 gas stations
* so place 1 new gas station here

* sector 1 -> 1, 13
* sector 2 -> 13, 17
* sector 3 -> 17, 23

sectors:
    | 1 |   |   |
      0   1   2

* it will look something like this:
    arr = [1, 7, 13, 17, 23]
    dis =   6  6    4   6

###################################
* let's start with 2nd  new gas station, where will I place that 1 new station
###################################
* now the maximum distance = 6
    * so we can place it in between sector 3
    * new max distance in sector 3 = (23 - 17)/(1 + 1) = 3
        * (right - left) / (existing + 1)

it will look like this now:
    arr = [1, 7, 13, 17, 20, 23]
             6  6   4   3   3

sectors:
    | 1 |   | 1 |
      0   1   2


###################################
* let's start with 3rd new gas station, where will i place that 1 new station

    * with the previous configuration, we have this setups:
    arr = [1, 7, 13, 17, 20, 23]
             6  6   4   3   3

sectors:
    | 1 |   | 1 |
      0   1   2

* we need to resolve the max distance = 6
###################################

arr = [1, 13, 17, 23], k = 5

* we now need to place 2 gas stations in sector 1
* distance = 1 and 13
    * |   .   .   |
      1          13
    * distance = 13 - 1 = 12
    * equal distance = 12 / 3 = 4
        * 3 = number of gaps b/w the 1 and 13 gas stations

arr = [1, 5, 9, 13, 17, 20, 23]
        4  4  4    4   3   3

sectors:
    | 2 |   | 1 |
      0   1   2


###################################
* let's start with 4th new gas station, where will i place that 1 new station

    * with the previous configuration, we have this setups:
arr = [1, 5, 9, 13, 17, 20, 23]
        4  4  4    4   3   3

sectors:
    | 2 |   | 1 |
      0   1   2

* we need to resolve the max distance = 4

* we choose the sector 2 for this, and place one gas station there

arr = [1, 5, 9, 13, 15, 17, 20, 23]
        4  4  4    2   2   3   3

sectors:
    | 2 | 1 | 1 |
      0   1   2
###################################



###################################
* let's start with 5th new gas station, where will i place that 1 new station

    * with the previous configuration, we have this setups:
arr = [1, 5, 9, 13, 15, 17, 20, 23]
        4  4  4    2   2   3   3

sectors:
    | 2 | 1 | 1 |
      0   1   2

* in sector 1, we have distances = (13 - 1) / (2 + 1) = 4
* in sector 2, we have distances = (17 - 13) / (1 + 1) = 2
* in sector 3, we have distances = (23 - 17) / (1 + 1) = 3

* we need to reduce the maximum length in sector 1, where max distance = 4

* sector 1:
    1   4   7   10   13   15   17   20   23
        x   x   x         x          x              -> x = placed
      3   3   3    3    2    2    3    3            -> max distance = 3


* so now the max distance = 3, return 3

###################################


watched till 20:50


# CODE SECTION
--------------
* what are we keeping track of:
    * how many were placed between them
    * we are going to place new gas stations one by one


how_many = | | | |

for gas in range(1, k+1):
    # Calculate the max distance between the original gas stations
    maximumValue = -1
    # The index of where the max distance occurs
    maxIdx = -1

    for i in range(0, n-1):
        diff = arr[i+1] - arr[i]
        section_length = diff / (how many are placed in this section + 1)

        if maximumValue < section_length:
            maximumValue = section_length
            maxIdx = i

# When this for loop ends
# We know where is the maximum distance
# Add one more gas station there

how_many[maxIdx] += 1


# Once we have done all the allocation/placement
# now we need to figure out each section's individual length

maxAns = -1
for i in range(0, n-1):
    section_length = (arr[i+1] - arr[i]) / (how_many[i] + 1)
    maxAns = max(maxAns, section_length)

return maxAns

"""
##########################
# BRUTE FORCE SOLUTION
##########################

def striversCode(arr, k):
    n = len(arr)
    how_many = [0 for i in range(n-1)]

    for gasStations in range(1, k+1):
        maxSection = -1
        maxIdx = -1
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            sectionLength = diff / (how_many[i] + 1)

            if sectionLength > maxSection:
                maxSection = sectionLength
                maxIdx = i

        how_many[maxIdx] += 1

    maxAns = -1
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        section_length = diff / (how_many[i] + 1)
        maxAns = max(maxAns, section_length)

    return maxAns

arr = [1, 2, 3, 4, 5]
k = 4
print(striversCode(arr, k))



arr = [1, 7]
k = 2
print(striversCode(arr, k))



arr = [1, 13, 17, 23]
k = 5
print(striversCode(arr, k))

"""
TIME COMPLEXITY -> (k * n) + n
---------------
* This is quadratic in nature


WE NEED TO OPTIMIZE THIS APPROACH

* we can't skip the k for loop
* As we are placing the stations one by one individually

* The O(n) internal loop:
    * it's trying to figure out the max length
    * can we optimize it?
        * Yes
        * by using heap/priority queue


INTRO TO PRIORITY QUEUE
-----------------------
* it's not a linear data structure
* it uses heap internally


pq.push(2) -> log N insertion
pq.push(3) -> log N insertion
pq.push(1) -> log N insertion

we've inserted 3 elements
* pq stores maximum at top, so the pq looks like this:
    |   3   |
    |   2   |
    |   1   |
    ---------

when I do pq.top() -> 3
    * it will return the max one at top (3 in this case)

when we again do pq.top() -> 3
    * it will give 3 again
    * as it will not be removing it


when we do pq.pop() -> 3 will be gone
    * the pop will remove the top element

now when we do pq.top() -> 2
    * because 3 is now not present
    * the max value is 2, which is what it returns

"""


"""
* the inner for loop was O(n)
* to do some optimization
    * we need to go:
        * log N, or
        * O(1) constant time
            * constant time not possible
            * since we need maximum value
            * that can't be done in constant time

* we can do log(N), with priority queue



how_many = [ 0 | 0 | 0 ]
             0   1   2

arr = [1, 13, 17, 23], k = 5


we will itarate over all the sections:
    * calculate distance and the section index:
        section 1 -> (12, 0) -> add in pq
        section 2 -> (4, 1) -> add in pq
        section 3 -> (6, 2) -> add in pq

    * in pq we are storing the length of section, and index of section

    * the pq will look like this:
    |   (12, 0)   |
    |   ( 6, 2)   |
    |   (4, 1)    |
    ---------------


---------------------------------------------
* Now where will I place the 1st gas station
---------------------------------------------
    * we have distances: 12, 6, 4 ( from the pq )
    * we need to reduce the 12

* How many are there at 12: ( 12 / 1 )
* We placed 1 gas station in section 0
* The how many array becomes this:

how_many = [ 1 | 0 | 0 ]
             0   1   2

* After this, the section 0 will be broken down into 2 sections:
    * distance = ( 12 / (1+1) ) = 6
    * so now the distance max in section 0 is 6

    * NOW ADD (6, 0) IN THE PRIORITY QUEUE
    * PQ WILL KEEP (6, 2) AT TOP, AS (6, 0) HAS FIRST VALUE SAME
    * THE SECOND VALUE WILL BE COMPARED, SO THIS WILL PUT
    * (6, 2) AT TOP

* now the pq will look like this:
    |   ( 6, 2)   |
    |   ( 6, 0)   |
    |   ( 4, 1)   |
    ---------------

---------------------------------------------
* Now where will I place the 2nd gas station
---------------------------------------------
* when we now take the max form pq, we get:
    * (6, 2)

* The how many array becomes this:

how_many = [ 1 | 0 | 1 ]
             0   1   2

    * when we place 1 more gas station in section 2
    * now distance = ( 6 / (1+1) ) = 3
    * now third section becomes: (3, 2)
    * add this to the PQ, PQ looks like this:

    |   ( 6, 0)   |
    |   ( 4, 1)   |
    |   ( 3, 2)   |
    ---------------

---------------------------------------------
* Now where will I place the 3rd gas station
---------------------------------------------
* when we now take the max form pq, we get:
    * (6, 0)

* The how many array becomes this:

how_many = [ 2 | 0 | 1 ]
             0   1   2

    * when we place 1 more gas station in section 0
    * now distance = ( 12 / (2+1) ) = 4
        * as 2 gas stations in between idx 0 and 1 in array
        * this results in 3 sections, hence 12/3 = 4
    * now first section becomes: (4, 0)
    * add this to the PQ, PQ looks like this:

    |   ( 4, 1)   |
    |   ( 4, 0)   |
    |   ( 3, 2)   |
    ---------------

---------------------------------------------
* Now where will I place the 4th gas station
---------------------------------------------
* when we now take the max form pq, we get:
    * (4, 1)

* The how many array becomes this:

how_many = [ 2 | 1 | 1 ]
             0   1   2

    * when we place 1 more gas station in section 1
    * now distance = ( 4 / (1+1) ) = 2
        * as 1 gas stations in between idx 1 and 2 in array
        * this results in 2 sections, hence 4/2 = 2
    * now second section becomes: (2, 1)
    * add this to the PQ, PQ looks like this:

    |   ( 4, 0)   |
    |   ( 3, 2)   |
    |   ( 2, 1)   |
    ---------------

---------------------------------------------
* Now where will I place the 5th gas station
---------------------------------------------
* when we now take the max form pq, we get:
    * (4, 0)

* The how many array becomes this:

how_many = [ 3 | 1 | 1 ]
             0   1   2

    * when we place 1 more gas station in section 0
    * now distance = ( 12 / (3+1) ) = 3
        * as 3 gas stations in between idx 0 and 1 in array
        * this results in 4 sections, hence 12/4 = 3
    * now second section becomes: (3, 0)
    * add this to the PQ, PQ looks like this:

    |   ( 3, 2)   |
    |   ( 3, 0)   | 
    |   ( 2, 1)   |
    ---------------
"""

import heapq

def heap(arr, k):
    n = len(arr)

    # Array to store how many gas stations are placed in each section
    how_many = [0] * (n-1)

    # Min heap to store sections by their current maximum distance
    pq = []

    # Insert first n-1 elements into priority queue with respective distance values
    for i in range(n-1):
        heapq.heappush(pq, (-float(arr[i+1] - arr[i]), i))
    
    for gasStations in range(1, k+1):
        # Find maximum section and insert the gas station
        neg_dist, secIdx = heapq.heappop(pq)

        # Get the section with maximum distance
        max_dist = -neg_dist

        # Insert current gas station into section
        how_many[secIdx] += 1

        # Calculate the initial difference between adjacent gas stations
        inidiff = float(arr[secIdx + 1] - arr[secIdx])
        # Calculate the new section length after inserting another gas station
        newSecLen = inidiff / (how_many[secIdx] + 1)
        # Push the updated section back into the priority queue
        heapq.heappush(pq, (-newSecLen, secIdx))
    
    # Return the maximum distance in the top section of the heap
    return -pq[0][0]

print("heap solution")
arr = [1, 2, 3, 4, 5]
k = 4
print(heap(arr, k))

arr = [1, 7]
k = 2
print(heap(arr, k))

arr = [1, 13, 17, 23]
k = 5
print(heap(arr, k))


"""
time complexity -> n * log(n) + k * long(n)
    * first loop + second loop
space complexity -> O(n-1)
    * always keeping (n-1) objects


SOME INTERVIEWERS MAY STILL NEED AN OPTIMAL SOLUTION
* TO OPTIMIZE SPACE COMPLEXITY EVEN FURTHER
* THAT IS THE OPTIMAL SOLUTION, DISCUSSED BELOW


what we need to do:
    * minimize the maximum distance between gas stations
    * whenever we have something like this
        * minimize the maximum distance
        * BINARY SEARCH COMES INTO PICTURE

so far we did this:
    while lo <= hi:

        # something happens
        lo = mid + 1

        # something happens
        hi = mid - 1

    * this won't work here
    * since we can't do +1 or -1 as we will loose a lot of things
    * also we can't do +0.0001 or -0.0001
        * this will take up a lot of time

        * THE PATTERN CHANGES HERE FOR THE BINARY SEARCH APPROACH
"""

# NEW PATTERN
"""
while (hi - lo > 10**(-6)):

    # something happens
    lo = mid

    # something happens
    hi = mid

    # we will not be incrementing/decrementing lo/hi




what we did so far:


while ():

    check()

    if check():
        lo = mid + 1 
    else:
        hi = mid - 1

# now we won't do:
    lo = mid + 1
    OR
    hi = mid - 1


* it will look like something below:


while ():

    check()

    if check():
        lo = mid
    else:
        hi = mid

* NOW WE NEED TO IDENTIFY WHAT WE NEED TO ---> CHECK()
"""



"""
SOLUTION APPROACH
=================

arr = [1, 2, 3, 4, 5], k = 4


############
############
Point 1: We need the range
############
############

For all the binary search problems so far, we need the range:
    It can be from: [ 0 , 1 ]

        * 0 -> we can place gas station at same coordinate
        * 1 -> maximum distance between all the available gas stations


############
############
Point 2: What we need to check on
############
############

# when we were doing linear search, this is what we did
# we need to check what we need to check

# previously we did linear search:
    * we go from 0, 1, 2, 3, ....
# now we will need to do this:
    for (dist=0; dist <= 1; dist += 10^-6)
    * each time we will increase it by 10^-6


for the sake of understanding, let's take the step value to be 0.1:

    0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0


attempt 1:
===========
* If we keep a distance of zero (0), how many gas stations will I be able to place:
    * we will need to place infinite gas stations
    * in order to make sure the distance doesn't exceed zero

    * it's not possible to do this with 4 gas stations
        * since we only have 4 new gas stations



attempt 2: distance = 0.1
===========
* If we keep a distance of 0.1, how many gas stations will I be able to place:
    * it will be like this:
        1.1 - 1.2 - 1.3 - 1.4 - 1.5
    * so we don't have enough gas stations


same will happen for distance = 0.2, 0.3, 0.4

attempt 5: 
===========
* if we keep a distance of 0.5, we will have:
    arr = [1   2   3   4   5]
            1.5 2.5 3.5 4.5

    * we need exactly 4 gas stations
    * so it's possible 

    * WE CAN ELIMINATE THE RIGHT SIDE
        * ANYTHING GREATER THAN 0.5 CAN BE IGNORED

    * WE CAN LOOK LEFT

* actually anything beyond 0.5 will also give us 4 gas stations
    * like 0.6:
        1.6, 2.6, 3.6, 4.6
    * and same with 0.7, 0.8, 0.9

* BUT WE NEED MINIMUM, SO WE LOOK LEFT OF THESE VALUES
* AND LAND ON 0.5


the pattern is:

    x x x x x x x o o o o o o o 
    |           |
    -------------
         |
    on the left section, we 
    have more no. of gas stations
    required to adjust to the distance gap
                   |            |
                   |            |
                   |------------|
                          |
                on the right section, we need less no. of gas
                stations to fill up the space between the gas
                stations


* on the left: 
    * no. of gas stations required > k
    * we need to increase the distance b/w gas stations

* on the right:
    * no. of gas stations required < k
    * we need to decrease the gas stations

* if something satisfies the condition of
    * no. of gas stations required = k
    * we still look left
    * as we need minimum value for this maximum distance b/w
        gas stations



##################
HOW TO FIGURE OUT HOW MANY GAS STATIONS WE ACTUALLY NEED
##################

example:

arr = [1  2  3  4  5], k = 4

for distance = 0.4
------------------
we will have:
    1  1.4  1.8  2 2.4 2.8 3

* how to figure out how many number of gas stations we can fit between any 2 gas stations:
    (right - left) / distance

example:
    (2 - 1) / 0.4 = 2.5
    * we remove the decimal part
    * basically take integer division = 2


but for distance = 0.5, it will be:
    (2 - 1) / 0.5 = 2
    * we can place 2
    * BUT THIS IS WRONG
    * SO WE NEED ONE EXTRA LOGIC
        * IF WE HAVE COMPLETE DIVISION WITH ANY DISTANCE VALUE
        * THAT MEANS WE CAN PLACE ONE LESS
        * FOR THIS EXAMPLE OF DISTANCE = 0.5
        * WE CAN ONLY PLACE 1




# CODE FOR THIS APPROACH
========================

lo = 0
hi = maximum of consecutive differences
ans = -1


while (hi - lo > 10**(-6)):
    mid = (lo + hi) // 2

    # count of gas stations required to maintain this gas station distance (mid)
    count = count of gas stations required ( arr, mid )

    if count > k:
        # not possible
        # look right
        # eliminate the left half
        lo = mid
    else:
        # possible
        # look left
        # eliminate the right half
        # and store the answer

        ans = mid
        hi = mid

    return ans or hi (both will be same)


"""
def no_of_gas_stations_required(dist, arr):
    """
    Function to calculate the number of gas stations
    required for a given distance
    """
    n = len(arr)
    cnt = 0
    for i in range(1, n):
        # Calculate the number of gas stations
        # needed between two pointers
        number_in_between = (arr[i] - arr[i-1]) / dist

        # Adjust if exact distance fits perfectly
        if (arr[i] - arr[i-1]) == (dist * int(number_in_between)):
            number_in_between -= 1

        cnt += int(number_in_between)
    return cnt


def minimise_max_distance(arr, k):
    """
    Function to minimize the maximum distance
    between gas stations
    """
    n = len(arr)
    lo = 0
    hi = 0
    ans = -1

    # Find the maximum distance b/w consecutive gas stations
    for i in range(n-1):
        hi = max(hi, arr[i+1] - arr[i])


    # apply binary search to find the minimum
    # possible maximum distance
    diff = 1e-6
    while hi - lo > diff:
        mid = (lo+hi) / 2.0
        cnt = no_of_gas_stations_required(mid, arr)

        # Adjust the search range based on number of
        # gas stations required
        if cnt > k:
            lo = mid
        else:
            ans = mid
            hi = mid

    # Return the smallest maximum distance
    #return hi
    return ans


print("FINAL OPTIMIZED SOLUTION")
arr = [1, 2, 3, 4, 5]
k = 4

print(minimise_max_distance(arr, k), "expected to be 0.5")
