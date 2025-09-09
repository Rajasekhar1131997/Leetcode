# Leetcode Problem 2553: Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/description/
from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # initialize an empty result list to store all the sublists
        result = []
        # loop through each num in nums list
        for num in nums:
            # convert each number into string
            num = str(num)
            # convert each string into list
            num = list(num)
            # append that list to result list
            result.extend(num)
        # convert each string into int again
        return [int(x) for x in result]

print("Time Complexity: O(N.D), where D is the average number of digits in number/list")
print("Space Complexity: O(N.D)")