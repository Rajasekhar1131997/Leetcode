# Leetcode Problem 680: Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if the substring s[l:r+1] is a palindrome
        def checkValidPalindrome(l, r):
            left, right = l, r
            while left < right:
                if s[left] != s[right]:  # If mismatch found, not a palindrome
                    return False
                left += 1
                right -= 1
            return True  # Substring is a palindrome
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:  
                # If mismatch found, try skipping either left or right character once
                return checkValidPalindrome(left + 1, right) or checkValidPalindrome(left, right - 1)
            left += 1
            right -= 1
        
        # If no mismatch found, the whole string is a palindrome
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")