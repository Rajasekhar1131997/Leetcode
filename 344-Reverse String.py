# Leetcode Problem 344: Reverse String
# https://leetcode.com/problems/reverse-string/
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # initialize two pointers left and right, left to the beginning of list and right to the end of the list
        left = 0
        right = len(s) - 1
        # loop until we reverse each character from the list
        while left < right:
            s[left], s[right] = s[right], s[left]
            # move to the right side to process the next character
            left += 1
            # move to the left side to process the next character
            right -= 1

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")