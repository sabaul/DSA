"""
--------------------------------------------
SPLIT ARRAY LARGEST SUM + PAINTERS PARTITION
--------------------------------------------

- EXACTLY SAME PROBLEM AS ALLOCATE BOOK
"""

class SubarrayPartitioner:
    # Counts how many partitions are needed for a given max_sum
    def count_partitions(self, a, max_sum):
        partitions = 1  # at least one partition
        subarray_sum = 0  # current subarray sum

        for num in a:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions

    # Finds the minimum largest subarray sum possible for at most k partitions
    def largest_subarray_sum_minimized(self, a, k):
        low = max(a)  # largest element
        high = sum(a)  # sum of all elements

        # Binary search
        while low <= high:
            mid = (low + high) // 2
            partitions = self.count_partitions(a, mid)

            if partitions > k:
                low = mid + 1  # too many partitions
            else:
                high = mid - 1  # try smaller max_sum
        return low


if __name__ == "__main__":
    a = [10, 20, 30, 40]
    k = 2
    sp = SubarrayPartitioner()
    ans = sp.largest_subarray_sum_minimized(a, k)
    print("The answer is:", ans)
