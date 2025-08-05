# Leetcode Problem 1: Two Sum
# https://leetcode.com/problems/two-sum/description/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary
        hash_map = {}
        # Loop through each index and value
        for index, value in enumerate(nums):
            # Find the difference
            difference = target - value
            # Checking if the difference value is present in the dictionary
            if difference in hash_map:
                # If difference value found, return indexes of both values
                return [index, hash_map[difference]]
            # Adding value to the dictionary
            hash_map[value] = index

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")