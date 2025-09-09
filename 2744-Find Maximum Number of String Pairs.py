# Leetcode Problem 2744: Find Maximum Number of String Pairs
# https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/
from typing import List
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # initialize the count to 0
        count = 0
        # loop through each word in words
        for i in range(len(words)):
            # loop through the next word to the end of list
            for j in range(i+1, len(words)):
                # check condition if i < j and check whether the reversed string matches or not
                if i < j:
                    if words[i] == words[j][::-1]:
                        # if yes, we increase the count
                        count += 1
        # return the count
        return count

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")