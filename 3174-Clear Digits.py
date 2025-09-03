# Leetcode Problem 3174: Clear Digits
# https://leetcode.com/problems/clear-digits/description/
class Solution:
    def clearDigits(self, s: str) -> str:
        # initialize an empty stack
        stack = []
        # loop through each character in string s
        for ch in s:
            # if the stack is not empty and the current character lies in between 0 - 9, we pop the character
            if stack and (48 <= ord(ch) <= 57):
                stack.pop()
            # else, we push the character to stack
            else:
                stack.append(ch)
        # we return the concatenated string
        return "".join(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")