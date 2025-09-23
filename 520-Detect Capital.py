# Leetcode Problem 520: Detect Capital
# https://leetcode.com/problems/detect-capital/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # we return True if the letters in the word are capitals, or the letters in the word are all small letters or only the first letter in the word is capital
        return True if word == word.upper() or word == word.lower() or word == word.capitalize() else False

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")