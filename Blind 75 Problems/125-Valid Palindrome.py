# Leetcode Problem 125: Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
# Approach - 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if the given string is null or is of length 1, we return true
        if len(s) == 0 or len(s) == 1:
            return True
        # Initialize an empty string
        new_string = ""
        # convert the string from uppercase to lowercase using lower() function
        lowered_string = s.lower()
        # loop through each character in lowered_string
        for char in lowered_string:
            # check if the character is alphanumeric using python built-in function isalnum()
            if char.isalnum():
                # If it's a alphanumeric character, we append that character to new_string
                new_string += char
        # check if the new_string is equal to the reversed string
        return new_string == new_string[::-1]
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")
    
# Approach - 2: Using Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Base case: If the length of the string is 0 or 1, we return True
        if len(s) == 0 or len(s) == 1:
            return True
        # Solving the problem using Two pointer Approach
        # Initialize the left pointer
        left = 0
        # Initialize the right pointer
        right = len(s) - 1
        # Checking until this condition satisfies
        while left < right:
            # If the character from left is not alpha numeric we move/proceed with the next character
            while left < right and not self.isalphaNum(s[left]):
                left += 1
            # If the character from the right is not alpha numeric, we move to the left side of the string from right
            while right > left and not self.isalphaNum(s[right]):
                right -= 1
            # If the left and right characters doesn't match, we return False
            if s[left].lower() != s[right].lower():
                return False
            # Move the left pointer to right side
            left += 1
            # move the right pointer to the left side
            right -= 1
        return True
    # This function is used to check whether the given character is alpha numeric or not, returns boolean value
    def isalphaNum(self, char):
        # built-in ord() function is used to check if the character is unicode/alphanumeric or not
        return (
                ord('a') <= ord(char) <= ord('z') or
                ord('A') <= ord(char) <= ord('Z') or
                ord('0') <= ord(char) <= ord('9')
            )

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")