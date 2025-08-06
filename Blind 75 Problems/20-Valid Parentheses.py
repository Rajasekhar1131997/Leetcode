# Leetcode Problem 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack or list to add characters
        stack = []
        # Initialize the dictionary with key value pairs like below
        dictionary = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        # Looping through each character in string
        for char in s:
            # Checking if the character is present in predefined dictionary.values
            if char in dictionary.values():
                # Appending that character to the stack
                stack.append(char)
            # Checking if the character is present in predefined dictionary.values
            elif char in dictionary.keys():
                # if the stack is empty or the last element in the stack is not equal
                if not stack or stack[-1] != dictionary[char]:
                    return False
                # pop the element from the stack
                stack.pop()
        # After processing all the characters from the string, check the length of stack.
        # If empty -> return True else False
        if len(stack) == 0:
            return True
        else:
            return False
        
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")