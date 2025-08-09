# Leetcode Problem 917: Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert the string into a list so we can modify characters in place
        s = list(s)
        
        # Initialize two pointers: one starting at the beginning, one at the end
        left, right = 0, len(s) - 1
        
        # Continue until the two pointers meet
        while left < right:
            # Case 1: Both characters at left and right are letters
            if (self.isLetter(s[left]) and self.isLetter(s[right])):
                # Swap them
                s[left], s[right] = s[right], s[left]
                # Move both pointers towards the center
                left += 1
                right -= 1
            
            # Case 2: Left is a letter but right is NOT a letter
            elif (self.isLetter(s[left]) and not self.isLetter(s[right])):
                # Move right pointer leftward to find a letter
                right -= 1
            
            # Case 3: Left is NOT a letter (regardless of right)
            else:
                # Move left pointer rightward to find a letter
                left += 1
        
        # Convert the list of characters back into a string
        return ''.join(s)

    def isLetter(self, letter: chr) -> bool:
        # Check if a character is an uppercase or lowercase English letter
        return (ord('A') <= ord(letter) <= ord('Z') or 
                ord('a') <= ord(letter) <= ord('z'))

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")