# Leetcode Problem 561: Array Partition
# https://leetcode.com/problems/array-partition/description/
from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort the given numbers to find the pattern
        nums.sort()
        # initialize sum to zero
        sum = 0
        # loop through the given list
        for i in range(len(nums)):
            # summing all the even positions from the array, once we find the pattern, we will understand, why we are doing the summation
            if i % 2 == 0:
                sum += nums[i]
        # return the sum
        return sum

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")