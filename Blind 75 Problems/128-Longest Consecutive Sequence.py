# Leetcode Problem: 128: Longest Consecutive Sequence Description
# https://leetcode.com/problems/longest-consecutive-sequence/description/
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If the nums list is empty, we return the longest consecutive elements sequence as 0
        if not nums:
            return 0
        # Removing the duplicates from the nums list
        nums_set = set(nums)
        # Intialize the variable longest to keep track of the longest sequence
        longest = 0
        # Loop through each value in nums_set
        for num in nums_set:
            # checking if the previous value is present in the set
            if (num-1) not in nums_set:
                # Initialize the length variable to find the sequence
                length = 0
                # If the current element is the start of the sequence and exists in the set
                while (num+length) in nums_set:
                    length += 1 # Increase the length
                longest = max(longest, length) # update the longest sequence
        return longest # return the longest sequence value

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")