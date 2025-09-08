# Leetcode Problem 3019: Number of Changing Keys
# https://leetcode.com/problems/number-of-changing-keys/description/
class Solution:
    def countKeyChanges(self, s: str) -> int:
        # convert the given string into lower case
        s = s.lower()
        # initialize count to 0 to keep track of changing keys
        count = 0
        # loop through from char 1 to rest of the string
        for i in range(1, len(s)):
            # compare the current char with previous char, if there is change, count it
            if s[i] != s[i-1]:
                count += 1
        # return the count
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")