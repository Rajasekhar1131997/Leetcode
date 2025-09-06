# Leetcode Problem 485: Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # find the length of given list
        n = len(nums)
        # if the length of given list is less than 1, we return 0
        if n < 1:
            return 0
        # if the length is 1 and value is 1, we return 1
        if n == 1 and nums[0] == 1:
            return 1
        # if the length is 1 and value is 0, we return 0
        if n == 1 and nums[0] == 0:
            return 0
        # initialize the count to keep track of consecutive 1's
        count = 0
        # initialize max_count to keep track of max number of consecutive 1's
        max_count = 0
        # loop through each value in array
        for i in range(n):
            # if we find the current value is 1, we increase the count by 1
            if nums[i] == 1:
                count += 1
                # we also find the max_count to keep track of max consecutive 1's
                max_count = max(max_count, count)
            # if we encounter 0 in the array, we reset the count to 0
            if nums[i] == 0:
                count = 0
        # return the max count
        return max_count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")