# Leetcode Problem 3423: Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/
from typing import List
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # initialize the max_diff to -1
        max_diff = -1
        # find the difference of first and last element, since it's a circular array
        difference = abs(nums[0] - nums[-1])
        if difference > max_diff:
            max_diff = difference
        # loop through the rest of the values from nums array
        for i in range(len(nums)-1):
            # find the difference
            diff = abs(nums[i] - nums[i+1])
            # find the max difference between the values
            max_diff = max(max_diff, diff)
        # return the max_difference
        return max_diff
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")