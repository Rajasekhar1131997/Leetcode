# Leetcode Problem 500: Keyboard Row
# https://leetcode.com/problems/keyboard-row/description/
from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # initialize an empty list to store the result
        result = []
        # converting the first row letters to set
        first_row_set = set("qwertyuiop")
        # converting the second row letters to set
        second_row_set = set("asdfghjkl")
        # converting the third row letters to set
        third_row_set = set("zxcvbnm")
        # loop through each word in words
        for word in words:
            # convert that word to set and also changing to lowercase letters
            word_set = set(word.lower())
            # checking if the word set is a subset of any of the letter sets
            if word_set <= first_row_set or word_set <= second_row_set or word_set <= third_row_set:
                # if yes, we add that word to the result
                result.append(word)
        # we return the result list
        return result
    
print("Time Complexity: O(M * N)")
print("Space Complexity: O(M + N)")