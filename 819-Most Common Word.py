# Leetcode Problem 819: Most Common Word
# https://leetcode.com/problems/most-common-word/description/
from typing import List
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # converting the given paragraph into lower case letters
        paragraph = paragraph.lower()
        # using regular expression to remove the punctuation from string
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph)
        # splitting the paragraph string separated by space
        paragraph = paragraph.split()
        # initialize an empty hash_map to get frequency of each word
        hash_map = {}
        # loop through every word in paragraph list
        for word in paragraph:
            # get the frequency of word which is not in banned list
            if word not in banned:
                hash_map[word] = hash_map.get(word, 0) + 1
        # find the maximum key of hash_map
        return max(hash_map, key=hash_map.get)
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")