# Leetcode Problem 387: First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # initialize an empty hashmap to store frequency of each character in string s
        frequency = {}
        # logic to get frequency of each character
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        # loop through each character in string s and find the first non-repeating character
        for index, char in enumerate(s):
            # if the frequency of that character is 1, then we return the index
            if frequency[char] == 1:
                return index
        # if there is no non-repeating character, we return -1
        return -1

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")