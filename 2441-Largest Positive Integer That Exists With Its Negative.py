# Leetcode Problem 2441: Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # initialize an empty hash_map/dictionary
        hash_map = {}
        # for each value in nums, add that value to hash_map
        for num in nums:
            hash_map[num] = True
        # initialize the max value to -1
        max_value = -1
        # for every value in num
        for num in nums:
            # if the num is > 0 and it's negative exists in hash map
            if num > 0 and -num in hash_map:
                # we get the maximum value
                max_value = max(max_value, num)
        # finally, we return the positive number such that it's negative also exists in array
        return max_value

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")