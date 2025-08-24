# Leetcode Problem 169: Majority Element
# https://leetcode.com/problems/majority-element/description/
# Solving this problem using Hashtable
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # initialize an empty hash table to get frequencies of each number
        frequency = {}
        # loop through each value in nums list to get their frequencies
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        # logic to check the majority element from the array
        for value, count in frequency.items():
            if count > len(nums)/2:
                return value
    
print("Time Complexity: O(N)")
print("Space COmplexity: O(N)")

# We can solve this problem with O(N) run time and O(1) space complexity
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize our element to None
        element = None
        # initialize count to 0
        count = 0
        # loop through each number in nums list
        for num in nums:
            # if our count is 0, then we assign element to num
            if count == 0:
                element = num
            # since we loop through each number, if we see the same number we increment the count, else decrement the count
            if element == num:
                count += 1
            else:
                count -= 1
        # we return the element
        return element
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")