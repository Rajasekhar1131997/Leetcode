# Leetcode Problem 977: Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for each value in list
        for i in range(len(nums)):
            # find the square of the number
            nums[i] **= 2
        # sort the list using sort() function
        nums.sort()
        # return the nums list
        return nums
    
print("Time Complexity: O(N log N)")
print("Space Complexity: O(1) or O(log N)")

# Solving this problem using Two Pointers Approach
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # initialize the result list with all 0's
        result = [0] * len(nums)
        # Starting the two pointer approach
        left = 0
        right = len(nums) - 1
        # initialize the index to the end, since we fill the result from end
        index = len(nums) - 1
        # loop until we sort all the values from the list
        while left <= right:
            # find the square of left value
            left_squared = nums[left] ** 2
            # find the square of right value
            right_squared = nums[right] ** 2
            # check if the left square is greater than right square and append it to the last
            if left_squared > right_squared:
                result[index] = left_squared
                left += 1
            else:
                result[index] = right_squared
                right -= 1
            # decrease the index pointer by 1
            index -= 1
        # return the result list
        return result
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")