# Leetcode Problem 2586: Count the Number of Vowel Strings in Range
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # initializing vowels in a set
        vowels = {'a','e','i','o','u'}
        # initializing count to 0
        count = 0
        # checking the range (left, right) inclusively
        for i in range(left, right+1):
            # assign each word from list
            word = words[i]
            # check if the first and last character are present in vowels or not
            if word[0] in vowels and word[-1] in vowels:
                # increase the count
                count += 1
        # return count
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")