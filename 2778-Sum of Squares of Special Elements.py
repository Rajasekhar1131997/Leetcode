# Leetcode Problem 2778: Sum of Squares of Special Elements 
# https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
from typing import List
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # find the length of the given list
        n = len(nums)
        # initialize the total to 0
        total = 0
        # loop through each value in list
        for i in range(1, n+1):
            # check if the number is special or not as per the condition listed
            if n % i == 0:
                # summing the squares of all special elements of nums
                total += nums[i-1] * nums[i-1]
        # return the total
        return total

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")