# Leetcode Problem 1446: Consecutive Characters
# https://leetcode.com/problems/consecutive-characters/description/
class Solution:
    def maxPower(self, s: str) -> int:
        # find the length of the string
        n = len(s)
        # if the length of string is 1, we return 1
        if n == 1: return 1
        # initialize the count to 0
        count = 0
        # initialize the max_count to 0
        max_count = 0
        # loop from the second character from the string
        for i in range(1, n):
            # check if the current char and previous char are same or not
            if s[i] == s[i-1]:
                # if yes, we increase the count by 1
                count += 1
                # keep track of max consecutive same unique character
                max_count = max(count, max_count)
            # if we see other character, we reset the count to 0
            else:
                count = 0
        # return the max_count + 1, since we have to add the first character that we didn't count
        return 1 + max_count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")