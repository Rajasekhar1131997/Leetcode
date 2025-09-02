# Leetcode Problem 414: Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/description/
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # convert the given nums list to set to eliminate the duplicate numbers
        nums = set(nums)
        # convert back the set to list
        nums = list(nums)
        # sort the list into descending order
        nums.sort(reverse = True)
        # if len(nums) >= 3, we return the nums[2], which is the third distinct max number
        if len(nums) >= 3:
            return nums[2]
        # else, we simply return the maximum number from the list
        else:
            return nums[0]

print("Time Complexity: O(N logN)")
print("Space Complexity: O(N)")

# This approach takes only O(N) time:
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # initialize the first, second, third max numbers to None
        first, second, third = None, None, None
        # for every num in nums
        for n in nums:
            # if n is already in first, second, and third, we skip it since the nums may contain duplicates
            if n in (first, second, third):
                continue
            # if the first max is None or current n value is greater than first
            if first is None or n > first:
                # we assign the first, second, third to n, first and second
                first, second, third = n, first, second
            # if the second is None or current n value is greater than second
            elif second is None or n > second:
                # assign the second, third values to n and second
                second, third = n, second
            # if the third value is None or current n value is greater than third
            elif third is None or n > third:
                # we assign the third max value to n
                third = n
        # return third max value if it's not none, otherwise return the first max
        return third if third is not None else first

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")