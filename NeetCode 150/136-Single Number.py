# Leetcode Problem 136: Single Number
# https://leetcode.com/problems/single-number/description/
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if the list is empty, we return 0
        if not nums:
            return 0
        # if the length of the list is 1, we return that number
        if len(nums) == 1:
            return nums[0]
        # Initialize an empty dictionary to find the frequency of each number
        hash_map = {}
        # find the frequency of each number from the list
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # loop through the dictionary and find whose count is less than 2 and return that number
        for num, count in hash_map.items():
            if count < 2:
                return num

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")