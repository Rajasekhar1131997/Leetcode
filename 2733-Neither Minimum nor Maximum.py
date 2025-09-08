# Leetcode Problem 2733: Neither Minimum nor Maximum
# https://leetcode.com/problems/neither-minimum-nor-maximum/description/
from typing import List
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # base case, if the given length of nums is less than or equal to 2, we return -1
        if len(nums) <= 2:
            return -1
        # sort the given numbers
        nums.sort()
        # return the second element from the last, which is neither min or max element
        return nums[-2]
    
print("Time Complexity: O(N logN)")
print("Space Complexity: O(1)")

# Solving this problem using O(N) time
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # base case, if the given length of nums is less than or equal to 2, we return -1
        if len(nums) <= 2:
            return -1
        # find the minimum value from the list
        min_val = min(nums)
        # find the maximum value from the list
        max_val = max(nums)
        # check every number from nums list
        for num in nums:
            # if the num is not equal to min and max values, then it's a valid answer
            if num != min_val and num != max_val:
                return num
        # return -1 if it doesn't exist
        return -1

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")