# Leetcode Problem 2562: Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/
from typing import List
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        # initialize the left pointer to start of the array
        i = 0
        # iniatialize the right pointer to end of the array
        j =  len(nums) - 1
        # initialize the sum to 0
        sum = 0
        # two pointer approach
        while i <= j:
            # if the array length is odd, we'll have the same element so we add that element
            if i == j:
                sum += nums[i]
            # if the array length is even, we'll get the first and last elements and concatenate
            else:
                concat = str(nums[i]) + str(nums[j])
                sum += int(concat)
            # move the left pointer to right by 1
            i += 1
            # move the right pointer to left by 1
            j -= 1
        # finally, return the sum
        return sum

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")