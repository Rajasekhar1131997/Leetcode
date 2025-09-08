# Leetcode Problem 2828: Check if a String Is an Acronym of Words
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
from typing import List
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # initialize an empty string
        string = ""
        # loop through each word in words to get the first char
        for word in words:
            string += word[0]
        # check if the generated string and given string s matches or not
        return string == s

print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")

# Solving this problem using O(N) time.
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        string = "".join(word[0] for word in words)
        return string == s

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")