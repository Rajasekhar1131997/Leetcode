# Leetcode Problem 2696: Minimum String Length After Removing Substrings
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
class Solution:
    def minLength(self, s: str) -> int:
        # initialize an empty stack or list to store the characters
        stack = []
        # for each character in string s
        for ch in s:
            # check if the stack is not empty and the pair matches AB and CD
            if stack and ((stack[-1] == 'A' and ch == 'B') or (stack[-1] == 'C' and ch == 'D')):
                # if there is such pair, pop the previously entered character and ignoring the current character from string s
                stack.pop()
            else:
                # if not, we simply push that character to stack/list
                stack.append(ch)
        # we need to return the length of the stack/list as requested.
        return len(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")