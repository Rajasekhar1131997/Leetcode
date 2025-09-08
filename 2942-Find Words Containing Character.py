# Leetcode Problem 2942: Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/description/
from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # initialize an empty result list to store indices
        result = []
        # loop through each word in words
        for index, word in enumerate(words):
            # check if the given string is present in word or not
            if x in word:
                # if yes, we append that index to result list
                result.append(index)
        # return the result list at the end
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")