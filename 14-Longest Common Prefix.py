# Leetcode Problem 14: Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # initialize the first string in the list as prefix
        prefix = strs[0]
        # loop until we process all the words in the list
        for i in range(len(prefix)):
            # we check each and every word in the list
            for word in strs:
                # if it's not equal to the length of word or prefix[i] != word[i], we return the prefix until that character.
                if i == len(word) or prefix[i] != word[i]:
                    return prefix[:i]
        # we return prefix
        return prefix

print("Time Complexity: O(N.M)")
print("Space Complexity: O(1)")