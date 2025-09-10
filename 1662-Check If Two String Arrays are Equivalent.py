# Leetcode Problem 1662: Check If Two String Arrays are Equivalent
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # convert the given word1 list to string
        string1 = "".join(word1)
        # convert the given word2 list to string
        string2 = "".join(word2)
        # check if both strings are equal or not
        return string1 == string2

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")