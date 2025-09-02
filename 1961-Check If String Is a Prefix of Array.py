# Leetcode Problem 1961: Check If String Is a Prefix of Array
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/
from typing import List
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # initialize an empty string prefix
        prefix = ""
        # loop through each word in words list
        for word in words:
            # add that word to the prefix string
            prefix += word
            # if the string s is equal to the prefix, we return True
            if s == prefix:
                return True
            # if string s doesn't start with prefix, we return False
            if not s.startswith(prefix):
                return False
        # return false, if the above cases doesn't work
        return False

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")