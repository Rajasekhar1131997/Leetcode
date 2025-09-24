# Leetcode Problem 2068: Check Whether Two Strings are Almost Equivalent
# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/description/
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # initialize an empty hashmap
        hash_map = {}
        # loop through each character in word1 and get their frequency
        for char in word1:
            hash_map[char] = hash_map.get(char, 0) + 1
        # loop through each character in word2 and decrease the frequency when we encounter the same character
        for char in word2:
            hash_map[char] = hash_map.get(char, 0) - 1
        
        # if the difference is greater than 3, we return False, otherwise true
        for char_count_diff in hash_map.values():
            if abs(char_count_diff) > 3:
                return False
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")