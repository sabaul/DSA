"""
==========================================
MEDIAN OF TWO SORTED ARRAYS

* the arrays can be of equal size or they can be of different size
* but they are sorted arrays
==========================================


==========================================
Example 1:
==========================================

arr1 = [1, 3, 4, 7, 10, 12]  ---  arr2 = [2, 3, 6, 15]
n1 = 6                            n2 = 4

PROCEDURE TO SOLVE:
-------------------
step 1: Combine the sorted arrays

    arr = [1, 2, 3, 3, 4, 6, 7, 10, 12, 15], n = 10 (as n1 + n2 = 10)
           0  1  2  3  4  5  6   7   8   9


For array size of 10, can we find median?
    * NO
    * if we select 4 -> on the left, we have 4 elements, on right we have 5
    * if we select 6 -> on the left, we have 5 elements, on right we have 4


==========================================
so there are no specific median
As MEDIAN means:
    * on the left and on the right, we should have equal number of elements
==========================================

* So we need something between 4 and 6
* Then we will have 5 on the left and 5 on the right

So the median will be middle of 4 and 6:
    (4 + 6) // 2 = 5

    * 5 will be the median



==========================================
Example 2:
==========================================


arr1 = [2, 3, 4], arr2 = [1, 3]
n1 = 3            n2 = 2


    arr = [1, 2, 3, 3, 4]
    n = 5 -> total number of elements


median = 3
    * 2 elements on left, 2 elements on right
    SOLVED


* FOR EVEN -> CONSIDER 2 ELEMENTS, TAKE MIDDLE OF IT
    * (n // 2)
    * (n // 2) - 1

* FOR ODD -> TAKE THE MIDDLE ELEMENT
    * n // 2 -> where n = length of the array
"""


"""
BRUTE APPROACH
--------------
* Merge the two sorted arrays into a third sorted arrays
* Take the middle of it

* Merge sorted algorithm part


example 1:
    arr = [1, 2, 3, 3, 4, 6, 7, 10, 12, 15]
    n = 10

    * if total number of elements is even
    * we will have 2 median elements
    * median = (4 + 6)//2 = 5
        * index will be -> 4 and 5
        * which is (10//2) and (10//2 - 1)


arr1 = [1, 2, 3, 7, 10, 12]
n1 = 6
i -> the index used to iterate over arr1

arr2 = [2, 3, 6, 5]
n2 = 4
j => the index used to iterate over arr2


i = 0
j = 0

while (i < n1 and j < n2):

    if arr1[i] < arr2[j]:
        arr3.append(arr1[i)
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

while i < n1:
    arr3.append(arr1[i])
    i += 1

while j < n2:
    arr3.append(arr2[j])
    j += 1

# At this point of time, arr3 is the combined sorted array
# now we need to find the median
n = n1 + n2

if n % 2 == 1:
    # n is odd
    # median will be at arr3[n // 2]
    return arr3[n // 2]
else:
    # median will be 2 positions
    # n//2 and (n//2 - 1)
    return (arr3[n//2] + arr3[n//2 - 1]) / 2



# TIME COMPLEXITY -> O (n1 + n2)
# SPACE COMPLEXITY -> O (n1 + n2)


# WE NEED TO DO BETTER
# FIRST WE WILL OPTIMIZE THE SPACE
"""






"""
BETTER APPROACH
    * SPACE OPTIMIZATION
--------------
    * DO WE NEED TO STORE ALL THE ELEMENTS??
    arr = [1, 2, 3, 3, 4, 6, 7, 10, 12, 15]
        * CAN WE STORE ONLY THE 4 & 6 FOR THE EVEN arr3 example
    arr = [1, 2, 3, 3, 4]
        * CAN WE STORE ONLY THE 3 FOR THE ODD arr3 example

What we did previously:
    * we merged both the sorted arrays first
    * to get the arr3
    * then we checked for the final length "n"
        * to check if it's even or odd


For this even size array::
    arr = [1, 2, 3, 3, 4, 6, 7, 10, 12, 15]
           0  1  2  3  4  5  6   7   8   9
                       ^  ^
                       |  |
                    idx1  idx2


    n = 10
    * first element is element at index idx1 = 4
    * second element is element at index idx2 = 5
    * which is nothing but the idx2 = n//2 and idx1 = (n//2 - 1)
    * return mean of element at idx1 and idx2
        * return (ele1 + ele2) / 2


For this odd size array::
    arr = [1, 2, 3, 3, 4]
           0  1  2  3  4 
                 ^
                 |
                 idx2


    n = 5
    * second element is element at index idx2 = 2
    * which is nothing but the idx2 = n//2 
    * return element at idx2
        * return ele2


#########################################################
arr1 = [1, 2, 3, 7, 10, 12]
n1 = 6
i -> the index used to iterate over arr1

arr2 = [2, 3, 6, 5]
n2 = 4
j => the index used to iterate over arr2


keep a count, which will track the elements required
count will store the idx1 and idx2
when we get to the elements at index idx1 and idx2
store these elements

since it's even size (n1 + n2)
* return mean of (ele1 + ele2) / 2


"""

