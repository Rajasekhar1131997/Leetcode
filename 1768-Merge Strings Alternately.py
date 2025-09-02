# Leetcode Problem 1768: Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # initialize i pointer to keep track of each character from word1
        i = 0
        # initialize j pointer to keep track of each character from word2
        j = 0
        # initialize an empty result to store the characters alternatively
        result = []
        # loop until we process each words from word1 and word2
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            # incrementing the i pointer in word1
            i += 1
            # incrementing the j pointer in word2
            j += 1
        # if there are any characters leftover to add in word1, add them
        result += word1[i:]
        # if there are any characters leftover to add in word2, add them
        result += word2[j:]
        # converting the result list to string and returning
        return "".join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

# The below code takes only O(1) space without using any space for List
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        output = ""
        while i < len(word1) and j < len(word2):
            output += word1[i] + word2[j]
            i += 1
            j += 1
        # Add leftovers
        output += word1[i:] + word2[j:]
        return output

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")