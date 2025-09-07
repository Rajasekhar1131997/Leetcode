# Leetcode Problem 645: Set Mismatch
# https://leetcode.com/problems/set-mismatch/description/
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # initialize an empty hash_map
        hash_map = {}
        # initialize two variables missing and duplicate
        missing = duplicate = -1
        # find the frequency of each value in nums list
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # find the missing value from list
        for i in range(1, len(nums) + 1):
            if i not in hash_map:
                missing = i
            # find the duplicate value
            elif hash_map[i] == 2:
                duplicate = i
        # return the duplicate and missing value in list
        return [duplicate, missing]

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")