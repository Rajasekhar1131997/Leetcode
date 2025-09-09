# Leetcode Problem 3467: Transform Array by Parity
# https://leetcode.com/problems/transform-array-by-parity/description/
from typing import List
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # loop through each value in nums
        for i in range(len(nums)):
            # if the value is even, we replace it with 0 else 1
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        # sort the numbers in ascending order
        nums.sort()
        # return the sorted array
        return nums

print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")