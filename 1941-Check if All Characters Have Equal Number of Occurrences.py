# Leetcode Problem 1941: Check if All Characters Have Equal Number of Occurrences
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # initialize an empty hash map to store the frequencies of each character
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        # using set, we can get all the values
        frequencies = set(hash_map.values())
        # if they all have the same frequencies, then our set will contain only one value and we return true, otherwise false
        if len(frequencies) == 1:
            return True
        else:
            return False
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")