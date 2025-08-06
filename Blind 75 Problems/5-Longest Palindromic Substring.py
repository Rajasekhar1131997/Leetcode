# Leetcode Problem 5: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initializing an empty result string
        result = ""
        # Initializing the result_length variable to keep track of the length of longest palindromic substring
        result_length = 0
        # Looping through the center of the string
        for i in range(len(s)):
            # when the given string is of odd length
            left, right = i, i
            # checking the boundaries and comparing the characters
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If the length is greater than the result_length
                if (right-left+1) > result_length:
                    # Add the string to the result
                    result = s[left:right+1]
                    # update the current result length
                    result_length = right-left+1
                # move the left pointer to the left to get the previous character
                left -= 1
                # move the right pointer to the right to get the next character
                right += 1
            # When the given string of even length
            left, right = i, i+1
            # checking the boundaries and comparing the characters
            while left >=0 and right < len(s) and s[left] == s[right]:
                # If the length is greater than the result_length
                if (right-left+1) > result_length:
                    # Add the string to the result
                    result = s[left:right+1]
                    # update the current result length
                    result_length = right-left+1
                # move the left pointer to left to get the previous character
                left -= 1
                # move the right pointer to the right to get the next character
                right += 1
        # returning the result string
        return result

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")