# Leetcode Problem 796: Rotate String
# https://leetcode.com/problems/rotate-string/description/
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # if the given strings length are not equal, we return False
        if len(s) != len(goal):
            return False
        # find the length of the given string
        n = len(s)
        # rotate the string n times
        for _ in range(n):
            # check every time if the rotated string is equal to the goal string
            s = s[1:] + s[0]
            if s == goal:
                return True
        # if they are not matching, return False
        return False

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")