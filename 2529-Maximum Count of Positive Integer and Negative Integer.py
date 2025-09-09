# Leetcode Problem 2529: Maximum Count of Positive Integer and Negative Integer
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # initialize the negative and positive counters to 0
        positive_count = negative_count = 0
        # check each number in nums
        for num in nums:
            # if the num is < 0, we negative count it
            if num < 0:
                negative_count += 1
            # if the num is > 0, we positive count it
            elif num > 0:
                positive_count += 1
        # return the maximum of both counts
        return max(negative_count, positive_count)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")