# Leetcode Problem 242: Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length of two strings differ then we return False
        if len(s) != len(t):
            return False
        # Initialize an empty hashmap to get count of each character from string s
        hash_map = {}
        # loop through each character in s and get their frequencies
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        # loop through each character in string t and decrease the count if it's exists in hashmap
        for ch in t:
            # this condition check if the character from string t exists in hashmap or not
            if ch not in hash_map or hash_map[ch] == 0:
                return False
            # decreases the count of that character in hashmap
            hash_map[ch] -= 1
        # return true if everything matches
        return True
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")