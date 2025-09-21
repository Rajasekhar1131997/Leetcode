# Leetcode Problem 2351: First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/description/
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # initialize an empty set to store the unique characters
        seen = set()
        # loop through each character in string s
        for char in s:
            # if the character is already in seen set, we return that char, since it will be the first letter to appear twice
            if char in seen:
                return char
            # else, we keep adding the unique characters to set
            seen.add(char)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")