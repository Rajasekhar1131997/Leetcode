# Leetcode Problem 3550: Smallest Index With Digit Sum Equal to Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/
from typing import List
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # loop through each index at nums list
        for i in range(len(nums)):
            # assign each value to num
            num = nums[i]
            # initialize sum to 0
            sum = 0
            # find the digit sum
            while num > 0:
                remainder = num % 10
                sum += remainder
                num = num // 10
            # if the digit sum is equal to index, we return that index
            if sum == i:
                return i
        # if there is no match, we return -1
        return -1

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")