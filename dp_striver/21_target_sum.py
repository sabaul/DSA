"""
TARGET SUM
==========

Given an **arr** of size **n** and a **target**.
Assign signs to all the numbers (+ve/-ve) and count in how many ways can
you achieve the given target.

arr = [1, 2, 3, 1]
target = 3

ways for above arr:
-, +, +, - = 3 --> 5 - 2 = 3
+, -, +, + = 3 --> 5 - 2 = 3
so Answer for above arr and target = 2 ways

----------------------------------------------------

what we did: assigned +ve sign to a subset say s1
			 and assigned -ve sign to a subset say s2

and s1 - s2 = target


we have already solved a problem which is something like this:
			[ arr ]
		   /       \
	 [ s1 ]         [ s2 ]

	 s1 - s2 = d
	 -> count these many guys
	 -> IT BECOMES THE DP QUESTION 18

-----------------------------------------------------

Now the question becomes:
Divide given input array into two subsets such that the difference is target.

i.e. [s1 - s2 = target] -> count no. of ways this can be achieved.

totalSum - s2 - s2 = target
s2 = (totalSum - target)//2




s1 - s2 = t
s1 + s2 = totalSum
------------------ add these two
2*s1 = (totalSum + t)//2

   =================
+++JUST SOME ALGEBRA+++
   =================
s1 + s2 = totalSum
(totalSum + t) + 2*s2 = 2*totalSum
t + 2*s2 = totalSum
s1 - s2 +2*s2 = totalSum
s1 + s2 = totalSum
"""


def spaceOptimization(n, target, arr):
    prev = [0 for i in range(target+1)]
    cur = [0 for i in range(target+1)]

    if arr[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1

    if arr[0] != 0 and arr[0] <= target:
        prev[arr[0]] = 1

    for idx in range(1, n):
        for tar in range(target+1):
            notTake = prev[tar]
            take = 0
            if arr[idx] <= tar:
                take = prev[tar-arr[idx]]

            cur[tar] = take+notTake
        prev = cur
    return prev[target]



def tabulation(n, target, arr):
    dp = [[0 for i in range(target+1)] for j in range(n)]

    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1

    if arr[0] != 0 and arr[0] <= target:
        dp[0][arr[0]] = 1

    for idx in range(1, n):
        for tar in range(target+1):
            notTake = dp[idx-1][tar]
            take = 0
            if arr[idx] <= tar:
                take = dp[idx-1][tar-arr[idx]]

            dp[idx][tar] = take+notTake

    return dp[n-1][target]



def memoization(n, target, arr):
    dp = [[-1 for i in range(target+1)] for j in range(n)]

    def f(idx, t):
        if idx == 0:
            if t == 0 and arr[0] == 0:
                return 2
            if t == 0 or arr[0] == t:
                return 1
            return 0

        if dp[idx][t] != -1:
            return dp[idx][t]

        # explore all possibilities
        notTake = f(idx-1, t)
        take = 0
        if arr[idx] <= t:
            take = f(idx-1, t-arr[idx])
        dp[idx][t] = take + notTake
        return dp[idx][t]
    return f(n-1, target)


def recursion(n, target, arr):

    def f(idx, target):
        if idx == 0:
            if target == 0 and arr[0] == 0:
                return 2
            if target == 0 or arr[0] == target:
                return 1
            return 0
        
        # explore all possibility
        notTake = f(idx-1, target)
        take = 0
        if arr[idx] <= target:
            take = f(idx-1, target-arr[idx])
        return take+notTake
    return f(n-1, target)


def sol(arr, target):
    n = len(arr)
    totalSum = sum(arr)

    if (totalSum-target) % 2:
    	return 0
    required_target = (totalSum-target)//2

    print(recursion(n, required_target, arr))
    print(memoization(n, required_target, arr))
    print(tabulation(n, required_target, arr))
    print(spaceOptimization(n, required_target, arr))

arr = [1, 2, 3, 1]
target = 3

sol(arr, target)




# ==================
# STRIVER SOLUTION
# ==================


mod = int(1e9 + 7)

# Function to find the number of ways to partition an array into two subsets
# with a given target difference using dynamic programming
def findWays(num, tar):
    n = len(num)

    # Initialize a list 'prev' to store results for the previous element
    prev = [0 for i in range(tar + 1)]

    # Initialize 'prev' based on the first element of 'num'
    if num[0] == 0:
        prev[0] = 2  # Two cases - pick and not pick
    else:
        prev[0] = 1  # One case - not pick

    if num[0] != 0 and num[0] <= tar:
        prev[num[0]] = 1  # One case - pick

    for ind in range(1, n):
        # Initialize a list 'cur' to store results for the current element
        cur = [0 for i in range(tar + 1)]
        for target in range(tar + 1):
            notTaken = prev[target]

            taken = 0
            if num[ind] <= target:
                taken = prev[target - num[ind]]

            # Store the result in 'cur' with modulo operation
            cur[target] = (notTaken + taken) % mod
        prev = cur

    # Return the result for the target sum
    return prev[tar]

# Function to calculate the number of ways to achieve a target sum
def targetSum(n, target, arr):
    totSum = 0
    for i in range(n):
        totSum += arr[i]

    # Checking for edge cases
    if (totSum - target) < 0 or ((totSum - target) % 2):
        return 0

    # Calculate and return the number of ways using 'findWays' function
    return findWays(arr, (totSum - target) // 2)

def main():
    arr = [1, 2, 3, 1]
    target = 3
    n = len(arr)

    # Print the number of ways found
    print("The number of ways found is", targetSum(n, target, arr))

# if __name__ == "__main__":
#     main()

