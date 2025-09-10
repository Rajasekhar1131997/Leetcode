# Leetcode Problem 2278: Percentage of Letter in String
# https://leetcode.com/problems/percentage-of-letter-in-string/description/
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        # count the occurence of letter from the given string
        count = 0
        for char in s:
            if char == letter:
                count += 1
        # finding the percentage of the letter in string
        percentage = (count * 100) // len(s)
        # return the percentage
        return percentage

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")