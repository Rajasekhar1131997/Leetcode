# Leetcode Problem 28: Find the index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# We can also solve this problem in a single statement using python's built-in function str.find().
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # initialize two variables i to track haystack and j to track needle
        i = 0
        j = 0
        # loop until it finds the 1st occurrence in a string
        while i < len(haystack) and j < len(needle):
            # assign the i value to start to keep track of first occurence
            start = i
            # loop until the whole string from needle is matched with haystack
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                # increment the pointers in each string to next character
                i += 1
                j += 1
            # if the string from needle matches
            if j == len(needle):
                # return the first occurrence index
                return start
            # update the i value to continue with the string search
            i = start + 1
            # change the j value to 0 to search again
            j = 0
        # if there is no occurrence of string, then we return -1
        return -1

print("Time Complexity: O(N x M)")
print("Space Complexity: O(1)")