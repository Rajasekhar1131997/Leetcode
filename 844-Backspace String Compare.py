# Leetcode Problem 844: Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/description/
from typing import List
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Convert string s into a list of characters for easier manipulation
        s_list = list(s)
        # Convert string t into a list of characters similarly
        t_list = list(t)
        # Compare the processed strings after applying backspace logic using returnString helper method
        return self.returnString(s_list) == self.returnString(t_list)
    
    def returnString(self, list: List[chr]) -> str:
        # Initialize an empty stack to simulate typing with backspaces
        stack = []
        # Iterate over each character in the input list
        for char in list:
            # If current char is '#' and stack is not empty, pop last character (backspace)
            if char == '#':
                if stack:
                    stack.pop()
            # Otherwise, add the current character to the stack (normal typing)
            else:
                stack.append(char)
        # Join all characters in stack to form the final processed string
        return "".join(stack)
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")