# Leetcode Problem 3005: Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # initialize empty hash_map
        hash_map = {}
        # get the frequency of each num from nums list
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        # get the maximum frequency
        max_freq = max(hash_map.values())
        # get the sum of max_frequency values
        total = sum(count for count in hash_map.values() if count == max_freq)
        # return the total value
        return total
            
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")