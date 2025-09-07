# Leetcode Problem 1394: Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/
from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # initialize an empty hash_map to store frequency of each value
        hash_map = {}
        # find the frequency of each value
        for num in arr:
            hash_map[num] = hash_map.get(num, 0) + 1
        # initialize max_num to keep track of lucky number
        max_num = 0
        # loop through each value and it's count in hash map
        for value, count in hash_map.items():
            # get the max lucky number
            if value == count:
                max_num = max(max_num, value)
        # finally, return the maximum lucky number, else return -1
        return max_num if max_num else -1

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")