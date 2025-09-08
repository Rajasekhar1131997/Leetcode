# Leetcode Problem 3110: Score of a String
# https://leetcode.com/problems/score-of-a-string/description/
class Solution:
    def scoreOfString(self, s: str) -> int:
        # initialize the total to 0
        total = 0
        # loop through each char in the string s
        for i in range(len(s)-1):
            # find the ascii values difference of adjacent characters
            diff = abs(ord(s[i]) - ord(s[i+1]))
            # add the difference for every iteration
            total += diff
        # return the total
        return total

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")