def better(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    n = n1 + n2

    # Required indices for median calculation
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1

    # Apply the merge step
    i, j = 0, 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if cnt == ind1:
                ind1el = arr1[i]
            if cnt == ind2:
                ind2el = arr1[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = arr2[j]
            if cnt == ind2:
                ind2el = arr2[j]
            cnt += 1
            j += 1

    # Process the remaining elements of the unfinished array
    while i < n1:
        if cnt == ind1:
            ind1el = arr1[i]
        if cnt == ind2:
            ind2el = arr1[i]
        cnt += 1
        i += 1

    while j < n2:
        if cnt == ind1:
            ind1el = arr2[j]
        if cnt == ind2:
            ind2el = arr2[j]
        cnt += 1
        j += 1

    # Find the median
    if n % 2 == 1:
        return float(ind2el)

    return float((ind1el + ind2el) / 2)

arr1 = [1, 2, 3, 7, 10, 12]
arr2 = [2, 3, 6, 5]
print(better(arr1, arr2))

arr1 = [2, 4, 6]
arr2 = [1, 3]
print(better(arr1, arr2))




class better:
    #Function to find the median of two sorted arrays.
    def median(self, arr1, arr2):
        # Size of two given arrays
        n1, n2 = len(arr1), len(arr2)
        n = n1 + n2  # Total size

        # Required indices for median calculation
        ind2 = n // 2
        ind1 = ind2 - 1
        cnt = 0
        ind1el, ind2el = -1, -1

        # Apply the merge step
        i, j = 0, 0
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                if cnt == ind1:
                    ind1el = arr1[i]
                if cnt == ind2:
                    ind2el = arr1[i]
                cnt += 1
                i += 1
            else:
                if cnt == ind1:
                    ind1el = arr2[j]
                if cnt == ind2:
                    ind2el = arr2[j]
                cnt += 1
                j += 1

        # Process the remaining elements of the unfinished array
        while i < n1:
            if cnt == ind1:
                ind1el = arr1[i]
            if cnt == ind2:
                ind2el = arr1[i]
            cnt += 1
            i += 1
        while j < n2:
            if cnt == ind1:
                ind1el = arr2[j]
            if cnt == ind2:
                ind2el = arr2[j]
            cnt += 1
            j += 1

        # Find the median
        if n % 2 == 1:
            return float(ind2el)

        return float((ind1el + ind2el) / 2)

if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]

    # Create an instance of the better class
    sol = better()

    # Print the median of the two sorted arrays
    print(f"The median of two sorted arrays is {sol.median(a, b)}")




"""
OPTIMAL SOLUTION -> BINARY SEARCH
########################################
* The brute and better solution were linear in time
    * O(n1 + n2)


* Since they were already linear
* The next improvement can be done with the binary search
    * as we also have sorted array



########################################
EXAMPLE
########################################

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

n1 = 6   --- n2 = 4
n = 10
    * even number of elements


The combined array looks like this:

                     |
arr = [1, 2, 3, 3, 4 | 6, 7, 10, 12, 15]
                     |

in the left half:
    3 elements from arr1, 2 elements from arr2

in the right half:
    3 elements from arr1, 2 elements from arr2


if we can formulate the correct left and right half
we can do the binary search approach


########################################
This is how we can do that:
########################################

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]
                     |
arr = [1, 2, 3, 3, 4 | 6, 7, 10, 12, 15]
                     |

Assume we have formulated the correct left + right half
The median will be: (4 + 6)/2 = 5

What we need in the correct left half:
    3 elements from arr1, 2 elements from arr2


* if we pick up zero elements from arr1:
    and take all 4 elements from arr2
    we still won't be able to make the left half
    as we need 5 elements in the left half

* if we pick up one element from arr1 (the first):
    we need to pick up 4 elements from arr2
    the left half will look like:

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]
                     |
arr = [       1      | 3, 4, 7, 10, 12]
           2 3 6 15  |
                     |

    This is not a valid configuration, because if we sort it out, we get:

                   |
        1 2 3 6 15 | 3 4 7 10 12
                   |
    This is not a sorted array
    as 15 > 3



* if we pick up two element from arr1 (the first):
    we need to pick up 3 elements from arr2
    the left half will look like:

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]
                     |
arr = [     1 3      | 4, 7, 10, 12]
           2 3 6     | 15
                     |

    This is not a valid configuration, because if we sort it out, we get:
        in sorted order

                   |
        1 2 3 3 6  | 4 7 10 12 15
                   |
    This is not a sorted array
    as 6 > 4



* if we pick up three element from arr1 (the first):
    we need to pick up 2 elements from arr2
    the left half will look like:

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]
                     |
arr = [     1 3 4    |  7, 10, 12]
           2 3       |  6, 15
                     |

    This is not a valid configuration, because if we sort it out, we get:
        in sorted order

                   |
        1 2 3 3 4  | 6 7 10 12 15
                   |
    This is a VALID SPLIT
    THIS IS IN SORTED ORDER 


    If we take 3 from arr1 and 2 from arr2
    We get a valid symmetry


* we can try picking 4 elements from arr1 and 1 from arr2:
    it won't work


THERE WILL ALWAYS BE ONLY ONE VALID SYMMETRY



################################
HOW TO FIGURE OUT THAT IT'S VALID SYMMETRY OR NOT?
################################

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

* Imagine we pick 4 from arr1, 1 from arr2:
    this is what it will look like:

                     |
arr = [ 1, 3, 4, 7   | 10, 12]
           2         | 3 6 15
                     |

    * top is the arr1
    * bottom is arr2

################################
    How to determine, if it's a valid symmetry or not??
################################
    * we know top = arr1, is sorted
    * bottom = arr2, is also sorted

    In order for this to be a valid symmetry:
        * 7 at top left section rightmost, should be smaller than the 3 (right bottom leftmost)
            * which is not the case
        * 2 (bottom left rightmost) should be smaller than 10 (top right side leftmost)
            * which is not valid

    This is not a valid configuration

==================================
==================================
==================================
==================================

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

* Imagine we pick 3 from arr1, 2 from arr2:
    this is what it will look like:

                     |
arr = [ 1, 3, 4      | 7, 10, 12]
           2 3       | 6 15
                     |

    * top is the arr1
    * bottom is arr2

################################
    How to determine, if it's a valid symmetry or not??
################################
    * we know top = arr1, is sorted
    * bottom = arr2, is also sorted

    In order for this to be a valid symmetry:
        * 4 at top left section rightmost, should be smaller than the 6 (right bottom leftmost)
            * which is valid 
        * 3 (bottom left rightmost) should be smaller than 7 (top right side leftmost)
            * which is valid

    This is a valid configuration
    Hence SYMMETRY


==================================
==================================
==================================
==================================

arr1 = [1, 2, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

* Imagine we pick 2 from arr1, 3 from arr2:
    this is what it will look like:

                     |
arr = [ 1, 3         | 4, 7, 10, 12]
           2 3 6     | 15
                     |

    * top is the arr1
    * bottom is arr2

################################
    How to determine, if it's a valid symmetry or not??
################################
    * we know top = arr1, is sorted
    * bottom = arr2, is also sorted

    In order for this to be a valid symmetry:
        * 3 at top left section rightmost, should be smaller than the 15 (right bottom leftmost)
            * which is valid 
        * 6 (bottom left rightmost) should be smaller than 4 (top right side leftmost)
            * which is not valid

    This is NOT a valid configuration
    Hence NOT SYMMETRY


###################################
###################################

TWO POINTS TO KEEP IN MIND:
    1. BINARY SEARCH WILL BE BASED ON SYMMETRY
        WHERE WE FIGURE OUT, HOW MANY FROM ARRAY WILL BE ON LEFT
                             HOW MANY FROM ARRAY WILL BE ON RIGHT
    2. HOW TO DETERMINE IF IT'S A VALID OR INVALID SYMMETRY
    3. THIS IS HOW WE FIGURE OUT THE MEDIAN ????

###################################
###################################
"""
