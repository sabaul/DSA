"""
######################################
MINIMUM NO. OF DAYS TO MAKE M BOUQUETS
######################################

    * given an array bloom_day, which states which flower will be blooming on which day
        * e.g. the 0th flower will bloom on 7th day in the array below
        * 4th flower will bloom on 13th day

    * what is the min. no. of days you require, such that you have
    ample amount of blooming flowers, to make m bouquets and you should
    have taken k adjacent flowers to have 1 bouquet

######################################

bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2 -> no. of bouquets
k = 3 -> adjacent flowers required

* imagine all flowers would have bloomed
    * this would only happen on the 13th day
        * all the flowers will be bloomed on the 13th day
    * what we need to make is:
        * make 2 bouquets, each of 3 flowers
        * we can take any 3 adjacent flowers to make a bouquet

    * so in this scenario, the answer will be day 13
        * where we can make 2 bouquets, each with 3 adjacent flowers

    * so 13 day is a possible answer
        * but question states, find minimum no. of days


* imagine we take the 7th day
bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
bloomed  = [x  x  x  x              x]

only flowers with x would have bloomed on day 7
    * so with this condition, we can only make 1 bouquet
    * only 1 scenario where we can make 1 bouquet on the left side

    * so day=7, not a possible answer




* imagine we take the 12th day
bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
bloomed  = [x  x  x  x       x   x  x]


only flowers with x would have bloomed on day 12

    * now we can make 2 bouquets
    * bouquet 1 -> [0, 1, 2]
    * bouquet 2 -> [5, 6, 7]

    * so day = 12, is a possible solution,
    * can we do better?? reduce the number of days



* imagine we take the 11th day
bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
bloomed  = [x  x  x  x       x      x]


only flowers with x would have bloomed on day 12
    * we can only make 1 bouquet
    * we can't make another bouquet with 3 adjacent flowers
    * 11th day is not a possible solution


we have a pattern:
    day1 day2 day3 ..... day10 day11 day12 day13
    np   np   np   ..... np    np    p     p

    here np -> not possible
          p -> possible

    day 1 to 11 -> nothing is possible
    day 12 to 13 -> both are possible answer
        * minimum possible would be 12 --> FINAL ANSWER

===============================================================
ANOTHER EXAMPLE
===============================================================


bloomDay = [1, 10, 3, 10, 2]
m = 3 -> 3 bouquets
k = 2 -> 2 flowers adjacent

here even if we take the 10th day
    * all the flowers would have bloomed
    * but at max we can make 2 bouquets
        * as we need 3 bouquets, not possible


return -1 as it's not possible with given inputs


===============================================================


===============================================================
brute force for the above question:
===============================================================

bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2 -> no. of bouquets
k = 3 -> adjacent flowers required


    * not possible condition:
        if m * k > n, where n is the length of the array
        return -1

        * other than this condition, everything would work

* what is the maximum answer: day 13, as everything will be bloomed
    * so we can pick any 2 bouquets with 3 adjacent values

* since we need the minimum possible answer
    * 1 day, 2 day, 3 day .... [min day to bloom in array]
    * so to altest bloom one flower
        * we need the min(array)


* so range will be: 7 to 13
    * 7 -> minimum value in array
    * 13 -> max value in array
        * between 7 and 13 will be our answer


* for day = 7, check how many flowers are bloomed
    * how many bouquets can we make?
        * only 1
        * not possible

* for day = 8, check how many flowers are bloomed
    * how many bouquets can we make?
        * only 1
        * not possible

* for day = 9, check how many flowers are bloomed
    * how many bouquets can we make?
        * only 1
        * not possible

* for day = 10, check how many flowers are bloomed
    * how many bouquets can we make?
        * only 1
        * not possible

* for day = 11, check how many flowers are bloomed
bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
bloomed  = [x  x  x  x       x      x

    counter = 1 2 3 4 [ the first 4], then find a non-bloom flowers
    NO. OF BOUQUETS SO FAR: 4//3 = 1

    counter = 1 2 3 4 0 1 
    NO. OF BOUQUETS AT THE END: 1 // 3 = 0

    counter = 1 2 3 4 0 1 0 1
    NO. OF BOUQUETS AT THE END: 1 // 3 = 0

    total bouquets: 1
        * day 11 is also not possible




* for day = 12, check how many flowers are bloomed
bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
bloomed  = [x  x  x  x       x   x  x

    counter = 1 2 3 4 [ the first 4], then find a non-bloom flowers
    NO. OF BOUQUETS SO FAR: 4//3 = 1

    counter = 1 2 3 4 0 1 2 3 
    NO. OF BOUQUETS AT THE END: 3 // 3 = 1

    total bouquets: 2
        * this is the required number of bouquets
        * day 12 is possible

    * this is the minimum number, return 12


#####################################
let's write the function that gives us the answer if it's possible or not to get the bouquets

#####################################

def possible(arr, days, m, k):
    counter = 0
    num_bouquets = 0
    for i in range(len(arr)):
      if arr[i] <= days:
        # blooming is possible
        counter += 1
      else:
        num_bouquets += counter//k
        counter = 0

    num_bouquets += counter//k

    if num_bouquets >= m:
      return True # if possible
    return False # if not possible

# we know the range [min(arr), max(arr)]

def check(arr, m, k):
    if n < m * k:
        return -1
    for i in range(min(arr), max(arr)+1):
        if possible(arr, i, m, k):
            return i
    return -1


#############################################
time complexity for brute force:
    * TC: (max(arr) - min(arr)) * N

#############################################


CAN WE OPTIMIZE THIS:
    * WE HAVE THE RANGE:
    [ 7 8 9 10 11 12 13 ]
      x x x  x  x  o  o

    * we go from the range of not possible to possible

* we can do binary search here


def binary_search(arr, m, k):
    if m * k > len(arr):
        return -1

    lo = min(arr)
    hi = max(arr)
    ans = float('inf')

    while lo <= hi:
        mid = (lo+hi)//2

        if possible(arr, mid, m, k):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


"""


def possible(arr, days, m, k):
    counter = 0
    num_bouquets = 0
    for i in range(len(arr)):
      if arr[i] <= days:
        # blooming is possible
        counter += 1
      else:
        num_bouquets += counter//k
        counter = 0

    num_bouquets += counter//k

    if num_bouquets >= m:
      return True # if possible
    return False # if not possible

def bruteforce(arr, m, k):
    if len(arr) < m * k:
        return -1
    for i in range(min(arr), max(arr)+1):
        if possible(arr, i, m, k):
            return i
    return -1


def binary_search(arr, m, k):
    if m * k > len(arr):
        return -1

    lo = min(arr)
    hi = max(arr)
    ans = float('inf')

    while lo <= hi:
        mid = (lo+hi)//2

        if possible(arr, mid, m, k):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2# -> no. of bouquets
k = 3# -> adjacent flowers required


print(binary_search(bloomDay, m, k))
print(bruteforce(bloomDay, m, k))
