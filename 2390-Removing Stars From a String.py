# Leetcode Problem 2390: Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/description/
class Solution:
    def removeStars(self, s: str) -> str:
        # initialize an empty list/stack data structure
        stack = []
        # loop through each character in s
        for char in s:
            # if the character is '*', we remove the previously added character from the stack
            if char == '*':
                stack.pop()
            # else, we append the character to stack
            else:
                stack.append(char)
        # finally, return the concatenated string
        return ''.join(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")