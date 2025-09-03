# Leetcode Problem 1047: Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # initialize an empty stack
        stack = []
        # traverse each character from string s
        for ch in s:
            # if the stack is not empty and the top of the character is equal to the current char
            if stack and stack[-1] == ch:
                # we pop the previous character from stack
                stack.pop()
            # else, we append that character to stack
            else:
                stack.append(ch)
        # return the string
        return "".join(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")