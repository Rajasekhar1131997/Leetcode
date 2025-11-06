# Leetcode Problem 3442: Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/
class Solution:
    def maxDifference(self, s: str) -> int:
        # initialize an empty hash map
        hash_map = {}
        # get the frequency of each character
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        # initialize max_odd and min_even values to inf
        max_odd = 0
        min_even = float('inf')
        # loop through all the counts in hash map
        for count in hash_map.values():
            # find the min even frequency in hash map
            if count % 2 == 0:
                min_even = min(min_even, count)
            # find the max odd frequency in hash map
            if count % 2 != 0:
                max_odd = max(max_odd, count)
        # finally, return the max difference
        return max_odd - min_even

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")